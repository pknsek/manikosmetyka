# Manikosmetyka — strona salonu

Statyczna strona salonu kosmetycznego Manikosmetyka (Czerwionka-Leszczyny).

- **Aktualna wersja (v2)** — w katalogu głównym. Styl inspirowany ROE Medical Aesthetics, KW Beauty i Nirelle: pełnoekranowe zdjęcia, stonowane beże i espresso, kwadratowe przyciski, lista zabiegów w formie akordeonu.
- **Poprzednia wersja (v1)** — w katalogu `v1/`.

## Struktura
- `index.html` i podstrony (`depilacja-laserowa`, `zabiegi-na-twarz`, `vivace-rf`, `oferta`, `o-nas`, `bony-podarunkowe`, `kontakt`)
- `style.css` — cały wygląd (kolory i fonty jako zmienne na górze pliku)
- `main.js` — menu mobilne, pasek „Umów wizytę” na telefonie, akordeon, konfigurator bonu
- `fonts/` + `fonts.css` — fonty Hanken Grotesk, Jost i Newsreader hostowane lokalnie
- `img/` — zdjęcia (tymczasowe, do podmiany na zdjęcia salonu)
- `generator.py` — skrypt, który generuje wszystkie strony HTML (wspólne menu i stopka). Po zmianie treści: `python3 generator.py .`

Teksty w nawiasach kwadratowych `[...]` to miejsca do uzupełnienia przez salon.
