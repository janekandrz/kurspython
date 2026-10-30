# Przewodnik prowadzącego

## Założenia

Uczestnik zaczyna bez znajomości programowania. Celem jest mała samodzielna
analiza CSV: od pytania i kontroli jakości po wykres i ostrożny wniosek.
Nie wymagamy pamięciowego odtwarzania składni. Ściąga i wcześniejsze notebooki
mogą być otwarte również podczas projektu.

Przed pierwszym spotkaniem sprawdź instalację i otwórz pierwszy notebook na
komputerze uczestnika. Na pomoc instalacyjną zarezerwuj osobne 20–30 minut.
Nie zużywaj na to całego wprowadzenia do Pythona.

## Rytm spotkania

Przykładowy rozkład 105 minut: 10 minut przypomnienia i pytania, 15 minut
demonstracji, 20 minut modyfikowania przykładów, 5 minut przerwy, 30 minut
samodzielnych ćwiczeń, 15 minut omawiania odpowiedzi, 10 minut interpretacji
i sprawdzenia notebooka po restarcie. Dostosuj do tempa ucznia.

Najpierw poproś o przewidywanie wyniku. Potem uruchom kod. Po zadaniu poproś
o wyjaśnienie odpowiedzi po polsku, z jednostką. Gdy uczestnik utknie, zapytaj,
co chciał uzyskać i co już sprawdził, zanim pokażesz rozwiązanie.

## Cele kontrolne i typowe trudności

| Lekcja | Zanim przejdziesz dalej | Na co uważać |
|---|---|---|
| 1 | Uczestnik zmienia dane wejściowe i przelicza wynik | `=` kontra równość, tekst kontra liczba, stare wyniki komórek |
| 2 | Wybiera wartość ze słownika i wywołuje funkcję | Indeksy od zera, wcięcia, `print` kontra `return` |
| 3 | Objaśnia znaczenie wiersza i wskazuje problemy | Liczba pozycji nie oznacza liczby sztuk lub klientów |
| 4 | Odtwarza 236 czystych rekordów i uzasadnia decyzje | Zastępowanie braków zerem, usuwanie prawdziwych zdarzeń jako duplikatów |
| 5 | Liczy grupy i sprawdza wspólny mianownik udziałów | Liczenie wierszy zamiast sztuk, średni paragon bez ID paragonu |
| 6 | Dobiera wykres do pytania i opisuje jego osie | Niewłaściwa agregacja, brak jednostek, wnioskowanie o przyczynach |
| 7 | Zachowuje otwarte wypożyczenia tam, gdzie są potrzebne | Odrzucenie otwartych rekordów z całej analizy |
| 8 | Notebook działa od początku i odpowiada na trzy pytania | Nadmiar wydruków, wnioski bez liczb, mylenie hipotezy z wynikiem |

## Dostosowanie tempa

Jeżeli listy i słowniki nadal sprawiają trudność, podziel lekcję 2. Własne
funkcje i pętlę można potraktować jako krótkie rozpoznawanie zapisu i wrócić
do nich później. Nie blokuj pandas na opanowaniu zaawansowanej składni.

W lekcji 4 w razie potrzeby rozdziel wybieranie danych od czyszczenia.
W lekcji 6 najpierw opanuj słupki i linię, potem histogram i punkty.
Dla szybszych osób: porównanie filii, udział otwartych wypożyczeń w kategoriach
lub tygodniowy przychód. Nie dodawaj na tym etapie klas ani uczenia maszynowego.

## Rozwiązania

Notebooki w `rozwiazania/` uruchamiają się samodzielnie. Zawierają odpowiedzi
do nazwanych ćwiczeń. Kod omawianych przykładów i pełny proces czyszczenia
są w notebookach lekcji. Odpowiedzi do lekcji 4 korzystają z gotowej kopii,
więc nie zastępują samodzielnego przejścia procesu czyszczenia.
Pytania refleksyjne i prace własne omawiaj indywidualnie.
Projekt przykładowy przedstawia jeden dopuszczalny kierunek, nie wzorzec do przepisania.

## Ocena projektu

Użyj rubryki z lekcji 8: pytania i miary, jakość danych, obliczenia, wykresy,
wnioski i odtwarzalność — po 0–2 punkty. Cel to przynajmniej 8/10,
bez istotnego błędu obliczeniowego. Poproś o pokazanie tabeli źródłowej jednego
wykresu i wyjaśnienie mianownika jednego procentu. To lepiej sprawdza rozumienie
niż odpytywanie z nazw metod.

Informacja zwrotna: wskaż jeden trafny element, jeden konkretny problem i jedną
poprawkę do wykonania. Po poprawce ponownie sprawdź restart i wykonanie całości.

## Granice kursu

Nie wprowadzamy łączenia wielu tabel, zaawansowanej statystyki, scrapingu,
obiektowości ani modeli predykcyjnych. Naturalnym dalszym krokiem są `merge`,
bardziej rozbudowana praca z datami i własne dane uczestnika.
