# Ściąga: Python, pandas i wykresy

## Python

```python
cena = 16                       # przypisanie
produkt = "Latte"                # tekst
ilosci = [2, 3, 1]               # lista
rekord = {"nazwa": "Latte", "cena": 16}  # słownik
print(ilosci[0])                 # pierwszy element: 2
print(rekord["cena"])            # wartość pod kluczem: 16
print(sum(ilosci) / len(ilosci))  # średnia niepustej listy

if cena >= 15:
    print("Co najmniej 15 zł")

def wartosc(cena, sztuki):
    return cena * sztuki

print(wartosc(16, 3))
```

`=` przypisuje, `==` porównuje, `!=` oznacza „różne”, `*` mnoży, `/` dzieli.
Liczby ułamkowe zapisuj z kropką. Python rozróżnia wielkość liter.

## pandas

Fragmenty poniżej zakładają, że uruchomiono komórkę z `DANE` i `WYNIKI`
z notebooka kursu. Kolejne linie pokazują osobne operacje na tej samej tabeli.

```python
import pandas as pd

df = pd.read_csv(DANE / "sprzedaz_kawiarni_gotowa.csv", parse_dates=["data"])
df.head()                           # początek
df.shape                            # (wiersze, kolumny), bez nawiasów ()
df.info()                           # typy i kompletność
df["liczba_sztuk"].describe()        # statystyki jednej miary
df.isna().sum()                     # liczba braków w kolumnach
df.duplicated(subset="id_transakcji").sum()

df["produkt"]                       # jedna kolumna: Series
df[["produkt", "kanal"]]            # kilka kolumn: DataFrame
df[df["liczba_sztuk"] >= 2]         # filtr
df[(df["liczba_sztuk"] >= 2) & (df["kanal"] == "na wynos")]
df.sort_values("liczba_sztuk", ascending=False)

df["przychod"] = df["liczba_sztuk"] * df["cena_jednostkowa"]
df["produkt"].value_counts()         # liczba wierszy według produktu
df.groupby("produkt")["liczba_sztuk"].sum()  # suma sztuk
df.groupby("produkt")["przychod"].sum()
df.to_csv(WYNIKI / "analiza.csv", index=False)
```

W maskach pandas: `&` = i, `|` = lub, `~` = odwrócenie. Każde porównanie
łączone z drugim ujmij w nawiasy. Na datę zamieniaj przez `pd.to_datetime()`;
właściwości dat są pod `.dt`, np. `df["data"].dt.month`.

## Czyszczenie: wybierz świadomie

```python
df = df.drop_duplicates(subset="id_transakcji").copy()
df["produkt"] = df["produkt"].str.strip()
```

Nie usuwaj ani nie uzupełniaj wszystkich braków automatycznie. Najpierw ustal,
co oznacza brak. Tekstową cenę z przecinkiem konwertuj jak w lekcji 4;
gotowy plik ma już liczby i nie wymaga ponownego użycia `.str` na cenie.

## Wykresy

```python
import matplotlib.pyplot as plt

tabela = df.groupby("produkt")["przychod"].sum().sort_values()
ax = tabela.plot.barh(figsize=(8, 4))
ax.set(title="Przychód według produktu", xlabel="Przychód [zł]", ylabel="Produkt")
plt.tight_layout()
ax.get_figure().savefig(WYNIKI / "produkty.png", dpi=150, bbox_inches="tight")
plt.show()
```

Słupki porównują kategorie. Linia pokazuje uporządkowany czas. Histogram
pokazuje rozkład jednej zmiennej liczbowej. Punkty zestawiają dwie zmienne liczbowe.
Do każdego wykresu dopisz jedno zdanie o wyniku i jedno o ograniczeniu.
