# Kartoteka — polska klasyka

Losowanie polskiego klasyka na wieczór: filtry (nastrój, dekada, długość), animowane losowanie i karta z cytatem lub zapamiętaną sceną oraz linkami do JustWatch i Filmwebu. Baza: 129 tytułów, od kina przedwojennego po nową klasykę — trzymana w zwykłym pliku Excela.

## Pliki

| plik | co zawiera |
| --- | --- |
| `app.py` | cały interfejs i logika losowania |
| `filmy.xlsx` | **baza filmów — tu dopisujesz nowe tytuły** (arkusz „Filmy” + arkusz „Instrukcja”) |
| `films.py` | stałe listy filtrów (nastroje/dekady/długości) + funkcja wczytująca `filmy.xlsx` |
| `requirements.txt` | zależności: Streamlit, pandas, openpyxl |
| `.streamlit/config.toml` | paleta kolorów |

## Lokalnie

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Publikacja na Streamlit Community Cloud

1. Utwórz publiczne repozytorium na GitHubie i wrzuć do niego wszystkie pliki, zachowując katalog `.streamlit/` (w tym `filmy.xlsx` — to plik binarny, wrzuć go tak jak jest, bez otwierania w edytorze tekstu).
2. Wejdź na https://share.streamlit.io i zaloguj się kontem GitHub.
3. **Create app → Deploy a public app from GitHub**.
4. Wskaż repozytorium, gałąź `main` i plik główny `app.py`.
5. **Deploy**. Po chwili dostaniesz adres w formacie `https://<nazwa>.streamlit.app` — publiczny, do wysłania komukolwiek.

Każdy push na `main` przebudowuje aplikację automatycznie.

## Dopisywanie filmów — w Excelu

Otwórz `filmy.xlsx`, zakładka **Filmy**. Dopisz wiersz na dole tabeli z kolumnami:

| kolumna | co wpisać |
| --- | --- |
| Tytuł | dokładny tytuł filmu |
| Reżyser | imię i nazwisko (kilku — oddziel przecinkiem) |
| Rok | rok premiery, sama liczba |
| Czas (min) | długość w minutach, sama liczba |
| Nastroje | jeden lub kilka z: Śmiech, PRL, Wojna, Egzystencjalne, Kryminał, Kostium, Obyczajowe, Kino osobne — oddzielone przecinkiem |
| Cytat | zweryfikowana kwestia z filmu — zostaw puste, jeśli nie masz pewności co do słowa |
| Scena | jedno zdanie o zapamiętanym obrazie — używane, gdy Cytat jest pusty |
| Zdanie | jedno zdanie, o czym jest film |

Zakładka **Instrukcja** ma tę samą ściągawkę wewnątrz pliku. Wypełnij Cytat **albo** Scenę (jedno wystarczy), zawsze uzupełnij Zdanie.

Zapisz plik, wgraj go na GitHuba w miejsce starego `filmy.xlsx` (przez przeglądarkę: wejdź w plik w repo → *Edit* / *Upload file* → zamień) — Streamlit Cloud przebuduje aplikację sam.

**Kontrola błędów:** jeśli w wierszu zabraknie roku, czasu, cytatu+sceny albo wpiszesz nastrój spoza listy, aplikacja nie wywali się — pominie ten wiersz i pokaże na górze strony rozwijane ostrzeżenie z numerem wiersza i opisem problemu, żeby łatwo było go poprawić.
