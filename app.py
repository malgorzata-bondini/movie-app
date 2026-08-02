import random
import time
import urllib.parse

import streamlit as st

from films import DECADES, LENGTHS, MOODS, load_films

FILMS, LOAD_WARNINGS = load_films()

st.set_page_config(
    page_title="Kartoteka polska klasyka",
    page_icon="🎞",
    layout="centered",
)

STYLE = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;1,9..144,400&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&display=swap');

:root{
  --paper:#EFEDE4;
  --card:#F8F6F0;
  --ink:#17150F;
  --ink-soft:#4A463C;
  --muted:#8B8677;
  --rule:#D8D3C4;
  --accent:#A6231A;
  color-scheme: light only;
}
html{color-scheme:light only}
html, body,
[data-testid="stApp"],
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
[data-testid="stHeader"],
[data-testid="stBottomBlockContainer"],
[data-testid="stSidebar"]{
  background:var(--paper) !important;
  color:var(--ink) !important;
}
.block-container{max-width:900px;padding-top:3rem;padding-bottom:5rem}
html, body, [class*="st-"]{font-family:"IBM Plex Sans",system-ui,sans-serif}
p, span, div, label{color:var(--ink)}

.kb-eyebrow{
  font-family:"IBM Plex Mono",monospace;font-size:.72rem;letter-spacing:.18em;
  text-transform:uppercase;color:var(--accent);margin:0 0 16px
}
.kb-title{
  font-family:"Fraunces",Georgia,serif;font-weight:400;
  font-size:clamp(2.4rem,6.5vw,4rem);line-height:1.03;letter-spacing:-.02em;
  color:var(--ink);margin:0 0 18px
}
.kb-title em{font-style:italic;color:var(--ink-soft)}
.kb-lede{max-width:48ch;color:var(--ink-soft);margin:0 0 30px;font-size:1rem;line-height:1.55}
.kb-strip{
  height:14px;margin:0 0 34px;background-color:var(--ink);
  background-image:repeating-linear-gradient(to right,transparent 0 7px,var(--paper) 7px 15px);
}
.kb-label{
  font-family:"IBM Plex Mono",monospace;font-size:.7rem;letter-spacing:.16em;
  text-transform:uppercase;color:var(--muted);margin:14px 0 2px
}
.kb-count{font-family:"IBM Plex Mono",monospace;font-size:.78rem;color:var(--muted);margin:12px 0 0}

.kb-frame{
  position:relative;background:var(--card);margin:26px 0 8px;
  border-top:1px solid var(--rule);border-bottom:1px solid var(--rule);
  padding:36px 54px;min-height:200px;overflow:hidden;
}
.kb-frame::before,.kb-frame::after{
  content:"";position:absolute;top:0;bottom:0;width:22px;
  background-color:var(--ink);
  background-image:repeating-linear-gradient(to bottom,transparent 0 9px,var(--card) 9px 21px);
}
.kb-frame::before{left:0}
.kb-frame::after{right:0}
.kb-meta{
  font-family:"IBM Plex Mono",monospace;font-size:.74rem;letter-spacing:.14em;
  text-transform:uppercase;color:var(--accent);margin:0 0 12px
}
.kb-film{
  font-family:"Fraunces",Georgia,serif;font-weight:600;color:var(--ink);
  font-size:clamp(1.6rem,4.2vw,2.6rem);line-height:1.08;letter-spacing:-.015em;margin:0 0 14px
}
.kb-spin .kb-film{color:var(--ink-soft);filter:blur(.4px)}
.kb-block{
  display:block;font-family:"IBM Plex Mono",monospace;font-size:.66rem;
  letter-spacing:.16em;text-transform:uppercase;color:var(--muted);
  margin:0 0 7px;font-style:normal
}
.kb-quote{
  margin:0 0 18px;padding:0 0 0 18px;border-left:2px solid var(--accent);
  font-family:"Fraunces",Georgia,serif;font-style:italic;color:var(--ink);
  font-size:clamp(1.1rem,2.5vw,1.45rem);line-height:1.35;max-width:34ch
}
.kb-scene{margin:0 0 18px;max-width:50ch;color:var(--ink-soft)}
.kb-hook{max-width:52ch;margin:0 0 20px;color:var(--ink-soft);font-size:.94rem}
.kb-tags{margin:0 0 22px}
.kb-tag{
  display:inline-block;font-family:"IBM Plex Mono",monospace;font-size:.68rem;
  letter-spacing:.1em;text-transform:uppercase;color:var(--muted);
  border:1px solid var(--rule);padding:4px 9px;border-radius:2px;margin:0 6px 6px 0
}
div[data-testid="stMarkdownContainer"] .kb-links a,
.kb-links a{
  color:var(--ink) !important;font-weight:500;font-size:.92rem;text-decoration:none !important;
  border-bottom:1px solid var(--accent);padding-bottom:2px;margin-right:20px
}
div[data-testid="stMarkdownContainer"] .kb-links a:hover,
.kb-links a:hover{color:var(--accent) !important}
.kb-empty{color:var(--muted);font-family:"IBM Plex Mono",monospace;font-size:.85rem;margin:0}

div[data-testid="stButton"] button{
  border-radius:2px;font-weight:600;letter-spacing:.01em;
  border:1px solid var(--rule);color:var(--ink-soft);background:transparent
}
div[data-testid="stButton"] button:hover{border-color:var(--ink-soft);color:var(--ink);background:transparent}
div[data-testid="stButton"] button[kind="primary"]{
  background:var(--accent);border-color:var(--accent);padding:.6rem 1.6rem
}
div[data-testid="stButton"] button[kind="primary"],
div[data-testid="stButton"] button[kind="primary"] p,
div[data-testid="stButton"] button[kind="primary"] div,
div[data-testid="stButton"] button[kind="primary"] span{
  color:#FBF8F2 !important;font-weight:700 !important
}
div[data-testid="stButton"] button[kind="primary"]:hover{background:#8E1D15;border-color:#8E1D15}
div[data-testid="stButton"] button[kind="primary"]:hover,
div[data-testid="stButton"] button[kind="primary"]:hover p,
div[data-testid="stButton"] button[kind="primary"]:hover div,
div[data-testid="stButton"] button[kind="primary"]:hover span{color:#FBF8F2 !important}
div[data-baseweb="tag"], span[data-baseweb="tag"]{border-radius:999px}
</style>
"""

st.markdown(STYLE, unsafe_allow_html=True)

MOOD_BY_LABEL = {label: key for key, label in MOODS}
MOOD_BY_KEY = {key: label for key, label in MOODS}
DECADE_BY_LABEL = {label: key for key, label in DECADES}
LENGTH_BY_LABEL = {label: key for key, label in LENGTHS}


def decade_key(film):
    if film["year"] < 1950:
        return "pre"
    if film["year"] >= 2000:
        return "00"
    return str(film["year"] // 10 * 10)[-2:]


def length_key(film):
    if film["minutes"] < 90:
        return "s"
    if film["minutes"] <= 120:
        return "m"
    return "l"


def time_text(minutes):
    hours, rest = divmod(minutes, 60)
    if not hours:
        return f"{minutes} min"
    return f"{hours} godz {rest} min" if rest else f"{hours} godz"


def film_id(film):
    return f"{film['title']}|{film['year']}"


def matches(film, moods, decades, lengths):
    if moods and not any(m in moods for m in film["moods"]):
        return False
    if decades and decade_key(film) not in decades:
        return False
    if lengths and length_key(film) not in lengths:
        return False
    return True


def spin_html(title):
    return (
        '<div class="kb-frame kb-spin">'
        '<p class="kb-meta">Kinematograficzne przeznaczenie</p>'
        f'<p class="kb-film">{title}</p>'
        '<p class="kb-hook">…</p>'
        "</div>"
    )


def card_html(film):
    if film.get("filmweb_url"):
        link = film["filmweb_url"]
    else:
        query = urllib.parse.quote_plus(f"{film['title']} {film['year']}")
        link = f"https://www.google.com/search?q={query}"
    link_label = "Przejdźmy do konkretów"
    if film.get("quote"):
        line = (
            '<blockquote class="kb-quote">'
            '<span class="kb-block">Sławny cytat</span>'
            f'„{film["quote"]}”</blockquote>'
        )
    else:
        line = (
            '<p class="kb-scene">'
            '<span class="kb-block">Scena, którą się pamięta</span>'
            f'{film["scene"]}</p>'
        )
    tags = "".join(f'<span class="kb-tag">{MOOD_BY_KEY[m]}</span>' for m in film["moods"])
    return (
        '<div class="kb-frame">'
        f'<p class="kb-meta">{film["year"]}&nbsp;&nbsp;&nbsp;{time_text(film["minutes"])}&nbsp;&nbsp;&nbsp;reż. {film["director"]}</p>'
        f'<p class="kb-film">{film["title"]}</p>'
        f"{line}"
        f'<p class="kb-hook">{film["hook"]}</p>'
        f'<div class="kb-tags">{tags}</div>'
        '<div class="kb-links">'
        f'<a href="{link}" target="_blank" rel="noopener">{link_label}</a>'
        "</div></div>"
    )


for key, default in (("pick", None), ("seen", set()), ("spin", False)):
    if key not in st.session_state:
        st.session_state[key] = default


def draw(pool):
    fresh = [f for f in pool if film_id(f) not in st.session_state.seen]
    if not fresh:
        st.session_state.seen = set()
        fresh = list(pool)
    current = st.session_state.pick
    if current and len(fresh) > 1:
        fresh = [f for f in fresh if film_id(f) != film_id(current)]
    pick = random.choice(fresh)
    st.session_state.pick = pick
    st.session_state.seen.add(film_id(pick))
    st.session_state.spin = True


def reset_filters():
    # Uruchamiane jako on_click: wykonuje się PRZED ponownym narysowaniem
    # widżetów st.pills, więc wolno tu bezpiecznie nadpisać ich stan.
    st.session_state.f_mood = []
    st.session_state.f_dec = []
    st.session_state.f_len = []


st.markdown(f'<p class="kb-eyebrow">Kartoteka&nbsp;&nbsp;&nbsp;{len(FILMS)} tytułów</p>', unsafe_allow_html=True)
st.markdown('<h1 class="kb-title">Polska klasyka<br><em>na dziś wieczór</em></h1>', unsafe_allow_html=True)
st.markdown(
    '<p class="kb-lede">Masz ochotę na polskie kino, ale nie wiesz co wybrać? Ustaw nastrój, '
    "dekadę i długość filmu, a resztę zostaw losowi i odkryj swoje filmowe przeznaczenie.</p>",
    unsafe_allow_html=True,
)
st.markdown('<div class="kb-strip"></div>', unsafe_allow_html=True)

if LOAD_WARNINGS:
    with st.expander(f"⚠ {len(LOAD_WARNINGS)} wiersz(y) w filmy.xlsx wymaga poprawki", expanded=False):
        for w in LOAD_WARNINGS:
            st.write("• " + w)

st.markdown('<p class="kb-label">Rodzaj</p>', unsafe_allow_html=True)
mood_labels = st.pills(
    "Rodzaj",
    [label for _, label in MOODS],
    selection_mode="multi",
    key="f_mood",
    label_visibility="collapsed",
)
st.markdown('<p class="kb-label">Dekada</p>', unsafe_allow_html=True)
decade_labels = st.pills(
    "Dekada",
    [label for _, label in DECADES],
    selection_mode="multi",
    key="f_dec",
    label_visibility="collapsed",
)
st.markdown('<p class="kb-label">Długość</p>', unsafe_allow_html=True)
length_labels = st.pills(
    "Długość",
    [label for _, label in LENGTHS],
    selection_mode="multi",
    key="f_len",
    label_visibility="collapsed",
)

moods = {MOOD_BY_LABEL[x] for x in mood_labels}
decades = {DECADE_BY_LABEL[x] for x in decade_labels}
lengths = {LENGTH_BY_LABEL[x] for x in length_labels}
pool = [f for f in FILMS if matches(f, moods, decades, lengths)]

st.write("")
left, right, _ = st.columns([2, 2, 3])
with left:
    if st.button("Losuj", type="primary", use_container_width=True, disabled=not pool):
        draw(pool)
        st.rerun()
with right:
    st.button("Wyczyść filtry", use_container_width=True, on_click=reset_filters)

if pool:
    remaining = sum(1 for f in pool if film_id(f) not in st.session_state.seen)
    filtered = len(pool) < len(FILMS)
    if remaining < len(pool):
        extra = f" ({len(FILMS)} ogółem)" if filtered else ""
        st.markdown(
            f'<p class="kb-count">{remaining} jeszcze do wylosowania z {len(pool)} w puli{extra}</p>',
            unsafe_allow_html=True,
        )
    elif filtered:
        st.markdown(f'<p class="kb-count">{len(pool)} z {len(FILMS)} tytułów w puli</p>', unsafe_allow_html=True)
    else:
        st.markdown(f'<p class="kb-count">{len(pool)} tytułów w puli</p>', unsafe_allow_html=True)
else:
    st.markdown('<p class="kb-count">brak dopasowań, zdejmij jeden filtr</p>', unsafe_allow_html=True)

slot = st.empty()
pick = st.session_state.pick

if pick and matches(pick, moods, decades, lengths):
    if st.session_state.spin and len(pool) > 1:
        st.session_state.spin = False
        delay = 0.05
        while delay < 0.22:
            slot.markdown(spin_html(random.choice(pool)["title"]), unsafe_allow_html=True)
            time.sleep(delay)
            delay *= 1.18
    slot.markdown(card_html(pick), unsafe_allow_html=True)
    if st.button("nie to, kręć dalej", disabled=not pool):
        draw(pool)
        st.rerun()
elif pool:
    slot.markdown(
        '<div class="kb-frame"><p class="kb-empty">Naciśnij „Losuj”, '
        "a karta zapełni się tytułem.</p></div>",
        unsafe_allow_html=True,
    )
else:
    slot.markdown(
        '<div class="kb-frame"><p class="kb-empty">Żaden tytuł nie pasuje do tych filtrów.</p></div>',
        unsafe_allow_html=True,
    )
