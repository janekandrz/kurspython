# Python do pracy z danymi — od zera

Praktyczny kurs po polsku: podstawy Pythona → pandas → wykresy → własna analiza.
Nie wymaga doświadczenia w programowaniu. Wystarczy umieć korzystać z plików,
folderów i przeglądarki oraz znać podstawowe działania i procenty.

**Forma:** 8 spotkań po 90–120 minut, krótkie prace własne i projekt końcowy.
Na dopracowanie projektu zaplanuj dodatkowe 30–60 minut. Dla osób potrzebujących
więcej czasu lekcje 2 i 4 można podzielić na dwa spotkania.

## Pierwsze uruchomienie

Potrzebny jest Python 3.11 lub nowszy (kurs sprawdzono na Pythonie 3.12).
Otwórz terminal w folderze tego kursu. Na macOS lub Linux:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m jupyterlab
```

Na Windows w PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m jupyterlab
```

JupyterLab otworzy się w przeglądarce. W panelu plików wejdź do `notebooks/`
i otwórz **01_pierwszy_notebook.ipynb**. Jeżeli przeglądarka się nie otworzy,
skopiuj lokalny adres wyświetlony w terminalu. Pozostaw terminal otwarty podczas pracy.
Internet jest potrzebny do instalacji; później lekcje i dane działają lokalnie.

## Jak pracować

1. Uruchamiaj komórki od góry przez **Shift+Enter**. Wybierz kernel Python 3,
   jeśli Jupyter o niego zapyta.
2. Czytaj krótkie wyjaśnienia, przewiduj wyniki i zmieniaj przykłady.
3. W ćwiczeniach zastąp komentarz własnym kodem. Puste miejsca są zamierzone.
4. Podpowiedzi otwieraj po pierwszej próbie. Odpowiedzi są w `rozwiazania/`.
5. Zapisuj wnioski w komórkach Markdown. Kliknij je dwa razy, aby edytować.
6. Na koniec wybierz **Kernel → Restart Kernel and Run All Cells**, sprawdź
   wyniki i zapisz. To wykrywa korzystanie z wcześniej zapamiętanych zmiennych.

Przed ćwiczeniami możesz wykonać kopię notebooka przez **File → Save Notebook As**.
Zostaw ją wewnątrz folderu kursu, żeby kod znalazł lokalne dane.

## Kolejność lekcji

| Lekcja | Notebook | Efekt pracy |
|---|---|---|
| 1 | [Pierwszy notebook](notebooks/01_pierwszy_notebook.ipynb) | Obliczenia, zmienne, liczby, tekst i proste błędy |
| 2 | [Minimum Pythona](notebooks/02_minimum_pythona.ipynb) | Listy, słowniki, warunki, funkcje i prosta pętla |
| 3 | [Pierwszy DataFrame](notebooks/03_pierwszy_dataframe.ipynb) | Wczytanie CSV i audyt danych |
| 4 | [Czyszczenie](notebooks/04_czyszczenie.ipynb) | Filtry, braki, duplikaty, typy i zapis pliku |
| 5 | [Pytania do danych](notebooks/05_pytania_do_danych.ipynb) | Nowe kolumny, grupowanie, rankingi i udziały |
| 6 | [Wykresy](notebooks/06_wykresy.ipynb) | Słupki, linie, histogramy, punkty i zapis PNG |
| 7 | [Analiza biblioteki](notebooks/07_analiza_biblioteki.ipynb) | Nowy zbiór, daty i analiza z mniejszą pomocą |
| 8 | [Projekt](notebooks/08_projekt.ipynb) | Własne pytania, analiza, wykresy i wnioski |

Każdy notebook uruchamia się niezależnie. Lekcje 5–6 korzystają z przygotowanej
czystej kopii danych; nie wymagają plików zapisanych przez uczestnika w lekcji 4.
Materiały pozostają jednak w kolejności zależnej od poznanych pojęć.

## Co jest w środku

- `notebooks/` — lekcje, zadania, podpowiedzi, kontrole odpowiedzi i prace własne.
- `rozwiazania/` — odpowiedzi do ćwiczeń i przykładowy projekt; otwieraj po próbie.
- `dane/` — lokalne, syntetyczne dane kawiarni i biblioteki, bez danych osobowych.
- [Słownik danych](dane/README.md) — znaczenie pól, zakres i celowe błędy.
- [Ściąga](materialy/sciaga.md) — najważniejsza składnia na jednej liście.
- [Przewodnik prowadzącego](materialy/prowadzacy.md) — przebieg zajęć i ocena projektu.
- `wyniki/` — miejsce na własne CSV i wykresy; pliki powstają podczas pracy.

## Gdy coś nie działa

- **`ModuleNotFoundError: pandas`**: uruchom Jupyter z tego samego środowiska,
  w którym wykonano instalację. Zamknij go przez Ctrl+C w terminalu, aktywuj
  `.venv` i ponownie uruchom `python -m jupyterlab`.
- **`NameError`**: sprawdź literówkę i wykonaj wcześniejsze komórki; po restarcie
  znikają wszystkie wartości zmiennych.
- **Brak pliku / `StopIteration` w komórce pomocniczej**: notebook musi znajdować
  się w folderze kursu lub jego podfolderze. Nie przenoś samego notebooka bez danych.
- **Zmieniony kod, stary wynik**: wykonaj komórkę ponownie; edycja nie uruchamia kodu.
- **Komórka ma `[*]`**: obliczenia jeszcze trwają. Jeżeli utknęły, wybierz
  **Kernel → Interrupt Kernel**, a w razie potrzeby restart i wykonanie całości.

## Sprawdzenie materiałów przez prowadzącego

Po aktywacji środowiska:

```sh
python -m pip install -r requirements-dev.txt
python scripts/check_notebooks.py
```

Kontrola uruchamia wszystkie 16 notebooków w świeżych jądrach oraz sprawdza,
czy proces czyszczenia odtwarza dostarczony czysty CSV. Działa w kopii tymczasowej,
więc nie nadpisuje Twoich wyników. Sprawdza przykłady i gotowe rozwiązania;
nie rozwiązuje pustych miejsc za uczestnika ani nie ocenia jego odpowiedzi.
