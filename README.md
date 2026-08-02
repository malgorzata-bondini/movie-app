# 🎞️ Kartoteka — polska klasyka na dziś wieczór

*Bo od trzydziestu minut scrollujesz Netflixa i dalej nic nie wybrałaś.*

Ta aplikacja rozwiązuje dokładnie jeden problem: **nie potrafisz się zdecydować, co obejrzeć**. Zamiast przeglądać katalog po raz siedemnasty, ustawiasz nastrój, dekadę i długość, klikasz jeden przycisk — i już, decyzja podjęta za Ciebie, obwiniaj apkę, nie siebie.

129 polskich klasyków. Zero paraliżu decyzyjnego. Sto procent szans, że i tak obejrzysz coś innego.

---

## Wygląda tak

![Nagłówek aplikacji](screenshots/hero.png)

Papierowo-beżowa kolorystyka i czerwony akcent, bo skoro kartoteka, to niech wygląda jak kartoteka, a nie jak kolejny czarny dashboard z gradientem.

## Wybierasz filtry jak profesjonalny kinoman

![Filtry: nastrój, dekada, długość](screenshots/filtry.png)

Nastrój, dekada, długość. Trzy suwaki decyzyjności, żebyś mogła udawać, że to Ty wybierasz, a nie ślepy los.

## …i klikasz „Losuj”

![Karta z wynikiem losowania](screenshots/karta.png)

Szpula się kręci (dosłownie — animowana perforacja jak w prawdziwym projektorze), tytuły migają, aż wyląduje jeden. Do kompletu: rok, reżyser, czas trwania, jedno zdanie o co chodzi, i albo słynny cytat („Kargul, podejdź no do płota”), albo scena, którą się pamięta, gdy nie mam stuprocentowej pewności co do brzmienia kwestii.

## Cała kartoteka, jakbyś jednak chciała przeglądać ręcznie

![Rozwijana lista katalogu](screenshots/katalog.png)

Bo czasem jednak wiesz, czego chcesz, i to jest ok.

---

## Co tu naprawdę siedzi

- **129 filmów** — od kina przedwojennego (*Piętro wyżej*, 1937) po *Boże Ciało* (2019). Wszystko, co powinnaś była obejrzeć w liceum, a obejrzałaś dopiero teraz, bo apka Ci kazała.
- **Losowanie bez powtórek** — dopóki nie przejdzie przez całą pulę pasującą do filtrów. Apka pamięta, co już wylosowałaś, więc nie oglądasz *Vabanku* piąty raz z rzędu (chyba że naprawdę chcesz, wtedy filtruj węziej).
- **Link do Filmwebu** — jeśli w arkuszu jest wypełniona kolumna „Link Filmweb", prowadzi prosto na stronę filmu; jeśli nie, spada na wyszukiwarkę Filmwebu (czasem trafia od razu, czasem pokazuje listę wyników — wtedy warto dopisać link ręcznie, patrz niżej).
- **Baza w Excelu, nie w kodzie** — dopisujesz film jak zwykły wiersz w tabeli, nie musisz znać Pythona. Prawdziwy przełom cywilizacyjny.

## Dla dociekliwych: jak to jest zbudowane

Bez owijania w bawełnę:

| Plik | Rola |
| --- | --- |
| `app.py` | cały interfejs, filtry, logika losowania |
| `filmy.xlsx` | baza filmów — **tu dopisujesz nowe tytuły**, zakładka „Filmy” + ściągawka w „Instrukcja” |
| `films.py` | listy filtrów (nastroje/dekady/długości) + wczytywanie `filmy.xlsx` |
| `requirements.txt` | Streamlit, pandas, openpyxl |
| `.streamlit/config.toml` | ta beżowo-czerwona paleta, o której była mowa wyżej |

### Uruchomienie lokalnie

```bash
pip install -r requirements.txt
streamlit run app.py
```

### Publikacja na Streamlit Community Cloud

1. Wrzuć wszystkie pliki na GitHuba, z zachowaniem `.streamlit/` (tak, ten folder z kropką — to nie błąd).
2. [share.streamlit.io](https://share.streamlit.io) → zaloguj się kontem GitHub.
3. **Create app → Deploy a public app from GitHub**.
4. Repozytorium, branch `main`, plik główny `app.py`.
5. **Deploy** i czekaj minutę-dwie.

Każdy kolejny push na `main` przebudowuje appkę samodzielnie — nawet nie musisz nic klikać na Streamlit Cloud.

### Dopisywanie filmów (bez pisania kodu, obiecuję)

Otwórz `filmy.xlsx`, zakładka **Filmy**, dopisz wiersz na dole:

| Kolumna | Co wpisać |
| --- | --- |
| Tytuł | dokładny tytuł |
| Reżyser | imię i nazwisko (kilku — przecinkiem) |
| Rok | sama liczba |
| Czas (min) | sama liczba |
| Nastroje | z listy: Śmiech, PRL, Wojna, Egzystencjalne, Kryminał, Kostium, Obyczajowe, Kino osobne — przecinkiem |
| Cytat | tylko jeśli masz stuprocentową pewność co do słowa |
| Scena | jedno zdanie o zapamiętanym obrazie, gdy Cytatu nie ma |
| Zdanie | jedno zdanie, o czym jest film |
| Link Filmweb | opcjonalne — wklej dokładny adres strony filmu (np. `https://www.filmweb.pl/film/Pan+Tadeusz-1999-630`), jeśli wiesz, że wyszukiwarka nie trafia we właściwy tytuł. Puste pole = apka sama zbuduje link do wyszukiwania. |

Wypełnij Cytat **albo** Scenę — jedno wystarczy. Zapisz, wgraj na GitHuba w miejsce starego pliku, gotowe.

Jeśli coś schrzanisz w wierszu (brak roku, zły nastrój, zero cytatu i sceny naraz) — apka się nie wywali. Po prostu pominie ten wiersz i pokaże ostrzeżenie na górze strony z numerem wiersza, żebyś wiedziała, co poprawić. Miła jest.

---

*Made with 🎬, Streamlit i lekką obsesją na punkcie polskiego kina moralnego niepokoju.*
