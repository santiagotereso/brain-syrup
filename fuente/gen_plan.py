# -*- coding: utf-8 -*-
"""Documento de scope y presupuesto de Brain Syrup. Fondo oscuro, paleta turquesa."""
import base64, io, os, datetime as dt
from PIL import Image

DESK = os.path.join(os.path.expanduser("~"), "Desktop")
OUT = "plan-brain-syrup.html"

# ---- miniaturas y logo: se recortan del Escritorio la primera vez y quedan
# cacheados en _assets.json, asi el documento se regenera aunque borres las fuentes
import json
CACHE = "_assets.json"
thumbs, LOGO = {}, ""
ORDEN = ["gravity", "fears", "seniors", "internet"]
try:
    CROPS = [("internet", (22, 20, 402, 232)), ("seniors", (418, 20, 790, 232)),
             ("fears", (808, 20, 1190, 232)), ("gravity", (22, 338, 402, 548))]
    src = Image.open(os.path.join(DESK, "thumbnails.JPG")).convert("RGB")
    for name, box in CROPS:
        im = src.crop(box)
        im = im.resize((460, int(460 * im.height / im.width)), Image.LANCZOS)
        buf = io.BytesIO(); im.save(buf, "JPEG", quality=80, optimize=True)
        thumbs[name] = "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
    _lg = Image.open(os.path.join(DESK, "logosolo.JPG")).convert("RGB").crop((21, 12, 165, 156))
    _lg = _lg.resize((288, 288), Image.LANCZOS)
    _b = io.BytesIO(); _lg.save(_b, "JPEG", quality=88, optimize=True)
    LOGO = "data:image/jpeg;base64," + base64.b64encode(_b.getvalue()).decode()
    json.dump({"logo": LOGO, "thumbs": [thumbs[k] for k in ORDEN]},
              io.open(CACHE, "w", encoding="utf-8"))
except Exception:
    d = json.load(io.open(CACHE, encoding="utf-8"))
    LOGO = d["logo"]
    thumbs = dict(zip(ORDEN, d["thumbs"]))

PUBLICADOS = [
    ("gravity",  u"Gravity undo",                 u"11:43", u"4.700",  75,  False),
    ("fears",    u"Why Are People Afraid of This?", u"9:24", u"12.000", 100, False),
    ("seniors",  u"SUPER SENIORS",                u"4:30",  u"2.700",  75,  False),
    ("internet", u"They understand The Internet", u"2:02",  u"41.000", 150, True),
]
cards = u"".join(
    u'<figure class="vid"><img src="%s" alt="Miniatura de %s">'
    u'<figcaption><p class="vnum">Video %02d</p><b>%s</b>'
    u'<p class="vstats"><span>%s</span><em>%s vistas</em></p>'
    u'<p class="gasto">$%d <small>en ads</small></p></figcaption></figure>'
    % (thumbs[k], t, i + 1, t, dur, views, gasto)
    for i, (k, t, dur, views, gasto, dest) in enumerate(PUBLICADOS))

# ---- semanas de posteo: del lunes 12 de octubre al 31 de diciembre
MES = {10: u"octubre", 11: u"noviembre", 12: u"diciembre"}
MESAB = {10: u"oct", 11: u"nov", 12: u"dic"}
semanas, d = [], dt.date(2026, 10, 12)
while d <= dt.date(2026, 12, 31):
    semanas.append(d); d += dt.timedelta(days=7)

viernes = [w + dt.timedelta(days=4) for w in semanas
           if w + dt.timedelta(days=4) <= dt.date(2026, 12, 31)]

head_dia = u"".join(u'<th class="c">%d %s</th>' % (w.day, MESAB[w.month]) for w in semanas)
fila_post = u"".join(
    u'<td class="c"><span class="chip chip--short">%d</span></td>' % (6 if i == 1 else 5)
    for i, w in enumerate(semanas))
fila_prod = u"".join(
    (u'<td class="c"><span class="chip chip--ent">5 trailers</span></td>' if i == 0 else
     u'<td class="c"><span class="chip chip--ent">6 cortos</span></td>' if i == 1 else
     u'<td class="c"><span class="na">&mdash;</span></td>')
    for i, w in enumerate(semanas))
# Pauta desde el lunes 19. La semana del 30 de noviembre queda afuera para que
# ningun mes pase de $1.000: noviembre tiene cinco lunes.
fila_pauta = u"".join(
    (u'<td class="c"><span class="pa">$250</span></td>'
     if i >= 1 and w != dt.date(2026, 11, 30)
     else u'<td class="c"><span class="na">&mdash;</span></td>')
    for i, w in enumerate(semanas))
assert sum(1 for i, w in enumerate(semanas)
           if i >= 1 and w != dt.date(2026, 11, 30)) == 10
fila_video = u"".join(
    (u'<td class="c"><span class="chip chip--pub">V%02d</span></td>' % (i + 5))
    if i < len(viernes) else u'<td class="c"><span class="na">&mdash;</span></td>'
    for i in range(len(semanas)))

futuros = u"".join(
    u'<div class="slot"><span class="slot-n">Video %02d</span>'
    u'<span class="slot-d">viernes %d de %s</span></div>' % (5 + i, v.day, MES[v.month])
    for i, v in enumerate(viernes))

HTML = u"""<title>Scope y presupuesto</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap">

<style>
:root{
  color-scheme:dark;
  --bg:#0F1418; --panel:#161D23; --panel-2:#1B242B;
  --ink:#E7EDF2; --ink-soft:#AFBCC7; --ink-faint:#7A8995;
  --line:#242E36; --line-strong:#38454F;
  --teal:#2DD4BF; --teal-soft:#122E2C;
  --past:#8A98A5; --past-bg:#1A2027;
  --blue:#93B4FD; --blue-soft:#15203A;
  --sans:"Inter","Segoe UI",system-ui,-apple-system,Helvetica,Arial,sans-serif;
}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);
  font-family:var(--sans);font-size:15px;line-height:1.55;-webkit-font-smoothing:antialiased}
.wrap{max-width:1600px;margin:0 auto;padding-block:20px 64px;padding-left:20px;padding-right:20px}
p{margin:0 0 12px}

header{display:flex;align-items:center;gap:22px;flex-wrap:wrap;padding-bottom:20px;border-bottom:1px solid var(--line)}
.logo{flex:none;width:88px;height:88px;border-radius:50%;display:block}
h1{font-size:clamp(30px,4.2vw,46px);font-weight:800;letter-spacing:-.03em;line-height:1.02;margin:0}
.kicker{font-size:12.5px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;
  color:var(--teal);margin:0 0 10px}

.nav{margin-left:auto;display:flex;gap:8px;flex-wrap:wrap;align-self:center}
.tab{text-decoration:none;border:1px solid var(--line-strong);color:var(--ink-faint);font-size:13.5px;font-weight:600;padding:8px 16px;border-radius:999px;white-space:nowrap}
.tab:hover{color:var(--ink);border-color:var(--teal)}
.tab.on{background:var(--teal);border-color:var(--teal);color:#06211E}
h2{font-size:21px;letter-spacing:-.015em;color:var(--ink);font-weight:700;
  margin:46px 0 14px;display:flex;align-items:center;gap:14px}
h2::after{content:"";flex:1;height:1px;background:var(--line)}
h3{font-size:12px;letter-spacing:.08em;text-transform:uppercase;font-weight:700;color:var(--ink-faint);
  margin:22px 0 10px}


#budwrap .p{display:none}
#budwrap.open .p{display:table-cell}
#budwrap:not(.open) .hoy{border-left:0!important}
#budwrap:not(.open) td.next{font-size:19px}
#budwrap:not(.open) .only-open{display:none}
#budwrap:not(.open) .grand .vnext{font-size:30px}
#budwrap.open tr.only-open{display:table-row}
.budbar{display:flex;justify-content:flex-end;margin:0 0 10px}
.objbar{display:flex;justify-content:flex-end;gap:6px;margin:-34px 0 10px}
.obj{appearance:none;border:1px solid var(--line);background:transparent;color:var(--ink-faint);font:inherit;font-size:12px;font-weight:600;padding:5px 12px;border-radius:999px;cursor:pointer}
.obj:hover{color:var(--ink)}
.obj.on{color:var(--teal);border-color:var(--teal)}
#budtoggle{appearance:none;border:1px solid var(--line-strong);background:transparent;
  color:var(--ink-faint);font:inherit;font-size:12.5px;font-weight:600;padding:6px 13px;
  border-radius:999px;cursor:pointer}
#budtoggle:hover{color:var(--ink)}
.cols4{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
@media(max-width:860px){.cols4{grid-template-columns:repeat(2,1fr)}}
.cols2{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.cols6{display:grid;grid-template-columns:repeat(6,1fr);gap:12px}
.split{display:grid;grid-template-columns:1.05fr .95fr;gap:16px;align-items:start}
@media(max-width:1180px){.cols6{grid-template-columns:repeat(4,1fr)}}
@media(max-width:980px){.cols2,.split{grid-template-columns:1fr 1fr}}
@media(max-width:680px){.cols2,.cols6,.split{grid-template-columns:1fr}}

.card{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:20px 22px}
.card h4{margin:0 0 14px;font-size:19px;font-weight:700;letter-spacing:-.02em}
.card h4 .who{display:block;font-size:13px;font-weight:500;color:var(--ink-faint);
  letter-spacing:0;margin-top:3px}
.card ul{margin:0;padding-left:20px}
.card li{margin-bottom:11px;font-size:16px;font-weight:500}
.card li:last-child{margin-bottom:0}

.tw.fit th,.tw.fit td{white-space:normal}
.tw.fit .sublabel{white-space:normal}
.tw{overflow-x:auto;border:1px solid var(--line);border-radius:10px;background:var(--panel);margin:0 0 10px}
table{border-collapse:collapse;width:100%;font-size:14px}
th,td{text-align:left;padding:10px 14px;border-bottom:1px solid var(--line);white-space:nowrap}
thead th{font-size:10.5px;letter-spacing:.09em;text-transform:uppercase;color:var(--ink-faint);
  font-weight:600;background:var(--panel-2)}
tbody th{font-weight:600}
td.n,th.n{text-align:right;font-variant-numeric:tabular-nums}
td.c,th.c{text-align:center}
td.z{color:var(--ink-faint);text-align:right}
tr.hip th,tr.hip td{color:var(--past)}
td.past{color:var(--past);font-size:12px;padding-top:7px;padding-bottom:7px}
td.z{font-size:12px}
thead th.n{font-size:10px}
thead th.hoy,thead th:nth-child(n+8){font-size:11.5px;color:var(--teal)}
td.next{color:var(--teal);font-size:16px;font-weight:600}
td.tot{font-weight:700;background:var(--panel-2)}
tr:last-child td,tr:last-child th{border-bottom:0}
tr.sumrow th,tr.sumrow td{background:var(--panel-2);font-weight:700;font-size:15px;
  border-top:1px solid var(--line-strong)}
tr.sumrow td.past{color:var(--past);font-size:12px;padding-top:7px;padding-bottom:7px}
td.z{font-size:12px}
thead th.n{font-size:10px}
thead th.hoy,thead th:nth-child(n+8){font-size:11.5px;color:var(--teal)}
tr.sumrow td.next{color:var(--teal);font-size:16px;font-weight:600}

/* calendario: columnas centradas, unidas por una linea */
.cal th.c,.cal td.c{border-left:1px solid var(--line)}
.cal thead th.c{color:var(--ink-soft);font-size:11.5px;letter-spacing:.04em;text-transform:none}
.cal tbody th{color:var(--ink-soft)}
.cal td.c{position:relative}
.cal tbody tr:first-child td.c::before{content:"";position:absolute;top:0;left:50%;width:1px;height:10px;
  background:var(--line-strong)}

.hoy{border-left:2px solid var(--teal)!important}
th.hoy{color:var(--teal)}
.nota{margin:0;padding:30px 34px;border:1px solid var(--line);border-left:3px solid var(--teal);border-radius:10px;background:var(--panel)}
.nota p + p{margin-top:16px}
.hl{color:var(--teal);font-weight:700}
.nota p{margin:0;font-size:21px;line-height:1.5;letter-spacing:-.01em;color:var(--ink)}
.sublabel{display:block;font-weight:400;font-size:12px;color:var(--ink-faint);margin-top:2px}
.grand{display:flex;flex-wrap:wrap;border:1px solid var(--line);border-radius:10px;
  background:var(--panel);overflow:hidden}
.grand div{flex:1;min-width:190px;padding:16px 20px;border-right:1px solid var(--line)}
.grand div:last-child{border-right:0}
.grand span{display:block;font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-faint)}
.grand b{display:block;font-size:24px;font-weight:800;letter-spacing:-.02em;margin-top:4px;
  font-variant-numeric:tabular-nums}
.grand .vpast{color:var(--past)} .grand .vnext{color:var(--teal)} .grand .vtot{color:var(--ink)}

.chip{display:inline-block;font-size:11.5px;font-weight:700;letter-spacing:.04em;padding:3px 10px;
  border-radius:999px;white-space:nowrap}
.chip--pub{background:var(--teal-soft);color:var(--teal)}
.chip--short{background:var(--blue-soft);color:var(--blue)}
.chip--ent{background:#2A2413;color:var(--warn)}
.chip--ads{background:var(--teal);color:#06211E}
.h1b{color:var(--teal)}
.chip--goal{background:var(--teal);color:#06211E;margin-left:10px;vertical-align:1px}
tr.goal th,tr.goal td{background:rgba(45,212,191,.08)}
tr.goal th:first-child{box-shadow:inset 3px 0 0 var(--teal)}
.legend{display:flex;gap:20px;flex-wrap:wrap;font-size:13px;color:var(--ink-faint);margin:0 0 12px;
  align-items:center}

.vid{margin:0;background:var(--panel);border:1px solid var(--line);border-radius:10px;
  overflow:hidden;min-height:168px;display:flex;flex-direction:column}
.vid img{display:block;width:100%;height:auto}
.vid figcaption{padding:9px 11px 11px;flex:1;display:flex;flex-direction:column;justify-content:space-between}
.vnum{margin:0 0 4px;font-size:11.5px;font-weight:700;letter-spacing:.04em;color:var(--ink-faint)}
.vid figcaption b{display:block;font-size:12.5px;font-weight:600;line-height:1.3;color:var(--ink-soft);
  overflow:hidden;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical}
.vid .vstats{margin:7px 0 0;display:flex;align-items:center;gap:7px;flex-wrap:wrap}
.vid .vstats span{font-size:14px;font-weight:700;font-variant-numeric:tabular-nums}
.vid .vstats em{font-style:normal;font-size:14px;font-weight:700;color:var(--teal);
  font-variant-numeric:tabular-nums}
.vid .gasto{margin:8px 0 0;padding-top:8px;border-top:1px solid var(--line);font-size:17px;font-weight:800;letter-spacing:-.02em;color:var(--teal)}
.vid .gasto small{font-size:11.5px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-faint)}

.slot{border:1px dashed var(--line-strong);border-radius:10px;padding:14px;min-height:168px;
  display:flex;flex-direction:column;justify-content:center;gap:4px;background:var(--panel-2)}
.slot-n{font-size:13px;font-weight:700;color:var(--ink-faint);letter-spacing:.04em}
.slot-d{font-size:12.5px;color:var(--ink-faint)}

.steps{margin:10px 0 0;padding-left:20px}
.steps li{font-size:15.5px;margin-bottom:9px;color:var(--ink-soft)}
.steps li b{color:var(--ink)}
td .pa{font-weight:600;color:var(--teal)}
td .na{color:var(--ink-faint)}
.pie{font-size:16.5px;line-height:1.55;color:var(--ink-soft);margin:12px 0 0;max-width:none}
.aviso{margin:16px 0 0;padding:18px 22px;border:1px solid var(--line);
  border-left:3px solid #E9B949;border-radius:10px;background:var(--panel)}
.aviso p{margin:0;font-size:17px;line-height:1.5;color:var(--ink-soft);max-width:none}
.aviso b{color:#E9B949}
.answer{font-size:14.5px;color:var(--ink-faint);margin:12px 0 0}
</style>

<div class="wrap">

<header>
  <img class="logo" src="__LOGO__" alt="Logo de Brain Syrup">
  <div>
    <p class="kicker">Objetivo</p>
    <h1>Brain Syrup <span class="h1b">YouTube Channel</span></h1>
  </div>
  <nav class="nav">
    <a class="tab on" href="https://santiagotereso.github.io/brain-syrup/" aria-current="page">Objetivo</a>
    <a class="tab" href="https://santiagotereso.github.io/brain-syrup/seguimiento/">Seguimiento</a>
    <a class="tab" href="https://santiagotereso.github.io/brain-syrup/videos/">Videos</a>
    <a class="tab" href="https://santiagotereso.github.io/brain-syrup/picadora/">Picadora</a>
    <a class="tab" href="https://santiagotereso.github.io/brain-syrup/cuentas/">Cuentas</a>
    <a class="tab" href="https://santiagotereso.github.io/brain-syrup/cta/">Mejor call to action</a>
    <a class="tab" href="https://santiagotereso.github.io/brain-syrup/posteos/">Posteos</a>
    <a class="tab" href="https://santiagotereso.github.io/brain-syrup/referencias/">Material de estudio</a>
  </nav>
</header>

<section id="p2">

<h2>El plan</h2>
<div class="grand">
  <div><span>Publicaciones por semana</span><b class="vnext">5</b></div>
  <div><span>Plataformas</span><b class="vtot">3</b></div>
  <div><span>Pauta por semana</span><b class="vnext">$250</b></div>
  <div><span>Publicaciones hasta el 31 de diciembre</span><b class="vtot">60</b></div>
  <div><span>Pauta del trimestre</span><b class="vnext">$2.500</b></div>
</div>
<p class="pie">Cada publicaci&oacute;n sale en TikTok, Reels y Shorts: son 180 posteos. El 60% de la pauta va a la pieza que ya est&aacute; funcionando sola y el 40% se reparte en las otras cuatro.</p>

<h2>Los pr&oacute;ximos diez d&iacute;as</h2>
<div class="grand">
  <div><span>Al viernes 16</span><b class="vnext">5 cortos</b></div>
  <div><span>Semana del 19</span><b class="vnext">6 cortos</b></div>
  <div><span>Por video largo</span><b class="vtot">1 trailer</b></div>
  <div><span>Pr&oacute;ximo video largo</span><b class="vtot">23 de octubre</b></div>
</div>
<p class="pie">Diez d&iacute;as dedicados solo a formato corto, con el video largo en paralelo.
El corte de cada video deja de ser un recorte suelto y pasa a ser <b>un trailer</b>.</p>

<div class="split" style="margin-top:16px">
  <div class="tw fit">
    <table>
      <thead><tr><th>Video largo</th><th class="n">Dura</th><th class="n">Viernes 16</th>
        <th class="n">Semana del 19</th></tr></thead>
      <tbody>
        <tr><th>An iPhone built with 1960s tech</th><td class="n">1:53</td>
          <td class="n next">Trailer</td><td class="n z">&mdash;</td></tr>
        <tr><th>They understand The Internet</th><td class="n">2:01</td>
          <td class="n next">Trailer</td><td class="n z">&mdash;</td></tr>
        <tr><th>SUPER SENIORS <span class="sublabel">Sin presentador, tratamiento cinematogr&aacute;fico</span></th>
          <td class="n">4:29</td><td class="n next">Trailer</td><td class="n next">2 cortos</td></tr>
        <tr><th>Why Are People Afraid of This?</th><td class="n">9:23</td>
          <td class="n next">Trailer</td><td class="n next">2 cortos</td></tr>
        <tr><th>Gravity undo</th><td class="n">11:43</td>
          <td class="n next">Trailer</td><td class="n next">2 cortos</td></tr>
        <tr class="sumrow"><th>Total</th><td class="n z">&mdash;</td>
          <td class="n next">5</td><td class="n next">6</td></tr>
      </tbody>
    </table>
  </div>
  <div class="card">
    <h4>C&oacute;mo es el trailer</h4>
    <ul>
      <li>Uno por video, de alta calidad, en lugar de varios recortes del mismo material.</li>
      <li>El presentador resume el concepto en c&aacute;mara.</li>
      <li><b>Call to action:</b> ver el episodio completo. Nunca pedir suscripciones.</li>
      <li>Voz en off uniforme en los cinco, para que se reconozcan como serie.</li>
      <li>La gr&aacute;fica vertical del call to action la hace Federico.</li>
    </ul>
    <p class="answer">El iPhone y The Internet no llevan cortos extra: duran menos de dos minutos y
      el trailer ya se lleva lo mejor. Si despu&eacute;s hace falta volumen, The Internet es de donde
      m&aacute;s se puede sacar, porque es ficci&oacute;n y cada pedazo se entiende solo.</p>
  </div>
</div>

<h2>Qu&eacute; decir al final</h2>
<div class="split">
  <div class="tw fit">
    <table>
      <thead><tr><th>La placa final</th><th>Qu&eacute; dice</th></tr></thead>
      <tbody>
        <tr><th>YouTube Shorts</th><td class="mono">FULL EPISODE ON THE CHANNEL</td></tr>
        <tr><th>TikTok</th><td class="mono">FULL EPISODE ON YOUTUBE &mdash; LINK IN BIO</td></tr>
        <tr><th>Instagram Reels</th><td class="mono">FULL EPISODE ON YOUTUBE &mdash; LINK IN BIO</td></tr>
      </tbody>
    </table>
  </div>
  <div class="card">
    <h4>Tres reglas</h4>
    <ol class="steps">
      <li><b>El &uacute;ltimo cuadro siempre lleva el destino.</b> Un chiste solo al final no lleva a ning&uacute;n lado.</li>
      <li><b>El pedido de comentario no va al final.</b> Va en el caption o como pregunta al principio.
        Si compite con el destino, pierden los dos.</li>
      <li><b>Dos versiones de la placa.</b> En Shorts el espectador ya est&aacute; en YouTube: decirle
        &laquo;en YouTube&raquo; suena raro.</li>
    </ol>
    <p class="answer">En TikTok e Instagram el link no va adentro del video, as&iacute; que la bio de las dos
      cuentas lleva el link al canal desde el primer d&iacute;a. Y el nombre de usuario tiene que ser el mismo
      en las tres: mucha gente no hace clic en la bio, busca el nombre.</p>
  </div>
</div>

<div class="tw fit" style="margin-top:14px">
  <table>
    <thead><tr><th>Video</th><th>La l&iacute;nea hablada al final</th><th>Para el caption o el principio</th></tr></thead>
    <tbody>
      <tr><th>An iPhone built with 1960s tech</th>
        <td>The answer is one and a half Manhattans. The whole thing is on the channel</td>
        <td>Guess how big. Comment before you watch</td></tr>
      <tr><th>They understand The Internet</th>
        <td>Meet your boss. The full episode is on the channel</td>
        <td>Who decides what you see? Fight us in the comments</td></tr>
      <tr><th>SUPER SENIORS <span class="sublabel">Sin voz, solo la placa</span></th>
        <td class="z">&mdash;</td>
        <td>Which power would you pick?</td></tr>
      <tr><th>Why Are People Afraid of This?</th>
        <td>There&rsquo;s nine more minutes of this on the channel</td>
        <td>Tell us the dumbest thing you&rsquo;re afraid of</td></tr>
      <tr><th>Gravity undo</th>
        <td>Who dies last? The answer is in the full episode</td>
        <td>Try it: circle with one hand, square with the other. Tell us how it went</td></tr>
    </tbody>
  </table>
</div>
<p class="pie">Nunca &laquo;subscribe&raquo;: pide algo sin haber dado nada y en una cuenta nueva suena
a desesperaci&oacute;n.</p>

<h2>D&oacute;nde va la plata</h2>
<div class="split">
  <div class="tw fit">
    <table>
      <thead><tr><th>Destino</th><th class="n">Por semana</th><th class="n">Reparto</th>
        <th class="n">Inversi&oacute;n del trimestre</th></tr></thead>
      <tbody>
        <tr><th>La pieza que mejor anduvo <span class="sublabel">60%</span></th>
          <td class="n next">$150</td><td class="n next">$50 en cada red</td>
          <td class="n next">$1.500</td></tr>
        <tr><th>Las otras cuatro <span class="sublabel">40%</span></th>
          <td class="n next">$100</td><td class="n next">$25 cada una</td>
          <td class="n next">$1.000</td></tr>
        <tr class="sumrow"><th>Total</th><td class="n next">$250</td>
          <td class="n next">$1.000 por mes</td><td class="n next">$2.500</td></tr>
      </tbody>
    </table>
  </div>
  <div class="card">
    <h4>C&oacute;mo se reparte cada semana</h4>
    <ol class="steps">
      <li><b>Las cinco salen sin plata.</b> A las 48 horas ya se ve cu&aacute;l se mueve sola.</li>
      <li><b>El 60% va a esa pieza:</b> $50 en cada una de las tres redes, la misma semana.</li>
      <li><b>El 40% se reparte en las otras cuatro:</b> $25 cada una, en la red donde mejor anduvo.</li>
      <li><b>A los siete d&iacute;as</b> se anota el costo por seguidor y se compara.</li>
    </ol>
    <p class="answer">La ganadora lleva el mismo monto en las tres redes, as&iacute; el costo por
      seguidor compara redes y no videos. El 40% restante existe para que ninguna pieza quede sin
      una sola oportunidad de empuje.</p>
  </div>
</div>

<h2>Las dos primeras semanas</h2>
<div class="split">
  <div class="tw fit">
    <table>
      <thead><tr><th>Cu&aacute;ndo</th><th class="n">Publicaciones</th><th class="n">Pauta</th></tr></thead>
      <tbody>
        <tr><th>D&iacute;a 1
          <span class="sublabel">Tres piezas, separadas cuatro horas, para que el perfil no nazca vac&iacute;o</span></th>
          <td class="n next">3</td><td class="n z">&mdash;</td></tr>
        <tr><th>Resto de la semana 1
          <span class="sublabel">Una por d&iacute;a</span></th>
          <td class="n next">4</td><td class="n z">&mdash;</td></tr>
        <tr><th>Semana 2
          <span class="sublabel">Una por d&iacute;a h&aacute;bil</span></th>
          <td class="n next">5</td><td class="n z">&mdash;</td></tr>
        <tr class="sumrow"><th>Desde la semana 2</th>
          <td class="n next">5 por semana</td><td class="n next">$250 repartidos 60/40</td></tr>
      </tbody>
    </table>
  </div>
  <div class="card">
    <h4>Por qu&eacute; no se pone plata antes</h4>
    <ol class="steps">
      <li><b>El perfil tiene que verse vivo.</b> El que hace clic en un anuncio y cae en una cuenta con
        dos piezas no se queda. Con nueve publicadas ya hay grilla.</li>
      <li><b>El sistema de anuncios necesita se&ntilde;al.</b> Sin datos org&aacute;nicos no tiene hacia d&oacute;nde
        optimizar y gasta a ciegas.</li>
      <li><b>A las 48 horas ya se sabe</b> qu&eacute; pieza se mueve sola. Poner la plata detr&aacute;s de esa
        rinde mucho m&aacute;s que repartirla a ciegas el d&iacute;a que sale.</li>
    </ol>
    <p class="answer">Nunca m&aacute;s de dos publicaciones el mismo d&iacute;a, y siempre con cuatro horas
      de distancia: si no, compiten entre ellas por la misma primera ronda de espectadores.</p>
  </div>
</div>

<h2>&iquest;Qu&eacute; queremos conseguir?</h2>
<div class="objbar">
  <button class="obj on" type="button" data-o="1">Realista</button>
  <button class="obj" type="button" data-o="2">Bueno</button>
  <button class="obj" type="button" data-o="3">Excelente</button>
</div>
<div class="grand" id="obj">
  <div><span>Publicaciones</span><b class="vtot">60</b></div>
  <div><span>Posteos en las tres redes</span><b class="vtot">180</b></div>
  <div><span>Videos de YouTube</span><b class="vtot">11</b></div>
  <div><span>Vistas en el trimestre</span><b class="vnext"
    data-o1="~1.100.000" data-o2="~1.600.000" data-o3="~2.500.000">~1.100.000</b></div>
  <div><span>Suscriptores nuevos</span><b class="vnext"
    data-o1="~7.800" data-o2="~11.000" data-o3="~17.500">~7.800</b></div>
</div>

<p class="pie">Estos n&uacute;meros son una <b>hip&oacute;tesis para validar</b>, no una meta
  comprometida. Todav&iacute;a no sabemos c&oacute;mo convierte esta audiencia: cu&aacute;nta gente que ve
  un corto termina suscribi&eacute;ndose al canal. Esta tanda de publicaciones existe para averiguarlo.
  Con ese dato, los n&uacute;meros de arriba se confirman o se corrigen.</p>

<h2>Estrategias para generar mec&aacute;nicas virales</h2>
<div class="cols2">
  <div class="card">
    <h4>Videos de YouTube<span class="who">Federico Heller</span></h4>
    <ul>
      <li>Un presentador recurrente</li>
      <li>Thumbnails hiper estrat&eacute;gicos</li>
      <li>Hook en los primeros 15 segundos</li>
      <li>Formato de 2 minutos</li>
      <li>Prueba A/B con la velocidad a 1,1&times;</li>
      <li><b>Call to action:</b> pedir comentarios, no suscripciones</li>
    </ul>
  </div>
  <div class="card">
    <h4>Shorts, Reels y TikToks<span class="who">Santiago Tereso</span></h4>
    <ul>
      <li><b>Desde el pr&oacute;ximo video:</b> un presentador interactuando con las
        animaciones</li>
      <li>Un trailer por video largo, no varios recortes</li>
      <li>Hook en los primeros 3 segundos</li>
      <li>La misma pieza en las tres plataformas</li>
      <li>Voz en off uniforme entre todos</li>
      <li><b>Call to action:</b> ver el episodio completo</li>
    </ul>
  </div>
</div>

<h2>Lo que ya publicamos</h2>
<div class="cols4">__CARDS__</div>
<p class="pie">561 suscriptores hoy. Cada vista cost&oacute; $0,007 y 1 de cada 100 se suscribi&oacute;.
De ah&iacute; salen todos los n&uacute;meros que vienen.</p>

<h2>Con pauta</h2>
<div class="split">
  <div class="tw fit">
    <table>
      <thead><tr><th>Pauta</th><th class="n">Vistas en el trimestre</th>
        <th class="n">Suscriptores en el trimestre</th></tr></thead>
      <tbody>
        <tr class="sumrow"><th>$1.000 por mes
          <span class="sublabel">$2.500 hasta fin de a&ntilde;o &middot; el plan actual</span></th>
          <td class="n">~250.000</td><td class="n">~2.500</td></tr>
        <tr><th>$3.000 por mes <span class="sublabel">$9.000 en los tres meses</span></th>
          <td class="n">~900.000</td><td class="n">~9.000</td></tr>
        <tr><th>$5.000 por mes <span class="sublabel">$15.000 en los tres meses</span></th>
          <td class="n">~1.500.000</td><td class="n">~15.000</td></tr>
        <tr class="hip"><th>$33.000 por mes
          <span class="sublabel">$100.000 en los tres meses &middot; para llegar a 100.000 suscriptores</span></th>
          <td class="n">~10.000.000</td><td class="n">100.000</td></tr>
      </tbody>
    </table>
  </div>
  <div class="card">
    <h4>C&oacute;mo se reparte cada semana</h4>
    <ol class="steps">
      <li><b>$1.000 por mes</b>, $250 por semana.</li>
      <li><b>$150 a la pieza que anduvo</b> y $100 repartidos en las otras cuatro.</li>
      <li><b>Al mes se compara</b> y la red que rinde se queda con m&aacute;s plata.</li>
    </ol>
  </div>
</div>

<div class="aviso">
  <p><b>Ojo con estos n&uacute;meros.</b> Salen de suponer que cada vista cuesta $0,01, y ese precio
    lo medimos con campa&ntilde;as sin segmentar: trajeron vistas de Kazajist&aacute;n en vez de
    California. Una vista de Estados Unidos cuesta varias veces m&aacute;s, as&iacute; que la tabla de
    arriba es el techo optimista, no la expectativa.</p>
</div>
<div class="tw fit">
  <table>
    <thead><tr><th>Si la vista segmentada a Estados Unidos cuesta&hellip;</th>
      <th class="n">Vistas con $1.000 por mes</th><th class="n">Suscriptores</th></tr></thead>
    <tbody>
      <tr><th>$0,01 <span class="sublabel">lo que supone la tabla de arriba</span></th>
        <td class="n">~250.000</td><td class="n">~2.500</td></tr>
      <tr><th>$0,03</th><td class="n">~83.000</td><td class="n">~830</td></tr>
      <tr><th>$0,05</th><td class="n">~50.000</td><td class="n">~500</td></tr>
    </tbody>
  </table>
</div>
<p class="pie">Cu&aacute;l de las tres es la real lo sabemos la semana que viene, con la primera
campa&ntilde;a segmentada a Estados Unidos. Hasta entonces, cualquier n&uacute;mero de
suscriptores comprados es una estimaci&oacute;n.</p>

<h2>Org&aacute;nico + pauta</h2>
<div class="tw fit">
  <table>
    <thead><tr><th>Si pasa esto</th><th class="n">Vistas acumuladas &middot; oct a dic</th>
      <th class="n">Suscriptores &middot; oct a dic</th></tr></thead>
    <tbody>
      <tr><th>Una vez: un video con 40k vistas y un short con 150k</th>
        <td class="n next">190.000</td><td class="n next">850</td></tr>
      <tr><th>Se repite 3 veces de ac&aacute; a fin de a&ntilde;o
          <span class="sublabel">Un resultado realista con 11 videos y 60 publicaciones</span></th>
        <td class="n next">570.000</td><td class="n next">2.550</td></tr>
      <tr class="sumrow"><th>Y encima, los $250 por semana</th>
        <td class="n next">~820.000</td><td class="n next">~5.050</td></tr>
      <tr class="goal"><th>Un video se dispara y empuja a todos los dem&aacute;s
          <span class="chip chip--goal">Objetivo</span></th>
        <td class="n next">~1.100.000</td><td class="n next">~7.800</td></tr>
      <tr class="hip"><th>Se vuelve viral</th>
        <td class="n">~10.000.000 en un video</td><td class="n">100.000</td></tr>
    </tbody>
  </table>
</div>
<p class="pie">La pauta pone 250.000 de ese mill&oacute;n. El resto lo ponen las publicaciones y las recomendaciones.</p>

<h2>C&oacute;mo se sostiene un canal</h2>
<div class="nota">
  <p>Los canales grandes viven de conseguir <span class="hl">marcas</span> y
    <span class="hl">sponsors</span> de su nicho. Mientras la plata salga del owner,
    YouTube nunca devuelve m&aacute;s de lo que cuesta.</p>
</div>

<h2>Calendario</h2>
<div class="legend">
  <span><span class="chip chip--short">5</span> &nbsp;Publicaciones por semana, a las tres redes</span>
  <span><span class="chip chip--ent">5 trailers</span> &nbsp;Lo que hay que tener listo</span>
  <span><span class="chip chip--pub">V05</span> &nbsp;El video largo, los viernes</span>
</div>
<div class="tw">
  <table class="cal">
    <thead><tr><th>Semana del</th>__HEAD_DIA__</tr></thead>
    <tbody>
      <tr><th>Entrega</th>__FILA_PROD__</tr>
      <tr><th>Publicaciones</th>__FILA_POST__</tr>
      <tr><th>Pauta</th>__FILA_PAUTA__</tr>
      <tr><th>Video</th>__FILA_VIDEO__</tr>
    </tbody>
  </table>
</div>

<h2>Budget</h2>
<div id="budwrap">
  <div class="budbar"><button id="budtoggle" type="button">Mostrar abril a septiembre</button></div>
  <div class="tw">
    <table>
      <thead><tr><th>Concepto</th>
        <th class="n p">Abr</th><th class="n p">May</th><th class="n p">Jun</th>
        <th class="n p">Jul</th><th class="n p">Ago</th><th class="n p">Sep</th>
        <th class="n hoy">Oct</th><th class="n">Nov</th><th class="n">Dic</th></tr></thead>
      <tbody>
        <tr><th>Federico Heller <span class="sublabel">1/3 de su sueldo</span></th>
          <td class="n past p">$5.000</td><td class="n past p">$6.000</td><td class="n past p">$6.000</td>
          <td class="n past p">$12.000</td><td class="n z p">&mdash;</td><td class="n past p">$2.000</td>
          <td class="n next hoy">$4.000</td><td class="n next">$4.000</td><td class="n next">$4.000</td></tr>
        <tr><th>Santiago Tereso <span class="sublabel">1/4 de su sueldo</span></th>
          <td class="n z p">&mdash;</td><td class="n z p">&mdash;</td><td class="n z p">&mdash;</td>
          <td class="n z p">&mdash;</td><td class="n z p">&mdash;</td><td class="n z p">&mdash;</td>
          <td class="n next hoy">$1.500</td><td class="n next">$1.500</td><td class="n next">$1.500</td></tr>
        <tr class="only-open"><th>AT team</th>
          <td class="n z p">&mdash;</td><td class="n z p">&mdash;</td><td class="n z p">&mdash;</td>
          <td class="n past p">$750</td><td class="n past p">$3.000</td><td class="n z p">&mdash;</td>
          <td class="n z hoy">&mdash;</td><td class="n z">&mdash;</td><td class="n z">&mdash;</td></tr>
        <tr><th>Pauta <span class="sublabel">$250 por semana &middot; tope de $1.000 por mes</span></th>
          <td class="n z p">&mdash;</td><td class="n z p">&mdash;</td><td class="n z p">&mdash;</td>
          <td class="n z p">&mdash;</td><td class="n z p">&mdash;</td><td class="n z p">&mdash;</td>
          <td class="n next hoy">$500</td><td class="n next">$1.000</td><td class="n next">$1.000</td></tr>
        <tr><th>Tools <span class="sublabel">Higgsfield, Suno, ElevenLabs, CapCut</span></th>
          <td class="n z p">&mdash;</td><td class="n z p">&mdash;</td><td class="n z p">&mdash;</td>
          <td class="n z p">&mdash;</td><td class="n z p">&mdash;</td><td class="n z p">&mdash;</td>
          <td class="n next hoy">$392</td><td class="n next">$392</td><td class="n next">$392</td></tr>
        <tr class="sumrow"><th>Total por mes</th>
          <td class="n past p">$5.000</td><td class="n past p">$6.000</td><td class="n past p">$6.000</td>
          <td class="n past p">$13.000</td><td class="n past p">$3.000</td><td class="n past p">$2.000</td>
          <td class="n next hoy">$6.392</td><td class="n next">$6.892</td><td class="n next">$6.892</td></tr>
      </tbody>
    </table>
  </div>
  <div class="grand">
    <div class="only-open"><span>Ya gastado &middot; abr a sep</span><b class="vpast">$34.413</b></div>
    <div><span>Inversi&oacute;n &middot; oct a dic</span><b class="vnext">$20.176</b></div>
    <div class="only-open"><span>Total del a&ntilde;o</span><b class="vtot">$54.589</b></div>
  </div>
</div>
<p class="pie">Pedido aparte, todav&iacute;a sin aprobar: <b>$7.000</b> hasta fin de a&ntilde;o para anuncios y herramientas, en dos pagos, para que la cuenta de la oficina deje de quedar en descubierto.</p>

</div>

<script>
(function(){
  "use strict";
  var objs = [].slice.call(document.querySelectorAll(".obj")),
      cifras = [].slice.call(document.querySelectorAll("#obj [data-o1]"));
  objs.forEach(function(b){
    b.addEventListener("click", function(){
      var n = b.getAttribute("data-o");
      cifras.forEach(function(c){ c.textContent = c.getAttribute("data-o" + n); });
      objs.forEach(function(x){ x.classList.toggle("on", x === b); });
    });
  });
  var bw = document.getElementById("budwrap"),
      bt = document.getElementById("budtoggle");
  if (bw && bt) bt.addEventListener("click", function(){
    var open = bw.classList.toggle("open");
    bt.textContent = open ? "Ocultar abril a septiembre" : "Mostrar abril a septiembre";
  });
})();
</script>
"""
for k, v in [(u"__N_SEM__", str(len(semanas))), (u"__HEAD_DIA__", head_dia),
             (u"__FILA_VIDEO__", fila_video), (u"__FILA_POST__", fila_post),
             (u"__FILA_PAUTA__", fila_pauta), (u"__FILA_PROD__", fila_prod),
             (u"__LOGO__", LOGO), (u"__CARDS__", cards)]:
    HTML = HTML.replace(k, v)
io.open(OUT, "w", encoding="utf-8").write(HTML)
print(u"escrito %s | %d KB | %d semanas, %d publicaciones, %d videos" % (
    OUT, len(HTML) // 1024, len(semanas), len(semanas) * 5, len(viernes)))
