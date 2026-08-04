# 🎞️ Kartoteka: polska klasyka na dziś wieczór

*Bo od trzydziestu minut scrollujesz Netflixa i dalej nic.*

Ta aplikacja rozwiązuje dokładnie jeden problem: **nie potrafisz się zdecydować, co obejrzeć**. Zamiast przeglądać katalog po raz siedemnasty, ustawiasz nastrój, dekadę i długość, klikasz jeden przycisk iiii już, decyzja podjęta za Ciebie, obwiniaj apkę, nie siebie.

130 polskich klasyków. Zero paraliżu decyzyjnego. 

---

## Zapraszam na seans

<img width="1201" height="456" alt="image" src="https://github.com/user-attachments/assets/0a4f9825-510f-49a2-bfc0-13593257e485" />


## Wybierz filtry jak profesjonalny kinoman

<img width="1136" height="374" alt="image" src="https://github.com/user-attachments/assets/edbf26c3-484c-4f7f-a586-8ab0da18f838" />


Nastrój, dekada, długość. Trzy suwaki decyzyjności, żebyś mogła udawać, że to Ty wybierasz, a nie ślepy los.

## …i kliknij „Losuj”

<img width="1169" height="480" alt="image" src="https://github.com/user-attachments/assets/1b5fda2e-a4c7-4ea6-b336-37fc9cede0f5" />

Losuj swoje filmowe przeznaczenie, patrz jak tytuły migają, aż wyląduje TEN jeden. Dla większej świadomości, jak przystało na konesera kina, dostępne są także takie informacje jak: rok, reżyser, czas trwania, podsumowanie fabuły, albo słynny cytat.

---

## Podsumowanie

- **130 filmów** - od kina przedwojennego. Wszystko, co powinno się w końcu obejrzeć, ale obejrzysz dopiero teraz, bo apka Ci kazała.
- **Losowanie bez powtórek** - dopóki nie przejdzie przez całą pulę pasującą do filtrów. Apka pamięta, co już wylosowałaś.
- **Wygodny Google link** - dla leniwych.
- **Baza w Excelu, nie w kodzie** - no niestety, API zawiodło.

## Dla dociekliwych

### Uruchomienie lokalnie

```bash
pip install -r requirements.txt
streamlit run app.py
```

### Publikacja na Streamlit Community Cloud

1. Wrzuć wszystkie pliki na GitHuba, z zachowaniem `.streamlit/`.
2. [share.streamlit.io](https://share.streamlit.io) → zaloguj się kontem GitHub.
3. **Create app → Deploy a public app from GitHub**.
4. Repozytorium, branch `main`, plik główny `app.py`.
5. **Deploy** i czekaj minutę-dwie.

Każdy kolejny push na `main` przebudowuje appkę samodzielnie.

---

*Made with 🎬, Streamlit i lekką obsesją na punkcie polskiego kina.*
