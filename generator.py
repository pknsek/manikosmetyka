#!/usr/bin/env python3
"""Generator statycznej strony Manikosmetyka v2."""
import os, sys

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
BOOKSY = 'https://booksy.com/pl-pl/106175_manikosmetyka_salon-kosmetyczny_12856_czerwionka-leszczyny'
TEL = '+48511483630'
TEL_H = '+48 511 483 630'
IG = 'https://www.instagram.com/manikosmetyka/'
FB = 'https://www.facebook.com/ManiKosmetyka/'
MAPS = 'https://www.google.com/maps/search/?api=1&amp;query=Ligonia+8+Czerwionka-Leszczyny'
EXT = 'target="_blank" rel="noopener"'

PHONE_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg>'

NAV_L = [('depilacja', 'depilacja-laserowa.html', 'Depilacja laserowa'),
         ('twarz', 'zabiegi-na-twarz.html', 'Zabiegi na twarz'),
         ('rf', 'radiofrekwencja-mikroiglowa.html', 'Radiofrekwencja')]
NAV_R = [('oferta', 'oferta.html', 'Oferta'),
         ('onas', 'o-nas.html', 'O nas'),
         ('szkolenia', 'szkolenia.html', 'Szkolenia'),
         ('bony', 'bony-podarunkowe.html', 'Bony'),
         ('kontakt', 'kontakt.html', 'Kontakt')]


def links(items, active):
    return ''.join(f'<a href="{h}"{" aria-current=\"page\"" if k == active else ""}>{t}</a>' for k, h, t in items)


def head(title, desc):
    return f'''<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#F8F4EE">
<link rel="preload" href="fonts/hanken-grotesk-latin-300-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="fonts.css">
<link rel="stylesheet" href="style.css">
</head>
<body>
<a class="skip" href="#tresc">Przejdź do treści</a>
'''


def header(active):
    return f'''<header class="header">
  <div class="wrap header-in">
    <nav class="nav-l" aria-label="Zabiegi">{links(NAV_L, active)}</nav>
    <a class="call" href="tel:{TEL}" aria-label="Zadzwoń: {TEL_H}">{PHONE_SVG}</a>
    <a class="logo" href="index.html" aria-label="Manikosmetyka — strona główna"><b>MANIKOSMETYKA</b><i>salon kosmetyczny</i></a>
    <nav class="nav-r" aria-label="Salon">{links(NAV_R, active)}<a class="btn btn-dark" href="{BOOKSY}" {EXT}>Umów wizytę</a></nav>
    <button class="burger" type="button" aria-label="Otwórz menu" aria-expanded="false" aria-controls="menu"><span></span><span></span></button>
  </div>
</header>
<div class="menu" id="menu" aria-hidden="true">
  <nav aria-label="Menu">{links([('home', 'index.html', 'Strona główna')] + NAV_L + NAV_R, active)}</nav>
  <div class="menu-foot">
    <a class="btn btn-dark" href="{BOOKSY}" {EXT}>Umów wizytę</a>
    <a class="btn btn-line" href="tel:{TEL}">Zadzwoń · {TEL_H}</a>
    <p>ul. Ligonia 8, Czerwionka-Leszczyny · pon–pt 8:00–20:00</p>
  </div>
</div>
<main id="tresc">
'''


def footer():
    return f'''</main>
<footer class="footer">
  <div class="wrap">
    <div class="footer-top">
      <div>
        <a class="logo" href="index.html"><b>MANIKOSMETYKA</b><i>salon kosmetyczny</i></a>
        <p>Depilacja laserowa, zabiegi na twarz i radiofrekwencja mikroigłowa w Czerwionce-Leszczynach. Zaczynamy od rozmowy.</p>
      </div>
      <div>
        <h4>Zabiegi</h4>
        <ul>
          <li><a href="depilacja-laserowa.html">Depilacja laserowa</a></li>
          <li><a href="zabiegi-na-twarz.html">Zabiegi na twarz</a></li>
          <li><a href="radiofrekwencja-mikroiglowa.html">Radiofrekwencja mikroigłowa</a></li>
          <li><a href="oferta.html">Pełna oferta</a></li>
        </ul>
      </div>
      <div>
        <h4>Salon</h4>
        <ul>
          <li><a href="o-nas.html">O nas</a></li>
          <li><a href="szkolenia.html">Szkolenia</a></li>
          <li><a href="bony-podarunkowe.html">Bony podarunkowe</a></li>
          <li><a href="kontakt.html">Kontakt i dojazd</a></li>
          <li><a href="{BOOKSY}" {EXT}>Rezerwacja online</a></li>
        </ul>
      </div>
      <div>
        <h4>Kontakt</h4>
        <ul>
          <li><a href="{MAPS}" {EXT}>ul. Ligonia 8<br>44-238 Czerwionka-Leszczyny</a></li>
          <li><a href="tel:{TEL}">{TEL_H}</a></li>
          <li><a href="mailto:hukaneta@gmail.com">hukaneta@gmail.com</a></li>
          <li>Pon–Pt 8:00–20:00</li>
        </ul>
      </div>
    </div>
    <div class="footer-big" aria-hidden="true"><span>MANIKOSMETYKA</span></div>
    <div class="footer-bottom">
      <span>© 2026 Manikosmetyka · Aneta Huk · NIP 6423090410</span>
      <div><a href="{IG}" {EXT}>Instagram</a><a href="{FB}" {EXT}>Facebook</a><a href="#">Polityka prywatności</a></div>
    </div>
  </div>
</footer>
<div class="bookbar">
  <a class="btn btn-dark" href="{BOOKSY}" {EXT}>Umów wizytę</a>
  <a class="btn btn-line" href="tel:{TEL}" aria-label="Zadzwoń">{PHONE_SVG}</a>
</div>
<script src="main.js"></script>
</body>
</html>
'''


def page_hero(crumb, title, lead, img, alt, pos='50% 40%', pos_m=None, btns=None):
    pm = f' --pos-m: {pos_m};' if pos_m else ''
    b = btns if btns is not None else f'<a class="btn btn-light" href="{BOOKSY}" {EXT}>Umów wizytę</a><a class="btn btn-ghost" href="{BOOKSY}" {EXT}>Bezpłatna konsultacja</a>'
    return f'''<section class="hero page-hero on-photo">
  <img class="hero-bg" src="img/{img}.jpg" alt="{alt}" style="--pos: {pos};{pm}" fetchpriority="high">
  <div class="wrap hero-in">
    <p class="crumbs"><a href="index.html">Strona główna</a> &nbsp;/&nbsp; {crumb}</p>
    <h1 class="h1" style="margin-top:22px">{title}</h1>
    <p class="lead">{lead}</p>
    <div class="btns">{b}</div>
  </div>
</section>
'''


def cta(title, lead, light=False):
    cls = 'bg-stone' if light else 'bg-dark'
    b1 = 'btn-dark' if light else 'btn-light'
    b2 = 'btn-line' if light else 'btn-ghost'
    return f'''<section class="section {cls} cta center">
  <div class="wrap rv">
    <p class="label">Zapraszamy</p>
    <h2 class="h2">{title}</h2>
    <p class="lead">{lead}</p>
    <div class="btns"><a class="btn {b1}" href="{BOOKSY}" {EXT}>Umów wizytę</a><a class="btn {b2}" href="tel:{TEL}">Zadzwoń</a></div>
  </div>
</section>
'''


def faq(title, items, label='Pytania'):
    det = ''.join(f'<details{" open" if i == 0 else ""}><summary>{q}<span class="ico" aria-hidden="true"></span></summary><div class="acc-body"><p>{a}</p></div></details>' for i, (q, a) in enumerate(items))
    return f'''<section class="section bg-paper">
  <div class="wrap acc-grid acc-faq">
    <div class="rv"><p class="label">{label}</p><h2 class="h2" style="margin-top:18px">{title}</h2></div>
    <div class="acc rv">{det}</div>
  </div>
</section>
'''


def steps(items):
    return ''.join(f'<div class="step"><h3>{t}</h3><p>{p}</p></div>' for t, p in items)


def write(name, html):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        f.write(html)


# =================================================================== HOME
SERVICES = [
    ('Depilacja laserowa', 'Laser diodowy · pakiety', 'laser-plecy', 'Depilacja laserowa pleców',
     '<p>Trwałe pozbycie się niechcianego owłosienia laserem diodowym. Pojedyncze partie i pakiety 6 zabiegów, możliwa płatność w ratach.</p>',
     'depilacja-laserowa.html'),
    ('Radiofrekwencja mikroigłowa', 'Twarz i ciało', 'twarz-mikronakluwanie', 'Skóra twarzy po zabiegu mikroigłowym',
     '<p>Mikronakłuwanie połączone z falami radiowymi: ujędrnienie, zmarszczki, blizny, rozstępy i pory — na twarz i ciało.</p>',
     'radiofrekwencja-mikroiglowa.html'),
    ('Zabiegi na twarz', 'Mezoterapia · Glass skin', 'twarz-oczyszczanie', 'Zabieg pielęgnacyjny na twarz w gabinecie',
     '<p>Zabiegi regenerujące, odmładzające i nawilżające — zawsze dobrane po konsultacji.</p><ul><li>Mezoterapia mikroigłowa</li><li>Glass skin</li></ul>',
     'zabiegi-na-twarz.html'),
    ('Zabiegi na ciało', 'Endermologia · radiofrekwencja mikroigłowa', 'cialo-cryo', 'Kosmetyk do zabiegów na ciało',
     '<p>Modelowanie i ujędrnianie sylwetki.</p><ul><li>Endermologia Primelle</li><li>Radiofrekwencja mikroigłowa na ciało</li><li>Rozstępy i blizny</li></ul>', 'oferta.html#cialo'),
    ('Medycyna estetyczna', 'Lipoliza · skóra głowy', 'twarz-maska', 'Zabieg na twarz w gabinecie',
     '<p>Zabiegi iniekcyjne wykonywane po kwalifikacji.</p><ul><li>Lipoliza iniekcyjna</li><li>Mezoterapia skóry głowy Dr Cyj Hair Filler</li></ul>', 'oferta.html#estetyczna'),
    ('Brwi i rzęsy', 'Laminacja · henna', 'brwi-produkty', 'Kosmetyki do stylizacji brwi',
     '<p>Oprawa oka, która wygląda naturalnie.</p><ul><li>Laminacja brwi</li><li>Henna pudrowa i żelowa</li><li>Henna rzęs</li><li>Regulacja woskiem</li></ul>', 'oferta.html#brwi'),
    ('Makijaż permanentny', 'Brwi metodą pudrową', 'twarz-serum', 'Kosmetolożka z serum podczas zabiegu',
     '<p>Brwi metodą pudrową z wizytą kontrolną oraz korekty wcześniejszych pigmentacji.</p>', 'oferta.html#pmu'),
    ('Wizaż i dłonie', 'Makijaż · manicure · pedicure', 'dlonie-lakiery', 'Lakiery hybrydowe w salonie',
     '<p>Makijaż okolicznościowy i ślubny z możliwością dojazdu, manicure i pedicure.</p>', 'oferta.html#wizaz'),
]


def home():
    acc = ''
    for i, (name, sub, img, alt, body, href) in enumerate(SERVICES):
        acc += f'''<details data-img="img/{img}.jpg" data-alt="{alt}"{" open" if i == 0 else ""}>
          <summary><span>{name}<small>{sub}</small></span><span class="ico" aria-hidden="true"></span></summary>
          <div class="acc-body">{body}<a class="link" href="{href}">Szczegóły <span class="arr" aria-hidden="true">→</span></a></div>
        </details>'''
    marquee_items = ['Depilacja laserowa', 'Radiofrekwencja mikroigłowa', 'Mezoterapia mikroigłowa', 'Bezpłatna konsultacja']
    mq = ''.join(f'<span>{t} ·</span>' for t in marquee_items) * 2
    html = head('Manikosmetyka — salon kosmetyczny w Czerwionce-Leszczynach',
                'Salon kosmetyczny w Czerwionce-Leszczynach: depilacja laserowa, zabiegi na twarz, radiofrekwencja mikroigłowa. Bezpłatna konsultacja.').replace('<body>', '<body class="light-top">') + header('home')
    html += f'''
<section class="hero hero-home">
  <picture>
    <source media="(max-width: 900px), (max-aspect-ratio: 1/1)" srcset="img/hero-m.jpg">
    <img class="hero-bg" src="img/hero-wide.jpg" alt="Aneta Huk, właścicielka salonu Manikosmetyka" fetchpriority="high">
  </picture>
  <div class="wrap hero-in">
    <p class="label">Salon kosmetyczny <span class="hide-m">· Czerwionka-Leszczyny</span></p>
    <h1 class="display">Naturalne piękno, bez&nbsp;pośpiechu</h1>
    <p class="lead">Depilacja laserowa, zabiegi na twarz i radiofrekwencja mikroigłowa w Czerwionce-Leszczynach. Każdy zabieg zaczynamy od bezpłatnej konsultacji.</p>
    <div class="btns"><a class="btn btn-dark" href="{BOOKSY}" {EXT}>Umów wizytę</a><a class="btn btn-line" href="#zabiegi">Poznaj zabiegi</a></div>
    <div class="hero-meta"><span>★ 5,0 na Booksy</span><span>734 opinie</span><span>Konsultacja gratis</span></div>
  </div>
</section>

<div class="marquee" aria-hidden="true"><div class="marquee-track">{mq}</div></div>

<section class="collage bg-dark">
 <div class="collage-stage">
  <div class="collage-imgs">
    <img class="collage-img c1" src="img/twarz-masaz.jpg" alt="" loading="lazy">
    <img class="collage-img c2" src="img/twarz-glowica.jpg" alt="" loading="lazy">
    <img class="collage-img c3" src="img/wnetrze-fotel.jpg" alt="" loading="lazy">
    <img class="collage-img c4" src="img/laser-okulary-tacka.jpg" alt="" loading="lazy">
  </div>
  <div class="wrap">
    <div class="collage-text rv">
      <p class="label">Jak pracujemy</p>
      <h2 class="h2">Efekty, które wyglądają naturalnie — bo&nbsp;zaczynamy od&nbsp;rozmowy</h2>
      <p class="lead">Nie sprzedajemy zabiegów na ślepo. Najpierw poznajemy Twoją skórę i oczekiwania, potem razem układamy plan.</p>
      <div class="btns"><a class="btn btn-light" href="{BOOKSY}" {EXT}>Bezpłatna konsultacja</a></div>
    </div>
  </div>
 </div>
  <div class="wrap">
    <div class="steps rv"><div class="grid-4">{steps([
        ('Konsultacja', 'Bezpłatna rozmowa w gabinecie i ocena skóry.'),
        ('Plan zabiegowy', 'Dobieramy zabieg, serię i przygotowanie skóry.'),
        ('Zabieg', 'Sprawdzony sprzęt, sterylne narzędzia, spokojna atmosfera.'),
        ('Pielęgnacja', 'Zalecenia do domu i kontrola efektów na kolejnych wizytach.')])}</div></div>
  </div>
</section>

<section class="section" id="specjalizacje">
  <div class="wrap">
    <div class="head-row rv">
      <div><p class="label">Specjalizacje</p><h2 class="h2">W tym jesteśmy najmocniejsze</h2></div>
      <a class="link" href="oferta.html">Cała oferta <span class="arr" aria-hidden="true">→</span></a>
    </div>
    <div class="grid-4 cards-4">
      <a class="card rv" href="depilacja-laserowa.html">
        <div class="card-media"><img src="img/laser-nogi.jpg" alt="Depilacja laserowa nóg" loading="lazy"></div>
        <h3 class="caps caps-lg">Depilacja laserowa</h3>
        <p>Laser diodowy — bez golenia, podrażnień i pośpiechu. Pakiety i raty.</p>
        <span class="btn btn-dark">Poznaj zabieg</span>
      </a>
      <a class="card rv" href="zabiegi-na-twarz.html">
        <div class="card-media"><img src="img/twarz-glowica-2.jpg" alt="Zabieg na twarz w gabinecie Manikosmetyka" loading="lazy"></div>
        <h3 class="caps caps-lg">Zabiegi na twarz</h3>
        <p>Oczyszczanie, peelingi, mezoterapia i pielęgnacja dobrana po konsultacji.</p>
        <span class="btn btn-dark">Poznaj zabiegi</span>
      </a>
      <a class="card rv" href="radiofrekwencja-mikroiglowa.html">
        <div class="card-media"><img src="img/twarz-maska.jpg" alt="Skóra twarzy po zabiegu mikroigłowym" loading="lazy"></div>
        <h3 class="caps caps-lg">Radiofrekwencja mikroigłowa</h3>
        <p>Ujędrnienie, zmarszczki, blizny i rozstępy — na twarz i ciało.</p>
        <span class="btn btn-dark">Poznaj zabieg</span>
      </a>
      <a class="card rv" href="oferta.html#pmu">
        <div class="card-media"><img src="img/brwi-produkty.jpg" alt="Kosmetyki do stylizacji brwi" loading="lazy"></div>
        <h3 class="caps caps-lg">Makijaż permanentny brwi</h3>
        <p>Metoda pudrowa: naturalny, delikatny efekt na 1–2 lata, z wizytą kontrolną.</p>
        <span class="btn btn-dark">Poznaj zabieg</span>
      </a>
    </div>
  </div>
</section>

<section class="section bg-stone" id="zabiegi">
  <div class="wrap acc-grid">
    <div class="acc-media"><img src="img/laser-plecy.jpg" alt="Depilacja laserowa pleców" loading="lazy"></div>
    <div>
      <div class="rv" style="margin-bottom: clamp(32px, 4vw, 56px)">
        <p class="label">Oferta</p>
        <h2 class="h2" style="margin-top:18px">Nasze zabiegi</h2>
        <p class="body" style="margin-top:20px">Ceny ustalamy indywidualnie — aktualne znajdziesz przy rezerwacji online.</p>
      </div>
      <div class="acc rv">{acc}</div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <img class="portrait rv" src="img/aneta.jpg" alt="Aneta Huk — właścicielka salonu" style="object-position: 50% 20%" loading="lazy">
    <div class="rv" style="--gap: 26px">
      <p class="label">Poznaj właścicielkę</p>
      <h2 class="h2" style="margin-top:18px">Aneta Huk</h2>
      <p class="lead" style="margin-top:26px">Manikosmetyka to miejsce, w którym piękno spotyka się z profesjonalizmem — i z czasem tylko dla Ciebie.</p>
      <p class="body" style="margin-top:20px">Z pasją i profesjonalizmem wykonuje zabiegi na twarz i ciało, dbając o każdy detal. Od ponad 20 lat zajmuje się również stylizacją paznokci i jest instruktorką NC Company. W swojej pracy stawia na jakość, precyzję i indywidualne podejście.</p>
      <div class="stats" style="margin-top:40px">
        <div class="stat"><b>5,0</b><span>ocena Booksy</span></div>
        <div class="stat"><b>734</b><span>opinie</span></div>
        <div class="stat"><b>20+</b><span>lat w stylizacji paznokci</span></div>
      </div>
      <a class="link" href="o-nas.html" style="margin-top:36px">Poznaj zespół <span class="arr" aria-hidden="true">→</span></a>
    </div>
  </div>
</section>

<section class="band section">
  <img src="img/wnetrze-kacik.jpg" alt="" loading="lazy">
  <div class="wrap notes">
    <div class="rv">
      <p class="label">Booksy · 5,0 / 734 opinie</p>
      <p class="notes-title">opinie<br>klientek</p>
    </div>
    <div class="quotes rv">
      <figure class="quote"><div class="stars" aria-label="5 na 5">★★★★★</div><blockquote>„Piękne brwi jak zawsze.”</blockquote><figcaption>Marta · laminacja brwi</figcaption></figure>
      <figure class="quote"><div class="stars" aria-label="5 na 5">★★★★★</div><blockquote>„Wszystko super!”</blockquote><figcaption>Natalia · manicure</figcaption></figure>
      <figure class="quote"><div class="stars" aria-label="5 na 5">★★★★★</div><blockquote>„Byłam na depilacji laserowej i mega polecam! Niesamowicie profesjonalne podejście, brak krępacji przy depilacji bikini, brak bólu, szybko trwał zabieg i dokładnie zostały wyjaśnione zasady pielęgnacji miejsca depilacji. Jestem bardzo zadowolona i polecam każdemu, kto się zastanawia.”</blockquote><figcaption>Agnieszka Ż. · depilacja laserowa · opinia z Google</figcaption></figure>
      <div><a class="btn btn-ghost" href="{BOOKSY}" {EXT}>Wszystkie opinie</a></div>
    </div>
  </div>
</section>

<section class="section bg-paper">
  <div class="wrap split">
    <div class="rv">
      <p class="label">Bony podarunkowe</p>
      <h2 class="h2" style="margin-top:18px">Podaruj chwilę dla siebie</h2>
      <p class="lead" style="margin-top:26px">Bon na wybrany zabieg lub dowolną kwotę — na urodziny, święta i bez okazji.</p>
      <div class="btns" style="margin-top:36px"><a class="btn btn-dark" href="bony-podarunkowe.html">Wybierz bon</a></div>
    </div>
    <div class="pair rv">
      <img class="media r-34" src="img/wnetrze-kawa.jpg" alt="Kawa z logo Manikosmetyki w strefie relaksu" loading="lazy">
      <img class="media r-34" src="img/bon-podarunkowy.jpg" alt="Bon podarunkowy Manikosmetyki w eleganckiej kopercie" loading="lazy">
    </div>
  </div>
</section>

<section class="section-sm">
  <div class="wrap">
    <div class="head-row rv" style="margin-bottom:32px">
      <h2 class="caps caps-lg">Instagram</h2>
      <a class="link" href="{IG}" {EXT}>@manikosmetyka <span class="arr" aria-hidden="true">→</span></a>
    </div>
  </div>
  <div class="ig rv">
    <a href="{IG}" {EXT} aria-label="Instagram — zdjęcie 1"><img src="img/zabieg-twarz-dlonie.jpg" alt="" loading="lazy"></a>
    <a href="{IG}" {EXT} aria-label="Instagram — zdjęcie 2"><img src="img/kwiaty-produkty.jpg" alt="" loading="lazy"></a>
    <a href="{IG}" {EXT} aria-label="Instagram — zdjęcie 3"><img src="img/laser-mezczyzna.jpg" alt="" loading="lazy"></a>
    <a href="{IG}" {EXT} aria-label="Instagram — zdjęcie 4"><img src="img/wnetrze-wazon.jpg" alt="" loading="lazy"></a>
    <a href="{IG}" {EXT} aria-label="Instagram — zdjęcie 5"><img src="img/twarz-pca.jpg" alt="" loading="lazy"></a>
    <a href="{IG}" {EXT} aria-label="Instagram — zdjęcie 6"><img src="img/kawa-magazyn.jpg" alt="" loading="lazy"></a>
  </div>
</section>

<section class="section bg-stone">
  <div class="wrap split">
    <div class="rv keep">
      <p class="label">Wizyta</p>
      <h2 class="h2" style="margin-top:18px">Do zobaczenia w salonie</h2>
      <div class="info" style="margin-top:40px">
        <div class="info-row"><span class="label">Adres</span><a href="{MAPS}" {EXT}>ul. Ligonia 8, 44-238 Czerwionka-Leszczyny</a></div>
        <div class="info-row"><span class="label">Godziny</span><p>Poniedziałek–piątek 8:00–20:00</p></div>
        <div class="info-row"><span class="label">Telefon</span><a href="tel:{TEL}">{TEL_H}</a></div>
      </div>
      <div class="btns" style="margin-top:40px"><a class="btn btn-dark" href="{BOOKSY}" {EXT}>Umów wizytę</a><a class="btn btn-line" href="kontakt.html">Jak dojechać</a></div>
    </div>
    <img class="media r-45 rv" src="img/gabinet-zabiegowy.jpg" alt="Gabinet zabiegowy Manikosmetyka" loading="lazy">
  </div>
</section>
'''
    html += footer()
    write('index.html', html)


# =================================================================== DEPILACJA
def depilacja():
    html = head('Depilacja laserowa — Manikosmetyka',
                'Depilacja laserowa w Czerwionce-Leszczynach. Pojedyncze zabiegi i pakiety, bezpłatna konsultacja.') + header('depilacja')
    html += page_hero('Depilacja laserowa', 'Depilacja laserowa',
                      'Gładka skóra przez cały sezon — bez golenia, bez podrażnień, bez pośpiechu.',
                      'laser-plecy', 'Depilacja laserowa pleców', '50% 18%')
    html += f'''
<section class="section">
  <div class="wrap">
    <div class="split" style="align-items:start">
      <div class="rv"><p class="label">Dlaczego laser</p><h2 class="h2" style="margin-top:18px">Koniec z maszynką i&nbsp;wrastającymi włoskami</h2></div>
      <p class="lead rv">Laser diodowy działa na mieszek włosowy, dlatego efekt budujesz serią zabiegów — a potem po prostu cieszysz się gładką skórą. Na konsultacji dobierzemy parametry do Twojej skóry i włosa.</p>
    </div>
    <div class="grid-4" style="margin-top: clamp(56px, 7vw, 96px)">
      <div class="feat rv"><h3 class="caps caps-md">Bez golenia</h3><p>Zapomnij o maszynce i codziennym pośpiechu.</p></div>
      <div class="feat rv"><h3 class="caps caps-md">Bez podrażnień</h3><p>Koniec z wrastającymi włoskami i zaczerwienieniem.</p></div>
      <div class="feat rv"><h3 class="caps caps-md">Na długo</h3><p>Efekt budowany serią zabiegów, a nie z dnia na dzień.</p></div>
      <div class="feat rv"><h3 class="caps caps-md">Dla niej i dla niego</h3><p>Partie kobiece i męskie, także twarz.</p></div>
    </div>
  </div>
</section>

<section class="section bg-stone">
  <div class="wrap split">
    <img class="media r-45 rv" src="img/laser-pacha.jpg" alt="Depilacja laserowa pach" loading="lazy">
    <div class="rv">
      <p class="label">Obszary zabiegowe</p>
      <h2 class="h2" style="margin-top:18px">Wybierz partię ciała</h2>
      <p class="body" style="margin-top:20px">Możesz zacząć od jednej partii albo połączyć kilka w pakiecie.</p>
      <h3 class="caps caps-md" style="margin:40px 0 16px">Kobiety</h3>
      <ul class="tags"><li>Twarz</li><li>Wąsik</li><li>Pachy</li><li>Bikini płytkie</li><li>Bikini głębokie</li><li>Uda</li><li>Łydki</li><li>Całe nogi</li><li>Przedramiona</li><li>Brzuch</li></ul>
      <h3 class="caps caps-md" style="margin:36px 0 16px">Mężczyźni</h3>
      <ul class="tags"><li>Broda</li><li>Kark</li><li>Plecy</li><li>Klatka piersiowa</li><li>Bikini męskie</li></ul>
      <p class="note" style="margin-top:24px">[Do potwierdzenia z salonem: pełna lista partii]</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="center rv" style="max-width:720px;margin:0 auto clamp(48px,6vw,80px)">
      <p class="label">Pakiety</p>
      <h2 class="h2" style="margin-top:18px">Seria to klucz do efektu</h2>
      <p class="lead" style="margin-top:24px">Oprócz pojedynczych wizyt przygotowujemy pakiety — zapytaj o aktualną promocję.</p>
    </div>
    <div class="grid-3">
      <div class="box rv"><p class="label">Na start</p><h3 class="h3">1 zabieg · 1 partia</h3><p>Idealny, jeśli chcesz spróbować.</p></div>
      <div class="box is-dark rv"><span class="tag">Najczęściej wybierany</span><h3 class="h3">6 zabiegów · 1 partia</h3><p>Możliwa płatność w ratach. Pakiet ważny 12 miesięcy.</p></div>
      <div class="box rv"><p class="label">Pakiet rozszerzony</p><h3 class="h3">6 zabiegów · 2 partie</h3><p>Najlepsza wartość przy dwóch partiach naraz.</p></div>
    </div>
    <div class="btns rv" style="justify-content:center;margin-top:48px"><a class="btn btn-dark" href="{BOOKSY}" {EXT}>Zarezerwuj termin</a></div>
  </div>
</section>

<section class="section bg-dark">
  <div class="wrap">
    <div class="rv" style="max-width:720px"><p class="label">Przebieg</p><h2 class="h2" style="margin-top:18px">Cztery kroki do gładkiej skóry</h2></div>
    <div class="steps rv" style="margin-top:56px"><div class="grid-4">{steps([
        ('Konsultacja', 'Rozmowa, ocena skóry i włosa, kwalifikacja do zabiegu.'),
        ('Przygotowanie', 'Dostaniesz jasne zalecenia, jak przygotować się do wizyty.'),
        ('Zabieg', 'Szybki zabieg laserem diodowym w komfortowych warunkach.'),
        ('Pielęgnacja', 'Zalecenia po zabiegu i plan kolejnych wizyt w serii.')])}</div></div>
  </div>
</section>
'''
    html += faq('Najczęściej pytacie', [
        ('Ile zabiegów potrzebuję?', 'To zależy od partii, rodzaju włosa i skóry. Najczęściej pracujemy w serii — dlatego pakiety obejmują 6 zabiegów. Dokładny plan ustalimy na konsultacji.'),
        ('Jak przygotować się do depilacji laserowej?', 'Najpóźniej dzień przed zabiegiem należy dokładnie ogolić maszynką obszar poddawany depilacji, najlepiej na zero. Im gładsza skóra, tym większy komfort podczas zabiegu. Skóra powinna być czysta, sucha, bez balsamów i innych kosmetyków.'),
        ('Czy depilacja laserowa boli?', 'Zabieg jest odczuwalny, ale zazwyczaj nie jest bolesny. Dzięki chłodzącej głowicy i pracy na żelu dyskomfort jest znacznie mniejszy. Odczucia są indywidualne, jednak większość osób dobrze toleruje zabieg.'),
        ('Czy mogę rozłożyć płatność na raty?', 'Tak, przy pakietach możliwa jest płatność w ratach. Zapytaj o szczegóły przy rezerwacji.'),
        ('Czy konsultacja jest płatna?', 'Nie, konsultacja w gabinecie jest bezpłatna.')])
    html += cta('Gotowa na lato bez maszynki?', 'Zarezerwuj konsultację i zacznij serię, zanim zrobi się ciepło.')
    html += footer()
    write('depilacja-laserowa.html', html)


# =================================================================== TWARZ
FACE_GROUPS = [
    ('Oczyszczanie i nawilżanie', 'Zabiegi na każdy dzień i na „reset” skóry.', [
        ('HydroRevive', 'Oczyszczanie wodorowe w 8 etapach (ok. 1 h 15 min): peeling kawitacyjny, sonoforeza z ampułką i maska.'),
        ('HydroGlow', 'Oczyszczanie wodorowe w 6 etapach (ok. 1 h): szybki blask i nawilżenie.'),
        ('HydroLux', 'Oczyszczanie wodorowe w 9 etapach (ok. 1 h 30 min) z falą radiową (RF), sonoforezą i maską.'),
        ('Oczyszczanie z peelingiem kawitacyjnym', 'Dokładne oczyszczenie skóry twarzy i delikatne złuszczenie.'),
        ('Rytuał Glass skin', 'Oczyszczanie, peeling, tonizacja, intensywne nawilżenie i filtr UV: efekt gładkiej, rozświetlonej skóry.'),
        ('Podstawowy zabieg pielęgnacyjny', 'Peeling, ampułka i maska dobrane do potrzeb skóry.'),
        ('Rytuał piękna ESTHEMAX', 'Rozbudowany rytuał pielęgnacyjny (ok. 1 h 30 min).')]),
    ('Złuszczanie i odnowa', 'Peelingi i mikrodermabrazja dla wyrównania struktury skóry.', [
        ('Mikrodermabrazja', 'Mechaniczne złuszczanie naskórka: twarz, szyja i dekolt, także z maseczką.'),
        ('Peelingi kwasowe', 'Złuszczanie kwasami dobranymi do rodzaju skóry.'),
        ('BioRePeel Cl3', 'Profesjonalny zabieg peelingujący.'),
        ('PRX-T33', 'Profesjonalny zabieg peelingujący.'),
        ('Reti Peel', 'Peeling z retinolem.'),
        ('PQ-AGE Evolution', 'Profesjonalny zabieg odmładzający.')]),
    ('Zabiegi autorskie i z retinolem', 'Bardziej wymagająca pielęgnacja, dobierana na konsultacji.', [
        ('Autorski zabieg terapeutyczny', 'Zabieg dopasowany do potrzeb Twojej skóry (ok. 1 h 30 min).'),
        ('Autorski zabieg z retinolem i mezoterapią', 'Połączenie retinolu z mezoterapią mikroigłową.'),
        ('Zabieg z retinolem i czynnikami wzrostu', 'Pielęgnacja z retinolem i czynnikami wzrostu (ok. 45 min).'),
        ('Zabieg Geneo', 'Zabieg dotleniający i odświeżający skórę.')]),
    ('PCA Skin', 'Profesjonalna pielęgnacja marki PCA Skin.', [
        ('PCA Oxygenating, stopnie I, II i III', 'Trzy stopnie intensywności zabiegu, dobierane do kondycji skóry.'),
        ('Zabieg terapeutyczny kwasami PCA', 'Pielęgnacja kwasami PCA.'),
        ('PCAskin Trądzik', 'Procedura dla cery z niedoskonałościami.'),
        ('PCAskin Cera naczynkowa', 'Delikatna procedura dla skóry wrażliwej i naczynkowej.')]),
]


def face_list():
    out = ''
    for t, d, items in FACE_GROUPS:
        li = ''.join(f'<li><span>{a}</span><small>{b}</small></li>' for a, b in items)
        out += f'<div class="cat"><div class="rv"><h3 class="h2" style="font-size:clamp(26px,2.8vw,38px)">{t}</h3><p class="body">{d}</p></div><ul class="lines rv">{li}</ul></div>'
    return out


def twarz():
    html = head('Zabiegi na twarz — Manikosmetyka',
                'Zabiegi na twarz w Czerwionce-Leszczynach: radiofrekwencja mikroigłowa, mezoterapia, oczyszczanie wodorowe, peelingi, PCA Skin.') + header('twarz')
    html += page_hero('Zabiegi na twarz', 'Skóra, która wygląda na wypoczętą',
                      'Zabiegi regenerujące, odmładzające i nawilżające — zawsze dobrane po konsultacji.',
                      'twarz-oczyszczanie', 'Zabieg pielęgnacyjny na twarz w gabinecie', '50% 68%', '55% 60%')
    mq = ''.join(f'<span>{t} ·</span>' for t in ['zmarszczki', 'utrata jędrności', 'rozszerzone pory', 'blizny', 'szara skóra', 'przesuszenie']) * 2
    html += f'''<div class="marquee" aria-label="Z czym przychodzicie najczęściej: zmarszczki, utrata jędrności, rozszerzone pory, blizny, szara skóra, przesuszenie"><div class="marquee-track" aria-hidden="true">{mq}</div></div>

<section class="section">
  <div class="wrap" style="display:grid;gap:clamp(80px,10vw,150px)">
    <article class="split">
      <img class="media r-45 rv" src="img/twarz-maska.jpg" alt="Skóra twarzy po zabiegu mikroigłowym" loading="lazy">
      <div class="rv">
        <p class="label">Specjalizacja</p>
        <h2 class="h2" style="margin-top:18px">Radiofrekwencja mikroigłowa</h2>
        <p class="body" style="margin-top:22px">Połączenie mikronakłuwania z falami radiowymi stymuluje głęboką regenerację skóry i produkcję kolagenu. Efekt to gładka, jędrna i odświeżona skóra.</p>
        <ul class="tags" style="margin-top:26px"><li>anti-aging</li><li>zmarszczki</li><li>blizny</li><li>pory</li></ul>
        <a class="link" href="radiofrekwencja-mikroiglowa.html" style="margin-top:32px">Więcej o radiofrekwencji mikroigłowej <span class="arr" aria-hidden="true">→</span></a>
      </div>
    </article>
    <article class="split">
      <div class="rv keep">
        <p class="label">Odżywienie i nawilżenie</p>
        <h2 class="h2" style="margin-top:18px">Mezoterapia mikroigłowa</h2>
        <p class="body" style="margin-top:22px">Substancje odżywcze trafiają w głąb skóry dzięki cienkim igłom urządzenia (dermapen). Skóra staje się odżywiona, nawilżona i ujędrniona. Najlepsze efekty daje seria 4–8 zabiegów co 2–3 tygodnie.</p>
        <ul class="lines" style="margin-top:28px"><li><span>Konsultacja i dobór preparatów</span></li><li><span>Oczyszczenie skóry, w razie potrzeby znieczulenie</span></li><li><span>Mikronakłucia z substancjami aktywnymi</span></li></ul>
      </div>
      <img class="media r-45 rv" src="img/twarz-mikronakluwanie.jpg" alt="Skóra po mezoterapii mikroigłowej" loading="lazy">
    </article>
  </div>
</section>

<section class="section bg-stone">
  <div class="wrap">
    <div class="head-row rv"><div><p class="label">Wszystkie zabiegi</p><h2 class="h2">Zabiegi na twarz w naszej ofercie</h2></div><a class="link" href="{BOOKSY}" {EXT}>Rezerwacja online <span class="arr" aria-hidden="true">→</span></a></div>
    {face_list()}
  </div>
</section>

<section class="section bg-dark">
  <div class="wrap">
    <div class="split" style="align-items:end">
      <div class="rv"><p class="label">Jak zaczynamy</p><h2 class="h2" style="margin-top:18px">Najpierw poznajemy Twoją skórę</h2></div>
      <p class="lead rv">Konsultacja jest bezpłatna. Ocenimy stan skóry, porozmawiamy o celu i zaproponujemy plan — od jednego zabiegu po pełną serię.</p>
    </div>
    <div class="steps rv" style="margin-top:56px"><div class="grid-4">{steps([
        ('Ocena skóry', 'Rozmowa i analiza potrzeb.'),
        ('Dobór zabiegu', 'Preparaty i technologia pod Twój cel.'),
        ('Seria', 'Plan wizyt w odpowiednich odstępach.'),
        ('Pielęgnacja domowa', 'Zalecenia, które utrwalą efekt.')])}</div></div>
  </div>
</section>
'''
    html += cta('Nie wiesz, jaki zabieg na twarz wybrać?', 'Umów się na konsultację połączoną z zabiegiem. Podczas wizyty ocenimy stan i potrzeby Twojej skóry, porozmawiamy o Twoich oczekiwaniach i wspólnie dobierzemy odpowiedni zabieg, który wykonamy podczas tej samej wizyty. Nie musisz martwić się wyborem — zajmiemy się tym na miejscu!', light=True)
    html += footer()
    write('zabiegi-na-twarz.html', html)


# =================================================================== RADIOFREKWENCJA
def rf():
    html = head('Radiofrekwencja mikroigłowa — Manikosmetyka',
                'Radiofrekwencja mikroigłowa — ujędrnienie, zmarszczki, blizny i rozstępy. Twarz i ciało. Manikosmetyka.') + header('rf')
    html += page_hero('Radiofrekwencja mikroigłowa', 'Radiofrekwencja mikroigłowa',
                      'Mikronakłuwanie połączone z falami radiowymi. Głęboka regeneracja i jędrność — na twarzy i na ciele.',
                      'zabieg-twarz-dlonie', 'Zabieg na twarz w gabinecie Manikosmetyka', '50% 40%')
    items = [('Ujędrnienie', 'Redukcja zmarszczek i poprawa napięcia skóry.'), ('Anti-aging', 'Odświeżona skóra bez oznak zmęczenia.'),
             ('Blizny', 'Wygładzenie blizn, także potrądzikowych.'), ('Rozstępy', 'Poprawa struktury skóry na ciele.'),
             ('Pory', 'Obkurczenie porów i wyrównanie struktury.'), ('Elastyczność', 'Skóra gładka, jędrna i sprężysta.')]
    feats = ''.join(f'<div class="feat rv"><h3 class="caps caps-md">{a}</h3><p>{b}</p></div>' for a, b in items)
    html += f'''
<section class="section">
  <div class="wrap">
    <div class="split" style="align-items:end">
      <div class="rv"><p class="label">Zastosowanie</p><h2 class="h2" style="margin-top:18px">Jeden zabieg, wiele efektów</h2></div>
      <p class="lead rv">Radiofrekwencja mikroigłowa działa w głębszych warstwach skóry, dlatego sprawdza się przy pierwszych oznakach starzenia, bliznach i rozstępach.</p>
    </div>
    <div class="grid-3" style="margin-top:clamp(56px,7vw,96px);row-gap:48px">{feats}</div>
  </div>
</section>

<section class="section-sm bg-dark">
  <div class="wrap split" style="align-items:center">
    <div class="rv"><p class="label">Aktualna promocja</p><h2 class="h2" style="margin-top:18px;font-size:clamp(30px,3.4vw,48px)">Radiofrekwencja mikroigłowa + zabieg przygotowujący w prezencie</h2></div>
    <div class="rv"><p class="body">Radiofrekwencja mikroigłowa z antyoksydacją oraz zabieg przygotowujący skórę. Dwie wizyty w jednym pakiecie.</p><div class="btns" style="margin-top:28px"><a class="btn btn-light" href="{BOOKSY}" {EXT}>Zarezerwuj</a></div></div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="head-row rv"><div><p class="label">Efekty</p><h2 class="h2">Przed i po serii</h2></div><a class="link" href="{IG}" {EXT}>Więcej na Instagramie <span class="arr" aria-hidden="true">→</span></a></div>
    <figure class="ba-wrap rv">
    <div class="ba" data-ba style="--ba: 50%">
      <img class="ba-img" src="img/rf-po.jpg" alt="Skóra klientki po serii zabiegów — przebarwienia wyraźnie rozjaśnione" loading="lazy" width="1050" height="1400">
      <div class="ba-before" aria-hidden="true"><img class="ba-img" src="img/rf-przed.jpg" alt="" loading="lazy" width="1050" height="1400"></div>
      <span class="ba-tag ba-tag-l" aria-hidden="true">Przed</span>
      <span class="ba-tag ba-tag-r" aria-hidden="true">Po</span>
      <span class="ba-handle" aria-hidden="true"><span class="ba-knob"></span></span>
      <input class="ba-range" type="range" min="0" max="100" value="50" step="1" aria-label="Porównanie przed i po — przesuń, aby zobaczyć efekt">
    </div>
    <figcaption>Ta sama klientka przed i po serii zabiegów · przesuń, aby porównać</figcaption>
    </figure>
  </div>
</section>
'''
    html += faq('Zanim przyjdziesz', [
        ('Ile zabiegów potrzebuję?', '[Do uzupełnienia przez salon: zalecana liczba zabiegów w serii i odstępy.]'),
        ('Kiedy widać efekty?', '[Do uzupełnienia przez salon.]'),
        ('Czy po zabiegu potrzebna jest regeneracja?', '[Do uzupełnienia przez salon: jak wygląda skóra po zabiegu i zalecenia.]'),
        ('Czy konsultacja jest płatna?', 'Nie, konsultacja w gabinecie jest bezpłatna.')])
    html += cta('Daj skórze nowy start', 'Zarezerwuj bezpłatną konsultację i sprawdź, czy radiofrekwencja mikroigłowa jest dla Ciebie.')
    html += footer()
    write('radiofrekwencja-mikroiglowa.html', html)



# =================================================================== SZKOLENIA
def szkolenia():
    html = head('Szkolenia ze stylizacji paznokci — Manikosmetyka',
                'Szkolenia ze stylizacji paznokci w Czerwionce-Leszczynach: kurs podstawowy, doszkolenia, zdobienia. Instruktorka NC Company.') + header('szkolenia')
    html += page_hero('Szkolenia', 'Szkolenia ze stylizacji paznokci',
                      'Naucz się stylizacji od instruktorki NC Company, która paznokcie robi od ponad 20 lat.',
                      'wnetrze-fotel', 'Wnętrze salonu Manikosmetyka', '50% 50%',
                      btns=f'<a class="btn btn-light" href="tel:{TEL}">Zadzwoń i zapytaj o termin</a><a class="btn btn-ghost" href="mailto:hukaneta@gmail.com">Napisz</a>')
    html += f'''
<section class="section">
  <div class="wrap split">
    <img class="portrait rv" src="img/aneta-o-nas.jpg" alt="Aneta Huk, instruktorka NC Company" style="object-position: 50% 20%" loading="lazy">
    <div class="rv">
      <p class="label">Instruktorka</p>
      <h2 class="h2" style="margin-top:18px">Aneta Huk</h2>
      <p class="lead" style="margin-top:26px">Instruktorka NC Company. Stylizacją paznokci zajmuje się od ponad 20 lat.</p>
      <p class="body" style="margin-top:20px">Na szkoleniach pokazuje to, co sprawdza się w codziennej pracy w salonie: poprawną technikę, higienę i sposoby na trwały, estetyczny efekt. Uczymy w małych grupach lub indywidualnie, z naciskiem na praktykę.</p>
    </div>
  </div>
</section>

<section class="section bg-stone">
  <div class="wrap">
    <div class="head-row rv"><div><p class="label">Oferta szkoleń</p><h2 class="h2">Wybierz swój poziom</h2></div></div>
    <div class="grid-2" style="row-gap:48px">
      <div class="feat rv"><h3 class="caps caps-md">Szkolenie podstawowe (basic)</h3><p>Dla osób zaczynających od zera: przygotowanie płytki, kształtowanie, opracowanie skórek, manicure hybrydowy oraz zasady higieny pracy.</p></div>
      <div class="feat rv"><h3 class="caps caps-md">Doszkolenie</h3><p>Dla osób, które już stylizują: poprawa techniki, trwałość stylizacji, praca na naturalnych paznokciach i najczęstsze błędy.</p></div>
      <div class="feat rv"><h3 class="caps caps-md">Zdobienia i trendy</h3><p>French, zdobienia, kolorystyka i aktualne trendy: jak tworzyć stylizacje, które klientki chcą powtarzać.</p></div>
      <div class="feat rv"><h3 class="caps caps-md">Szkolenie indywidualne</h3><p>Zakres i tempo dobrane do Ciebie: wybierasz temat, a my pracujemy tylko nad tym, czego potrzebujesz.</p></div>
    </div>
    <p class="note rv" style="margin-top:32px">Dokładny program, czas trwania i terminy ustalamy indywidualnie.</p>
  </div>
</section>

<section class="section bg-dark">
  <div class="wrap">
    <div class="rv" style="max-width:720px"><p class="label">Jak wygląda szkolenie</p><h2 class="h2" style="margin-top:18px">Teoria krótko, praktyka długo</h2></div>
    <div class="steps rv" style="margin-top:56px"><div class="grid-4">{steps([
        ('Rozmowa', 'Poznajemy Twój poziom i cel szkolenia.'),
        ('Pokaz', 'Instruktorka pokazuje technikę krok po kroku.'),
        ('Praktyka', 'Pracujesz samodzielnie, a my poprawiamy na bieżąco.'),
        ('Wskazówki', 'Dostajesz zalecenia, jak rozwijać się dalej.')])}</div></div>
  </div>
</section>
'''
    html += faq('Zanim się zapiszesz', [
        ('Czy muszę mieć doświadczenie?', 'Nie. Szkolenie podstawowe (basic) jest dla osób zaczynających od zera.'),
        ('Jak zapisać się na szkolenie?', 'Zadzwoń pod numer ' + TEL_H + ' lub napisz na hukaneta@gmail.com. Uzgodnimy zakres i termin.'),
        ('Czy można szkolić się indywidualnie?', 'Tak, szkolenie indywidualne to osobna opcja. Zakres i tempo dopasowujemy do Ciebie.')])
    html += f'''<section class="section bg-dark cta center">
  <div class="wrap rv">
    <p class="label">Zapraszamy</p>
    <h2 class="h2">Chcesz zacząć naukę?</h2>
    <p class="lead">Zadzwoń lub napisz, a dobierzemy szkolenie do Twojego poziomu.</p>
    <div class="btns"><a class="btn btn-light" href="tel:{TEL}">Zadzwoń</a><a class="btn btn-ghost" href="mailto:hukaneta@gmail.com">Napisz e-mail</a></div>
  </div>
</section>
'''
    html += footer()
    write('szkolenia.html', html)


# =================================================================== OFERTA
CATS = [
    ('depilacja', 'Depilacja laserowa', 'Laser diodowy Primelase. Pojedyncze zabiegi i pakiety.', 'depilacja-laserowa.html',
     [('Pojedyncza partia ciała', 'damska i męska'), ('Pakiet 4 partie', ''), ('Bikini płytkie / głębokie', ''), ('Bikini męskie', ''), ('Broda', ''), ('Pakiety 6 zabiegów', 'zapytaj o aktualną promocję')]),
    ('twarz', 'Pielęgnacja twarzy', 'Zabiegi dobierane po konsultacji.', 'zabiegi-na-twarz.html',
     [('Vivace — radiofrekwencja mikroigłowa: twarz, szyja, dekolt', ''), ('Mezoterapia mikroigłowa (dermapen)', ''), ('Oczyszczanie wodorowe', 'HydroRevive, HydroGlow, HydroLux'), ('Mikrodermabrazja', ''), ('Peelingi kwasowe i złuszczające', ''), ('Zabiegi PCA Skin', ''), ('Rytuał Glass skin', ''), ('Konsultacja z zabiegiem', ''), ('Konsultacja w gabinecie', 'bezpłatna')]),
    ('cialo', 'Zabiegi na ciało', '', 'radiofrekwencja-mikroiglowa.html',
     [('Vivace — radiofrekwencja mikroigłowa: ramiona, okolica nadkolanowa, uda, brzuch', ''), ('Endermologia Primelle', 'masaż próżniowy, drenaż'), ('Vivace — radiofrekwencja mikroigłowa: rozstępy i blizny', '')]),
    ('estetyczna', 'Medycyna estetyczna', '', '',
     [('Lipoliza iniekcyjna', 'seria 3–6 zabiegów'), ('Mezoterapia skóry głowy Dr Cyj Hair Filler', '')]),
    ('brwi', 'Brwi i rzęsy', '', '',
     [('Laminacja brwi', 'efekt 4–6 tygodni'), ('Henna pudrowa brwi', ''), ('Henna żelowa brwi z regulacją', ''), ('Henna rzęs', ''), ('Henna rzęs i brwi z regulacją', ''), ('Depilacja woskiem — brwi, wąsik, nos, cała twarz', '')]),
    ('pmu', 'Makijaż permanentny', '', '',
     [('Brwi metodą pudrową', 'z wizytą kontrolną po 6 tygodniach'), ('Korekta makijażu permanentnego', '')]),
    ('wizaz', 'Wizaż', '', '',
     [('Makijaż dzienny i wieczorowy', ''), ('Makijaż okolicznościowy', 'studniówka, sesje zdjęciowe, gala · możliwy dojazd'), ('Makijaż ślubny i próbny', 'możliwy dojazd')]),
    ('dlonie', 'Dłonie i stopy', '', '',
     [('Manicure hybrydowy / żelowy', ''), ('Manicure japoński', 'wzmacniająco-odżywczy'), ('French i stylizacje z inspiracji', ''), ('Pedicure pododyskiem', ''), ('Hybryda / żel na stopy', '')]),
    ('szkolenia', 'Szkolenia', 'Szkolenia ze stylizacji paznokci prowadzi Aneta, instruktorka NC Company.', 'szkolenia.html',
     [('Szkolenie podstawowe (basic)', 'stylizacja paznokci od podstaw'), ('Doszkolenie', 'dla osób, które już stylizują'), ('Zdobienia i trendy', ''), ('Szkolenie indywidualne', 'zakres dobrany do Ciebie')]),
    ('uszy', 'Przekłuwanie uszu', '', '',
     [('Przekłuwanie płatków uszu systemem Studex', 'kolczyki hipoalergiczne w cenie'), ('Przekłuwanie dzieci metodą duo', '')]),
]


def oferta():
    html = head('Oferta — Manikosmetyka',
                'Pełna oferta salonu Manikosmetyka: depilacja laserowa, twarz, ciało, brwi, makijaż permanentny, wizaż, szkolenia ze stylizacji paznokci.') + header('oferta')
    html += page_hero('Oferta', 'Pełna oferta salonu',
                      'Ceny dobieramy indywidualnie — aktualne znajdziesz przy rezerwacji online lub zapytaj telefonicznie.',
                      'twarz-swiece', 'Świece i profesjonalne kosmetyki w gabinecie', '50% 55%')
    nav = ''.join(f'<a href="#{k}">{t}</a>' for k, t, *_ in CATS)
    html += f'<nav class="cat-nav" aria-label="Kategorie"><div class="wrap">{nav}</div></nav>\n<section><div class="wrap">'
    for k, t, d, href, items in CATS:
        li = ''.join(f'<li><span>{a}</span>{f"<small>{b}</small>" if b else ""}</li>' for a, b in items)
        side = f'<p class="body">{d}</p>' if d else ''
        if href:
            side += f'<a class="link" href="{href}">Szczegóły <span class="arr" aria-hidden="true">→</span></a>'
        html += f'<div class="cat" id="{k}"><div class="rv"><h2 class="h2">{t}</h2>{side}</div><ul class="lines rv">{li}</ul></div>'
    html += '</div></section>\n'
    html += cta('Nie wiesz, co wybrać?', 'Konsultacja w gabinecie jest bezpłatna. Doradzimy zabieg i podamy cenę dla Twojego przypadku.', light=True)
    html += footer()
    write('oferta.html', html)


# =================================================================== O NAS
def onas():
    html = head('O nas — Manikosmetyka', 'Poznaj salon Manikosmetyka i nasz zespół. Czerwionka-Leszczyny, ul. Ligonia 8.') + header('onas')
    html += page_hero('O nas', 'Piękno z profesjonalizmem',
                      'Salon w Czerwionce-Leszczynach, w którym każda wizyta ma być chwilą tylko dla Ciebie.',
                      'wnetrze-kacik', 'Wnętrze salonu Manikosmetyka', '50% 55%')
    html += f'''
<section class="section">
  <div class="wrap">
    <div class="split" style="align-items:end">
      <div class="rv"><p class="label">Nasze zasady</p><h2 class="h2" style="margin-top:18px">Dbamy o każdy detal</h2></div>
      <p class="lead rv">Nasz zespół z pasją dba o każdy etap wizyty — od konsultacji po efekt, który zostaje na długo.</p>
    </div>
    <div class="grid-4" style="margin-top:clamp(56px,7vw,96px)">
      <div class="feat rv"><h3 class="caps caps-md">Konsultacje gratis</h3><p>Zanim cokolwiek zrobimy, rozmawiamy.</p></div>
      <div class="feat rv"><h3 class="caps caps-md">Sterylność</h3><p>Sterylizowane narzędzia i jednorazowe akcesoria.</p></div>
      <div class="feat rv"><h3 class="caps caps-md">Sprawdzone marki</h3><p>Profesjonalne kosmetyki i nowoczesny sprzęt.</p></div>
      <div class="feat rv"><h3 class="caps caps-md">Komfort</h3><p>Bezpłatny parking przy salonie i płatność kartą.</p></div>
    </div>
  </div>
</section>

<section class="section bg-stone">
  <div class="wrap">
    <div class="head-row rv"><div><p class="label">Zespół</p><h2 class="h2">Poznaj nasze dziewczyny</h2></div></div>
    <div class="grid-3" style="gap:clamp(40px,5vw,72px)">
      <article class="rv">
        <img class="portrait" src="img/aneta-o-nas.jpg" alt="Aneta Huk" style="object-position: 50% 20%" loading="lazy">
        <p class="label" style="margin-top:28px">Właścicielka</p>
        <h3 class="caps caps-lg" style="margin-top:12px">Aneta Huk</h3>
        <p class="body" style="margin-top:14px">Z pasją i profesjonalizmem wykonuje zabiegi na twarz i ciało, dbając o każdy detal. Od ponad 20 lat zajmuje się również stylizacją paznokci i jest instruktorką NC Company. W swojej pracy stawia na jakość, precyzję i indywidualne podejście.</p>
      </article>
      <article class="rv">
        <img class="portrait" src="img/kamila.jpg" alt="Kamila, linergistka" style="object-position: 50% 15%" loading="lazy">
        <p class="label" style="margin-top:28px">Linergistka</p>
        <h3 class="caps caps-lg" style="margin-top:12px">Kamila</h3>
        <p class="body" style="margin-top:14px">Jej pasją jest sztuka podkreślania naturalnego piękna. Szczególną uwagę poświęca harmonii twarzy, idealnie dobranej oprawie brwi i subtelnym detalom, które wydobywają urodę. W swojej pracy łączy wyczucie estetyki, precyzję i zamiłowanie do makijażu.</p>
      </article>
      <article class="rv">
        <img class="portrait" src="img/paulina.jpg" alt="Paulina, stylistka paznokci" style="object-position: 50% 22%" loading="lazy">
        <p class="label" style="margin-top:28px">Stylistka paznokci</p>
        <h3 class="caps caps-lg" style="margin-top:12px">Paulina</h3>
        <p class="body" style="margin-top:14px">Z pasją tworzy stylizacje, które podkreślają indywidualny styl każdej klientki. Dba o estetykę, staranne wykończenie i piękny efekt, zarówno w klasycznych, jak i bardziej wyrazistych stylizacjach.</p>
      </article>
    </div>
  </div>
</section>

<section class="section-sm bg-dark">
  <div class="wrap"><div class="stats rv" style="border:0;padding:0">
    <div class="stat"><b>5,0</b><span>ocena Booksy</span></div>
    <div class="stat"><b>734</b><span>opinie klientek</span></div>
    <div class="stat"><b>20+</b><span>lat w stylizacji paznokci</span></div>
  </div></div>
</section>

<section class="section">
  <div class="wrap">
    <div class="head-row rv"><div><p class="label">Gabinet</p><h2 class="h2">Zajrzyj do środka</h2></div></div>
    <div class="grid-4" style="gap:12px">
      <img class="media r-34 rv" src="img/wnetrze-polki.jpg" alt="Półki z kosmetykami w salonie" loading="lazy">
      <img class="media r-34 rv" src="img/gabinet-zabiegowy.jpg" alt="Gabinet zabiegowy" loading="lazy">
      <img class="media r-34 rv" src="img/wnetrze-lilie.jpg" alt="Kawa i lilie w strefie relaksu" loading="lazy">
      <img class="media r-34 rv" src="img/wnetrze-wazon.jpg" alt="Detal wnętrza salonu" loading="lazy">
    </div>
  </div>
</section>
'''
    html += cta('Do zobaczenia w salonie', 'ul. Ligonia 8, Czerwionka-Leszczyny · poniedziałek–piątek 8:00–20:00', light=True)
    html += footer()
    write('o-nas.html', html)


# =================================================================== BONY
def bony():
    html = head('Bony podarunkowe — Manikosmetyka', 'Bony podarunkowe Manikosmetyka — na kwotę lub wybrany zabieg.') + header('bony')
    html += page_hero('Bony podarunkowe', 'Podaruj chwilę dla siebie',
                      'Bon do Manikosmetyki to prezent, który zawsze trafia. Wybierz kwotę albo konkretny zabieg.',
                      'kwiaty-lustro', 'Kwiaty i kosmetyki w salonie', '50% 45%',
                      btns=f'<a class="btn btn-light" href="#bon">Skomponuj bon</a>')
    am = ''.join(f'<button class="btn btn-line" type="button" data-pick="amount" data-val="{a}" aria-pressed="false">{a}</button>' for a in ['100 zł', '200 zł', '300 zł', '500 zł'])
    tr = ''.join(f'<button class="btn btn-line" type="button" data-pick="treatment" data-val="{a}" aria-pressed="false">{a}</button>' for a in ['Depilacja laserowa', 'Radiofrekwencja mikroigłowa', 'Mezoterapia', 'Laminacja brwi'])
    html += f'''
<section class="section" id="bon" style="scroll-margin-top:var(--header-h)">
  <div class="wrap split">
    <div class="rv keep">
      <div class="voucher" aria-live="polite">
        <span class="logo"><b>MANIKOSMETYKA</b><i>salon kosmetyczny</i></span>
        <div><p class="label" style="color:rgba(248,244,238,.7)">Bon podarunkowy</p><p class="voucher-val" data-voucher-value style="margin:12px 0 0">200 zł</p></div>
      </div>
      <p class="note" style="margin-top:16px">Podgląd bonu</p>
    </div>
    <div class="cfg rv" data-voucher>
      <div><p class="label" style="margin-bottom:14px">1. Rodzaj bonu</p><div class="btns"><button class="btn btn-line" type="button" data-pick="type" data-val="amount" aria-pressed="true">Kwota</button><button class="btn btn-line" type="button" data-pick="type" data-val="treatment" aria-pressed="false">Zabieg</button></div></div>
      <div data-group="amount"><p class="label" style="margin-bottom:14px">2. Kwota</p><div class="btns">{am}</div><p class="note" style="margin-top:12px">[Kwoty przykładowe — do ustalenia z salonem]</p></div>
      <div data-group="treatment" hidden><p class="label" style="margin-bottom:14px">2. Zabieg</p><div class="btns">{tr}</div></div>
      <div style="border-top:1px solid var(--line);padding-top:28px">
        <div class="btns"><span class="btn btn-dark" role="link" aria-disabled="true">Kup online — wkrótce</span><a class="btn btn-line" href="tel:{TEL}">Zamów telefonicznie</a></div>
        <p class="note" style="margin-top:14px">Bon kupisz też na miejscu w salonie.</p>
      </div>
    </div>
  </div>
</section>

<section class="section bg-stone">
  <div class="wrap split">
    <img class="media r-34 rv" src="img/bon-podarunkowy.jpg" alt="Bon podarunkowy Manikosmetyki w eleganckiej kopercie" loading="lazy" style="max-width:460px">
    <div class="rv">
      <p class="label">Bon w salonie</p>
      <h2 class="h2" style="margin-top:18px">Elegancki bon w kopercie</h2>
      <ul class="lines" style="margin-top:32px"><li><span>Ważność</span><small>pół roku od zakupu</small></li><li><span>Wykorzystanie</span><small>na jeden lub kilka zabiegów</small></li><li><span>Odbiór</span><small>w salonie, ul. Ligonia 8</small></li></ul>
    </div>
  </div>
</section>

<section class="section bg-dark">
  <div class="wrap">
    <div class="rv"><p class="label">Jak to działa</p><h2 class="h2" style="margin-top:18px">Prezent w trzech krokach</h2></div>
    <div class="steps rv" style="margin-top:56px"><div class="grid-3">{steps([
        ('Wybierz bon', 'Kwota do wykorzystania na dowolne usługi albo konkretny zabieg.'),
        ('Odbierz', 'Elegancki bon w salonie. [Wkrótce: wersja elektroniczna na e-mail.]'),
        ('Podaruj', 'Obdarowana umawia się na dogodny termin.')])}</div></div>
  </div>
</section>
'''
    html += faq('Warto wiedzieć', [
        ('Jak długo bon jest ważny?', 'Bon jest ważny pół roku od daty zakupu.'),
        ('Czy bon można wykorzystać na kilka zabiegów?', 'Tak, wartość bonu można wykorzystać na kilka zabiegów.'),
        ('Jak umówić wizytę z bonem?', 'Wystarczy zarezerwować termin online lub telefonicznie i pokazać bon w salonie.')])
    html += footer()
    write('bony-podarunkowe.html', html)


# =================================================================== KONTAKT
def kontakt():
    html = head('Kontakt — Manikosmetyka', 'Kontakt: ul. Ligonia 8, 44-238 Czerwionka-Leszczyny, tel. +48 511 483 630. Pon–Pt 8:00–20:00.') + header('kontakt')
    html += page_hero('Kontakt', 'Zapraszamy do salonu',
                      'Najszybciej umówisz się online. Masz pytanie? Zadzwoń lub napisz — chętnie doradzimy.',
                      'wizytowka', 'Wizytówka Manikosmetyka na półce w salonie', '50% 50%',
                      btns=f'<a class="btn btn-light" href="{BOOKSY}" {EXT}>Umów wizytę online</a><a class="btn btn-ghost" href="tel:{TEL}">Zadzwoń</a>')
    html += f'''
<section class="section">
  <div class="wrap split" style="align-items:start">
    <div class="rv">
      <h2 class="h2">Manikosmetyka</h2>
      <div class="info" style="margin-top:40px">
        <div class="info-row"><span class="label">Adres</span><div><p>ul. Ligonia 8<br>44-238 Czerwionka-Leszczyny</p><a class="link" href="{MAPS}" {EXT} style="margin-top:14px;font-size:12px">Wyznacz trasę <span class="arr" aria-hidden="true">→</span></a></div></div>
        <div class="info-row"><span class="label">Telefon</span><a href="tel:{TEL}">{TEL_H}</a></div>
        <div class="info-row"><span class="label">E-mail</span><a href="mailto:hukaneta@gmail.com">hukaneta@gmail.com</a></div>
        <div class="info-row"><span class="label">Godziny</span><div class="hours"><span>Poniedziałek – piątek</span><span>8:00 – 20:00</span><span>Sobota</span><span>[do uzupełnienia]</span><span>Niedziela</span><span>nieczynne</span></div></div>
        <div class="info-row"><span class="label">Social media</span><p><a href="{IG}" {EXT}>Instagram</a> &nbsp;·&nbsp; <a href="{FB}" {EXT}>Facebook</a></p></div>
      </div>
    </div>
    <a class="rv" href="{MAPS}" {EXT} style="display:block;position:relative;text-decoration:none">
      <img class="media r-45" src="img/wnetrze-kawa.jpg" alt="Strefa relaksu w salonie" loading="lazy">
      <span class="btn btn-light" style="position:absolute;left:20px;bottom:20px">Otwórz w Mapach Google</span>
    </a>
  </div>
</section>

<section class="section-sm bg-stone">
  <div class="wrap grid-3">
    <div class="feat rv"><h3 class="caps caps-md">Parking</h3><p>Parking przy salonie jest bezpłatny.</p></div>
    <div class="feat rv"><h3 class="caps caps-md">Płatność kartą</h3><p>Akceptujemy karty płatnicze.</p></div>
    <div class="feat rv"><h3 class="caps caps-md">Odwołanie wizyty</h3><p>Prosimy o informację z wyprzedzeniem — szczegóły w regulaminie salonu.</p></div>
  </div>
</section>
'''
    html += footer()
    write('kontakt.html', html)


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for fn in (home, depilacja, twarz, rf, szkolenia, oferta, onas, bony, kontakt):
        fn()
    print('ok', OUT)
