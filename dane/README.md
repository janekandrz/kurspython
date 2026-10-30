# Słownik i pochodzenie danych

Wszystkie dane utworzono na potrzeby kursu. Są syntetyczne: nie opisują prawdziwej
kawiarni, biblioteki ani osób. Nie pobieramy niczego z sieci podczas lekcji.
Pliki mają kodowanie UTF-8, separator przecinek i nagłówek w pierwszym wierszu.

## Kawiarnia — `sprzedaz_kawiarni.csv`

Zakres poprawnych dat: **1 stycznia–31 marca 2026**. Jedna obserwacja to pozycja
sprzedaży jednego produktu, potencjalnie kilku sztuk. ID jest unikalnym numerem
pozycji, a nie wspólnym numerem paragonu. Nie ma informacji o klientach ani kosztach.

| Kolumna | Znaczenie | Format źródłowy |
|---|---|---|
| `id_transakcji` | Identyfikator pozycji sprzedaży | Liczba całkowita |
| `data` | Dzień sprzedaży | Tekst `RRRR-MM-DD` |
| `produkt` | Espresso, Latte, Herbata, Sernik, Croissant lub Kanapka | Tekst |
| `kategoria` | napoje / jedzenie | Tekst, możliwy brak |
| `liczba_sztuk` | Sprzedana ilość, od 1 do 4 | Liczba, możliwy brak |
| `cena_jednostkowa` | Cena jednej sztuki w zł | Tekst z przecinkiem, np. `16,00` |
| `kanal` | na miejscu / na wynos | Tekst |
| `rabat_proc` | Rabat procentowy, w całym tym zbiorze równy 0 | Liczba |

Przychód w zadaniach to `liczba_sztuk * cena_jednostkowa`. Pole rabatu jest
stałe, więc nie zmienia wyniku. Przy innym zbiorze z rabatami trzeba dostosować wzór.
Nie wyliczamy zysku, kwot netto ani podatku.

### Celowe problemy i przyjęte reguły

- **243 wiersze źródłowe**, w tym 3 dokładne kopie pozycji (ID 6, 46, 86).
  Usuwamy powtórzenia ID, pozostawiając pierwszy rekord: 240 pozycji.
- **3 brakujące ilości** (ID 13, 75, 156). Nie znamy poprawnych wartości;
  odrzucamy te pozycje z obliczeń ilości i przychodu, zapisując je osobno.
- **1 niepoprawna data** `2026-02-30` (ID 206). Odrzucamy tę pozycję
  z przygotowanej wspólnej wersji danych, choć można byłoby osobno rozważyć
  zachowanie jej w analizie niewymagającej daty.
- **2 brakujące kategorie** (ID 19, 120). Uzupełniamy je na podstawie znanego
  przypisania produktów: Espresso, Latte i Herbata → napoje; pozostałe → jedzenie.
- **3 nazwy ze spacjami** na początku i końcu (ID 5, 66, 131). Przycinamy tekst.
- Wszystkie ceny zamieniamy z tekstu z przecinkiem na liczby.

`sprzedaz_kawiarni_gotowa.csv` to wzorcowy rezultat: **236 pozycji**, bez braków
i duplikatów, z ceną zapisaną liczbowo z kropką. Wczytaj datę przez `parse_dates`.
Wynik analizy dotyczy zachowanych rekordów. Nie zastępuje pełnej ewidencji sprzedaży.

## Biblioteka — `wypozyczenia_biblioteki.csv`

**Stan na 30 czerwca 2026.** 180 wypożyczeń rozpoczętych od 1 stycznia
do 30 maja 2026. Dane wygenerowano tylko dla tego okna rozpoczęć; brak nowych
wypożyczeń w czerwcu nie jest informacją o działaniu biblioteki.

| Kolumna | Znaczenie |
|---|---|
| `id_wypozyczenia` | Unikalny numer wypożyczenia |
| `id_czytelnika` | Syntetyczny identyfikator, może występować wiele razy |
| `kategoria` | literatura / reportaż / nauka / dla dzieci |
| `data_wypozyczenia` | Początek wypożyczenia, `RRRR-MM-DD` |
| `data_zwrotu` | Data oddania; pusta, gdy nadal nie oddano na dzień stanu |
| `filia` | Centrum / Północ / Południe |

150 wypożyczeń jest zakończonych, 30 nadal otwartych. Brak daty zwrotu jest
znaczącą informacją, nie błędem. Licz wszystkie 180 zdarzeń przy porównaniu
popularności, ale czas zakończonych wypożyczeń oblicz na 150 zwrotach.
Nie ma terminów wymaganych zwrotów, więc nie da się ustalić opóźnień.
