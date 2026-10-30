"""Execute course examples and answers in isolated kernels; preserve student files."""
from pathlib import Path
import base64
import os
import shutil
import sys
import tempfile

import nbformat
from nbclient import NotebookClient
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]


def check_data():
    raw = pd.read_csv(ROOT / "dane/sprzedaz_kawiarni.csv")
    clean = raw.drop_duplicates(subset="id_transakcji").copy()
    clean["produkt"] = clean["produkt"].str.strip()
    clean["cena_jednostkowa"] = (
        clean["cena_jednostkowa"].str.replace(",", ".", regex=False).astype(float)
    )
    categories = {
        "Espresso": "napoje", "Latte": "napoje", "Herbata": "napoje",
        "Sernik": "jedzenie", "Croissant": "jedzenie", "Kanapka": "jedzenie",
    }
    clean["kategoria"] = clean["kategoria"].fillna(clean["produkt"].map(categories))
    clean["data"] = pd.to_datetime(clean["data"], format="%Y-%m-%d", errors="coerce")
    clean = clean.dropna(subset=["liczba_sztuk", "data"]).copy()
    clean["liczba_sztuk"] = clean["liczba_sztuk"].astype(int)
    expected = pd.read_csv(ROOT / "dane/sprzedaz_kawiarni_gotowa.csv", parse_dates=["data"])
    pd.testing.assert_frame_equal(clean.reset_index(drop=True), expected)
    assert len(raw) == 243 and len(clean) == 236
    assert not clean.isna().any().any()
    assert not clean["id_transakcji"].duplicated().any()
    dates = pd.date_range(clean["data"].min(), clean["data"].max())
    assert len(dates.difference(clean["data"].unique())) == 0

    loans = pd.read_csv(ROOT / "dane/wypozyczenia_biblioteki.csv")
    started = pd.to_datetime(loans["data_wypozyczenia"])
    returned = pd.to_datetime(loans["data_zwrotu"])
    assert len(loans) == 180 and returned.isna().sum() == 30
    assert not loans["id_wypozyczenia"].duplicated().any()
    assert (returned.dropna() <= pd.Timestamp("2026-06-30")).all()
    assert ((returned - started).dropna().dt.days >= 0).all()
    print("OK — dane i odtworzenie procesu czyszczenia", flush=True)


def main():
    # Ensure the generic python3 kernelspec uses this virtual environment.
    os.environ["PATH"] = str(Path(sys.executable).parent) + os.pathsep + os.environ["PATH"]
    check_data()
    paths = sorted(ROOT.glob("notebooks/*.ipynb")) + sorted(ROOT.glob("rozwiazania/*.ipynb"))
    assert len(paths) == 16, f"Oczekiwano 16 notebooków, znaleziono {len(paths)}"
    failures = []
    chart_count = 0
    # Set COURSE_QA_DIR to retain executed copies and figures for manual inspection.
    export_dir = Path(os.environ["COURSE_QA_DIR"]).resolve() if os.environ.get("COURSE_QA_DIR") else None
    if export_dir:
        export_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="python-course-") as temporary:
        work = Path(temporary)
        shutil.copytree(ROOT / "dane", work / "dane")
        for path in paths:
            relative = path.relative_to(ROOT)
            cwd = work / relative.parent
            cwd.mkdir(exist_ok=True)
            notebook = nbformat.read(path, as_version=4)
            nbformat.validate(notebook)
            try:
                NotebookClient(
                    notebook, timeout=120, kernel_name="python3",
                    resources={"metadata": {"path": str(cwd)}},
                    allow_errors=False,
                ).execute()
                for cell_index, cell in enumerate(notebook.cells):
                    for output_index, output in enumerate(cell.get("outputs", [])):
                        png = output.get("data", {}).get("image/png")
                        if png:
                            chart_count += 1
                            if export_dir:
                                name = f"{relative.parent.name}_{path.stem}_{cell_index}_{output_index}.png"
                                (export_dir / name).write_bytes(base64.b64decode(png))
                if export_dir:
                    target = export_dir / relative
                    target.parent.mkdir(exist_ok=True)
                    nbformat.write(notebook, target)
                print(f"OK — {relative}", flush=True)
            except Exception as error:
                failures.append((relative, str(error)))
                print(f"BŁĄD — {relative}: {error}", flush=True)
    if failures:
        raise SystemExit(f"Niepowodzenie: {len(failures)} notebooków.")
    assert chart_count >= 10, f"Zbyt mało wykresów do kontroli: {chart_count}"
    print(f"Gotowe: {len(paths)} notebooków, {chart_count} wykresów. Puste ćwiczenia wymagają pracy uczestnika.")


if __name__ == "__main__":
    main()
