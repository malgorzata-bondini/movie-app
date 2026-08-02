"""Stałe listy filtrów. Sama baza filmów mieszka teraz w filmy.xlsx —
wczytuje ją funkcja load_films() poniżej, nie ten plik."""

import pandas as pd
import streamlit as st

MOODS = [
    ("smiech", "Śmiech"),
    ("prl", "PRL"),
    ("wojna", "Wojna"),
    ("egz", "Egzystencjalne"),
    ("krym", "Kryminał"),
    ("kostium", "Kostium"),
    ("obycz", "Obyczajowe"),
    ("surreal", "Kino osobne"),
]

DECADES = [
    ("pre", "przed 1950"),
    ("50", "lata 50."),
    ("60", "lata 60."),
    ("70", "lata 70."),
    ("80", "lata 80."),
    ("90", "lata 90."),
    ("00", "XXI wiek"),
]

LENGTHS = [
    ("s", "do 90 min"),
    ("m", "90–120 min"),
    ("l", "ponad 120 min"),
]


MOOD_KEY_BY_LABEL = {label: key for key, label in MOODS}
REQUIRED_COLS = ["Tytuł", "Reżyser", "Rok", "Czas (min)", "Nastroje", "Zdanie"]


@st.cache_data(show_spinner=False)
def load_films(path: str = "filmy.xlsx"):
    """Wczytuje kartotekę z arkusza 'Filmy' w pliku Excel i zamienia ją
    na listę słowników w formacie, którego oczekuje reszta aplikacji.
    Zwraca (filmy, ostrzeżenia) — ostrzeżenia to lista czytelnych
    komunikatów o wierszach pominiętych lub nierozpoznanych nastrojach."""
    df = pd.read_excel(path, sheet_name="Filmy")
    df.columns = [str(c).strip() for c in df.columns]

    missing_cols = [c for c in REQUIRED_COLS if c not in df.columns]
    if missing_cols:
        return [], [f"W arkuszu brakuje kolumn: {', '.join(missing_cols)}."]

    films = []
    warnings = []
    for i, row in df.iterrows():
        excel_row = i + 2  # +1 za nagłówek, +1 bo pandas liczy od 0
        title = str(row["Tytuł"]).strip() if pd.notna(row["Tytuł"]) else ""
        if not title:
            continue  # pusty wiersz na dole arkusza — pomijamy bez ostrzeżenia

        try:
            year = int(row["Rok"])
            minutes = int(row["Czas (min)"])
        except (ValueError, TypeError):
            warnings.append(f"Wiersz {excel_row} ({title}): Rok i Czas (min) muszą być liczbami — pominięto.")
            continue

        mood_cell = str(row["Nastroje"]).strip() if pd.notna(row["Nastroje"]) else ""
        moods = []
        for label in mood_cell.split(","):
            label = label.strip()
            if not label:
                continue
            key = MOOD_KEY_BY_LABEL.get(label)
            if key:
                moods.append(key)
            else:
                warnings.append(f"Wiersz {excel_row} ({title}): nastrój „{label}” nie jest na liście, zignorowano.")
        if not moods:
            warnings.append(f"Wiersz {excel_row} ({title}): brak rozpoznanego nastroju — pominięto.")
            continue

        quote = str(row.get("Cytat", "")).strip() if pd.notna(row.get("Cytat")) else ""
        scene = str(row.get("Scena", "")).strip() if pd.notna(row.get("Scena")) else ""
        hook = str(row["Zdanie"]).strip() if pd.notna(row["Zdanie"]) else ""
        if not quote and not scene:
            warnings.append(f"Wiersz {excel_row} ({title}): brak Cytatu i Sceny — uzupełnij choć jedno.")
            continue
        if not hook:
            warnings.append(f"Wiersz {excel_row} ({title}): brak Zdania (opisu) — uzupełnij, żeby karta miała sens.")
            continue

        film = {
            "title": title,
            "director": str(row["Reżyser"]).strip() if pd.notna(row["Reżyser"]) else "",
            "year": year,
            "minutes": minutes,
            "moods": moods,
            "hook": hook,
        }
        if quote:
            film["quote"] = quote
        else:
            film["scene"] = scene

        if "Link Filmweb" in df.columns:
            fw_link = str(row["Link Filmweb"]).strip() if pd.notna(row["Link Filmweb"]) else ""
            if fw_link:
                if fw_link.startswith("https://www.filmweb.pl/"):
                    film["filmweb_url"] = fw_link
                else:
                    warnings.append(
                        f"Wiersz {excel_row} ({title}): Link Filmweb nie zaczyna się od "
                        "https://www.filmweb.pl/ — zignorowano, użyto wyszukiwarki."
                    )
        films.append(film)

    return films, warnings
