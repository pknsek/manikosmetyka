# CLAUDE.md — strona Manikosmetyka

Kontekst projektu dla Claude (i dla każdego, kto przejmie pracę). Czytaj przed zmianami.

## O projekcie
- Strona salonu kosmetycznego **Manikosmetyka** (Instagram: @manikosmetyka), właścicielka **Aneta Huk**, ul. Ligonia 8, 44-238 Czerwionka-Leszczyny.
- Robi ją **Patryk Konsek** (koleżeński projekt). Patryk sam wprowadza zmiany i ogląda stronę na GitHub Pages, nie na localhoście.
- Repo: `pknsek/manikosmetyka` (branch `main`) → https://pknsek.github.io/manikosmetyka/ (Pages: deploy from branch main / root, ~1 min po pushu).
- Salon ma domenę, ale na razie brak do niej dostępu.
- Brak deadline'u — jakość ważniejsza niż tempo. **Wygląd na telefonie jest tak samo ważny jak na komputerze.**

## Ustalenia (decyzje Patryka)
- Struktura: strona główna (landing) + podstrony.
- Przyciski „Umów wizytę” prowadzą do **Booksy** (docelowo Booksy zostanie usunięte):
  `https://booksy.com/pl-pl/106175_manikosmetyka_salon-kosmetyczny_12856_czerwionka-leszczyny`
- **Bez cen** na stronie (ceny są płynne).
- Nacisk na: **depilację laserową (Primelase), zabiegi na twarz, Vivace RF**. Paznokcie nie są w centrum.
- Zespół: **Aneta Huk (właścicielka)** i **Kamila** (nazwisko do uzupełnienia); później mogą dojść kolejne osoby.
- **Nie zbieramy maili** (brak newslettera / formularzy zapisu).
- **Bony podarunkowe** — w przyszłości zakup online; na razie konfigurator + „Kup online — wkrótce”.
- Zdjęcia są **prawdziwe**, z Google Drive salonu (sesja salonu, zabiegów, Aneta i Kamila). Oryginały zostają na Drive, w repo tylko wersje max 1600 px. Hero strony głównej: Aneta (desktop wersja pozioma, telefon pion).
- Zespół: Aneta (`aneta.jpg` — uśmiech, strona główna; `aneta-o-nas.jpg` — O nas), Kamila (`kamila.jpg`).
- Dane kontaktowe: tel. +48 511 483 630, e-mail hukaneta@gmail.com, pon–pt 8:00–20:00, FB: facebook.com/ManiKosmetyka.

## Historia designu (żeby nie wracać do odrzuconych kierunków)
- v1 (krem/bordo/złoto, Cormorant + Jost, łuki) — zaakceptowana jako baza, teraz w `v1/`.
- Odrzucone: wersje „modowe/editorial” (za odważne, złe kolory), wersja pudrowo-różowa, nowe logo z Canvy. Klientka chce czegoś **bezpiecznego, stonowanego** — w tonach z jej Instagrama.
- **v2 (aktualna, katalog główny)** — inspiracja: roemedicalaesthetics.com, kwbeauty.pl, nirellecosmetics.com. Patryk: „na tej bazie będziemy pracować”.

## Design system v2 (`style.css`, zmienne w `:root`)
- Kolory (dopasowane do wnętrza salonu: jasne szarości, ecru, przygaszony róż): `--cream #F5F1EE` (tło), `--paper #FBF9F7`, `--stone #ECE2DD`, `--taupe #BBA79F`, `--taupe-ink #7F6962`, `--espresso #2E2826` (ciemne sekcje, stopka), `--mocha #5A4540` (przyciski), `--ink #2A2422`, `--muted #6F625E`. Hero strony głównej ma szare tło dopasowane do zdjęć Anety: `#C8CBCE` (desktop), `#E3E4E6` (telefon).
- Fonty (hostowane lokalnie w `fonts/`, `fonts.css`): **Hanken Grotesk** 300 — nagłówki; **Jost** — etykiety/nawigacja, WIELKIE LITERY z szerokim rozstrzeleniem; **Newsreader** 300 — leady i cytaty.
- Przyciski kwadratowe (bez zaokrągleń), uppercase, tracking .24em. Easing `cubic-bezier(.23,1,.32,1)`.
- Wzorce: pełnoekranowe hero ze zdjęciem; przewijany pasek (marquee); ciemna sekcja-kolaż; karty specjalizacji; akordeon zabiegów (na desktopie zmienia zdjęcie obok); sekcja „opinie klientek” na przyciemnionym zdjęciu; pasek Instagrama; duży napis MANIKOSMETYKA w stopce.
- Zasady stylu: bez numeracji 01/02, bez kursywnych akcentów w nagłówkach, bez złota. Pojedyncze małe etykiety nad nagłówkami są OK (jak na ROE).
- Mobile: burger → menu pełnoekranowe; ikona telefonu w nagłówku; stały dolny pasek „Umów wizytę” + telefon (pojawia się po przewinięciu); przyciski na pełną szerokość. Hero strony głównej na telefonach/tabletach/wąskich oknach (≤900px lub proporcja ≤1:1) układa się pionowo: zdjęcie u góry, tekst pod spodem.

## Struktura plików
- `index.html`, `depilacja-laserowa.html`, `zabiegi-na-twarz.html`, `vivace-rf.html`, `oferta.html`, `o-nas.html`, `bony-podarunkowe.html`, `kontakt.html` — **generowane**, nie edytuj ręcznie.
- `generator.py` — źródło wszystkich stron (wspólny `head`, `header`, `footer`, `page_hero`, `cta`, `faq` + funkcja na każdą stronę). Treści i menu zmienia się tutaj.
- `style.css` — cały wygląd. `main.js` — nagłówek przy przewijaniu, menu mobilne, pasek rezerwacji, reveal, podgląd zdjęć w akordeonie, konfigurator bonu.
- `img/` — zdjęcia (JPG, max 1600 px), nazwy opisowe (`laser-*`, `twarz-*`, `wnetrze-*` itd.). `hero-wide.jpg` (2400×1250, desktop) i `hero-m.jpg` (1000×1156, mobile) to hero strony głównej. `vivace-przed/po.jpg` to prawdziwy efekt klientki wycięty z kolażu (bez znaku wodnego) i **nałożony na siebie** (zdjęcie „przed” obrócone ~7° i przesunięte, żeby usta, fałd i żuchwa się pokrywały) — używane w suwaku przed/po (`.ba`, `data-ba` w `main.js`) na stronie Vivace. Nowe pary do suwaka muszą być tak samo wyrównane i mieć identyczny kadr.
- `v1/` — poprzednia wersja (zostawiona do porównania).
- `.nojekyll` — wymagane dla Pages.

## Jak wprowadzać zmiany
1. Edytuj `generator.py` (treści) i/lub `style.css` / `main.js`.
2. `python3 generator.py .` — przegeneruj strony.
3. QA (Playwright, jest w środowisku): zrzuty pełnych stron w 1440×900 i 390×844 (`isMobile`), sprawdzenie, że `scrollWidth == clientWidth` (brak poziomego scrolla), test menu, akordeonu i konfiguratora bonu. Warto sprawdzić też ~800 px i 1024×768.
4. Commit i push na `main`. Autor commitów: `-c user.name="Patryk Konsek" -c user.email="patrykkonsek@gmail.com"`; na końcu wiadomości linie atrybucji wymagane przez sesję.
5. Status deployu: `gh api repos/pknsek/manikosmetyka/actions/runs --jq '.workflow_runs[0].status'`.

## Ograniczenia środowiska (Claude)
- Z kontenera nie działa większość zewnętrznych hostów (unsplash, pexels, CDN-y obrazków, Google Fonts) — zdjęcia brane z repozytoriów na GitHubie, fonty z npm (`@fontsource/*`).
- `gh repo create` i API Pages są blokowane — repo i Pages ustawia Patryk.
- Strony do inspiracji ogląda się wbudowaną przeglądarką Patryka (emulacja 1440×900 i 390×844) albo Firecrawlem (markdown + branding).

## Do uzupełnienia przez salon (w treści oznaczone `[...]`)
- NIP, godziny w sobotę, info o parkingu.
- Pełna lista partii do depilacji laserowej.
- Opisy: PDRN, masaż Kobido, Glass skin; odpowiedzi w FAQ (ból przy laserze, przygotowanie, Vivace — seria/efekty/regeneracja).
- Opis Anety, nazwisko i specjalizacja Kamili, liczba lat doświadczenia.
- Ważność i zasady bonów, kwoty bonów.
- Dłuższa prawdziwa opinia klientki (np. o laserze/Vivace).
- Zdjęcia samego zabiegu Vivace RF (urządzenie, głowica) — na razie brak, na stronie Vivace są zdjęcia ogólne zabiegów na twarz. Brak zdjęć do makijażu permanentnego, stóp i przekłuwania uszu.

## Pomysły na później
- Zakup bonów online (płatności).
- Osadzona mapa Google na stronie kontaktu.
- Podpięcie własnej domeny salonu do GitHub Pages.
- Rezygnacja z Booksy → własny system rezerwacji / formularz.
- Polityka prywatności (link w stopce jest pusty).
