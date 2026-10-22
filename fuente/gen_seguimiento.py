# -*- coding: utf-8 -*-
"""Seguimiento: un hub con el resumen de las tres redes y una pagina por red.

Escribe seguimiento/index.html, seguimiento/youtube/, /tiktok/ y /instagram/
directo en el repo. Los numeros de YouTube salen de Analytics y de Google Ads;
TikTok e Instagram esperan los screenshots.
"""
import datetime, io, json, os

SITE = u"https://santiagotereso.github.io/brain-syrup/"
AQUI = os.path.dirname(os.path.abspath(__file__))
_padre = os.path.dirname(AQUI)
REPO = (_padre if os.path.isdir(os.path.join(_padre, "posteos"))
        else os.path.join(os.path.expanduser("~"), "SHIET", "brain-syrup"))
LOGO = json.load(io.open("_assets.json", encoding="utf-8"))["logo"]

MESES = [u"enero", u"febrero", u"marzo", u"abril", u"mayo", u"junio", u"julio",
         u"agosto", u"septiembre", u"octubre", u"noviembre", u"diciembre"]
_h = datetime.datetime.now()
FECHA = u"%d de %s de %d, %02d:%02d" % (_h.day, MESES[_h.month - 1], _h.year, _h.hour, _h.minute)

# ---------------------------------------------------------------- datos
#
# Los numeros no viven aca: viven en datos/*.json, uno por red, para que dos
# computadoras puedan actualizar redes distintas sin pisarse.
#   datos/youtube.json    <- la maquina principal, "Actualizar Brain Syrup.bat"
#   datos/instagram.json  <- la de Los Angeles, "Actualizar Instagram.bat"
#   datos/tiktok.json     <- a mano, desde screenshots

def cargar(nombre):
    return json.load(io.open(os.path.join(AQUI, "datos", nombre + ".json"), encoding="utf-8"))

_yt, _ig, _tt = cargar("youtube"), cargar("instagram"), cargar("tiktok")

YT_SHORTS = [(s["id"], s["titulo"], s["corto"], s["dur"], s["costo"], s["vistas"],
              s["pago"], s["media"], s["visto"], s["subs"], s["likes"]) for s in _yt["shorts"]]
YT_GASTADO, YT_PRES = _yt["gastado"], _yt["presupuesto"]
YT_PAIS = [(p["nombre"], p["vistas"], p["pct"]) for p in _yt["paises"]]
YT_VIDEOS = [(v["id"], v["titulo"], v["dur"], v["vistas"], v["pago"],
              v["media"], v["visto"], v["subs"], v["likes"]) for v in _yt["episodios"]]

TT_VIDEOS = [(v["id"], v["titulo"], v["corto"], v["dur"], v["vistas"],
              v["media"], v["full"], v["seg"], v["inter"]) for v in _tt["videos"]]
TT_GASTADO, TT_PERFIL = _tt["gastado"], _tt["visitas_perfil"]
TT_PAIS = [(p["nombre"], p["pct"]) for p in _tt["paises"]]

IG_VIDEOS = [(v["id"], v["titulo"], v["corto"], v["dur"], v["vistas"], v["pagas"],
              v["gasto"], v["perfil"], v["seg"], v["inter"]) for v in _ig["reels"]]
IG_PRES = _ig["presupuesto_por_reel"]
IG_PAIS = [(p["nombre"], p["pct"]) for p in _ig["paises"]]

REDES = [
 (u"youtube-shorts", u"YouTube Shorts", u"%d shorts" % len(YT_SHORTS)),
 (u"tiktok",         u"TikTok",         u"%d posteos" % len(TT_VIDEOS)),
 (u"instagram",      u"Instagram",      u"%d reels" % len(IG_VIDEOS)),
 (u"youtube-videos", u"YouTube Videos", u"%d episodios" % len(YT_VIDEOS)),
]


# ---------------------------------------------------------------- formato

def mil(n):
    return u"{:,}".format(int(n)).replace(u",", u".")

def usd(x):
    return u"USD&nbsp;" + (u"%.2f" % x).replace(u".", u",")

def pc(x):
    return (u"%.1f" % x).replace(u".", u",") + u"%"

CSS = u'''
:root{
  color-scheme:dark;
  --bg:#0F1418; --panel:#161D23; --panel2:#111920;
  --line:#242E36; --line2:#38454F;
  --ink:#E7EDF2; --ink2:#AFBCC7; --dim:#7A8995;
  --teal:#2DD4BF; --blue:#93B4FD; --warn:#E9B949; --past:#8A98A5;
  --ui:"Inter","Segoe UI",system-ui,-apple-system,Helvetica,Arial,sans-serif;
  --mono:'JetBrains Mono',ui-monospace,Consolas,monospace;
}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--ui);font-size:15px;
  line-height:1.5;-webkit-font-smoothing:antialiased}
.app{max-width:1600px;margin:0 auto;padding:20px 20px 64px}
.mono{font-family:var(--mono);font-variant-numeric:tabular-nums}

header{display:flex;align-items:center;gap:22px;flex-wrap:wrap;padding-bottom:20px;
  border-bottom:1px solid var(--line)}
.logo{flex:none;width:88px;height:88px;border-radius:50%;display:block}
h1{margin:0;font-size:clamp(30px,4.2vw,46px);font-weight:800;letter-spacing:-.03em;line-height:1.02}
.h1b{color:var(--teal)}
.kicker{font-size:12.5px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;
  color:var(--teal);margin:0 0 10px}
.nav{margin-left:auto;display:flex;gap:8px;flex-wrap:wrap}
.tab{text-decoration:none;border:1px solid var(--line2);color:var(--dim);font-size:13.5px;
  font-weight:600;padding:8px 16px;border-radius:999px;white-space:nowrap}
.tab:hover{color:var(--ink);border-color:var(--teal)}
.tab.on{background:var(--teal);border-color:var(--teal);color:#06211E}

h2{font-size:21px;letter-spacing:-.015em;color:var(--ink);font-weight:700;margin:40px 0 14px;
  display:flex;align-items:center;gap:14px}
h2::after{content:"";flex:1;height:1px;background:var(--line)}

.grand{display:flex;flex-wrap:wrap;border:1px solid var(--line);border-radius:10px;
  background:var(--panel);overflow:hidden}
.grand div{flex:1;min-width:190px;padding:16px 20px;border-right:1px solid var(--line)}
.grand div:last-child{border-right:0}
.grand span{display:block;font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--dim)}
.grand b{display:block;font-size:24px;font-weight:800;letter-spacing:-.02em;margin-top:4px;
  font-variant-numeric:tabular-nums}
.grand .vteal{color:var(--teal)} .grand .vink{color:var(--ink)} .grand .vdim{color:var(--past)}

.tw{overflow-x:auto;border:1px solid var(--line);border-radius:10px;background:var(--panel)}
table{border-collapse:collapse;width:100%;font-size:14px}
th,td{text-align:left;padding:10px 12px;border-bottom:1px solid var(--line);white-space:nowrap}
thead th{font-size:11px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--dim);
  background:var(--panel2)}
tbody tr:last-child td{border-bottom:0}
td.n,th.n{text-align:right;font-variant-numeric:tabular-nums}
.win{color:var(--teal)}
.sub{display:block;font-size:11.5px;color:var(--dim);margin-top:2px}

td.vid{white-space:normal;min-width:300px}
td.vid img{float:left;width:52px;height:92px;object-fit:cover;border-radius:6px;
  border:1px solid var(--line2);margin-right:12px}
td.vid.w img{width:112px;height:63px}
td.vid span{display:block;overflow:hidden}
td.vid b{color:var(--ink);font-weight:600}
.mbar{display:block;height:5px;border-radius:3px;background:var(--line2);margin:6px 0 2px;overflow:hidden}
.mbar i{display:block;height:100%;background:var(--teal)}
tr.tot td{background:var(--panel2);font-weight:700;border-top:1px solid var(--line2)}
tr.tot td.vid b{font-weight:800}
.mal{color:var(--warn)}
.stamp{margin-left:auto;font-size:12px;color:var(--dim);font-family:var(--mono);white-space:nowrap}

.redes{display:flex;gap:14px;flex-wrap:wrap;margin-top:18px}
.red{flex:1;min-width:240px;text-decoration:none;display:block;padding:22px 24px;
  border:1px solid var(--line2);border-radius:12px;background:var(--panel);color:var(--ink)}
.red:hover{border-color:var(--teal);background:var(--panel2)}
.red b{display:block;font-size:26px;font-weight:800;letter-spacing:-.02em}
.red span{display:block;font-size:12px;letter-spacing:.08em;text-transform:uppercase;
  color:var(--dim);margin-top:6px}
.red em{display:block;font-style:normal;color:var(--teal);font-weight:700;font-size:13.5px;margin-top:14px}

.pie{font-size:16.5px;line-height:1.55;color:var(--ink2);margin:12px 0 0}
.espera{margin:0;padding:22px 26px;border:1px solid var(--line);border-left:3px solid var(--warn);
  border-radius:10px;background:var(--panel)}
.espera p{margin:0;font-size:18px;line-height:1.5;color:var(--ink)}
.espera ul{margin:12px 0 0;padding-left:20px;color:var(--ink2);font-size:16px}
.espera li{margin-top:4px}

@media (max-width:700px){ .grand div{min-width:150px} }
'''

NAV_PAGS = [(u"Objetivo", u""), (u"Seguimiento", u"seguimiento/"), (u"Videos", u"videos/"),
            (u"Picadora", u"picadora/"), (u"Cuentas", u"cuentas/"),
            (u"Mejor call to action", u"cta/"), (u"Posteos", u"posteos/"),
            (u"Material de estudio", u"referencias/")]

def nav():
    o = []
    for nm, sub in NAV_PAGS:
        on = u" on" if nm == u"Seguimiento" else u""
        ac = u' aria-current="page"' if nm == u"Seguimiento" else u""
        o.append(u'    <a class="tab%s" href="%s%s"%s>%s</a>' % (on, SITE, sub, ac, nm))
    return u'  <nav class="nav">\n%s\n  </nav>' % u"\n".join(o)

def subnav(act):
    o = [u'<a class="tab%s" href="%sseguimiento/">Resumen</a>'
         % (u" on" if act == u"" else u"", SITE)]
    for slug, nom, _ in REDES:
        on = u" on" if act == slug else u""
        o.append(u'<a class="tab%s" href="%sseguimiento/%s/">%s</a>' % (on, SITE, slug, nom))
    return (u'<nav class="nav" style="margin:18px 0 0;justify-content:flex-start;align-items:center">'
            u'%s<span class="stamp">Le&iacute;do el %s</span></nav>' % (u"".join(o), FECHA))

def pagina(titulo, h1b, act, cuerpo):
    return u'''<!doctype html>
<html lang="es">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%s</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap">
<style>%s</style>

<div class="app">

<header>
  <img class="logo" src="%s" alt="Logo de Brain Syrup">
  <div class="id">
    <p class="kicker">Seguimiento</p>
    <h1>Brain Syrup <span class="h1b">%s</span></h1>
  </div>
%s
</header>

%s

%s

</div>
''' % (titulo, CSS, LOGO, h1b, nav(), subnav(act), cuerpo)

# ---------------------------------------------------------------- YouTube

def youtube():
    filas, tC, tV, tP, tS, tL = [], 0.0, 0, 0, 0, 0
    for vid, tit, corto, dur, costo, vistas, pagoPct, media, visto, subs, likes in YT_SHORTS:
        pagas = int(round(vistas * pagoPct / 100.0))
        organ = vistas - pagas
        tC += costo; tV += vistas; tP += pagas; tS += subs; tL += likes
        cps = usd(costo / subs) if (subs and costo) else u"&mdash;"
        filas.append(u'''      <tr>
        <td class="vid"><img src="%sposteos/media/thumb-%s-sm.webp" alt="">
          <span><b>%s</b><span class="sub">%s &middot; %s</span></span></td>
        <td class="n mono">%s</td>
        <td class="n mono">%s<span class="mbar"><i style="width:%.1f%%"></i></span>
          <span class="sub">%s pagas &middot; %s ganadas</span></td>
        <td class="n mono%s">%s<span class="sub">%s de %s</span></td>
        <td class="n mono">%s</td>
        <td class="n mono">%s</td>
        <td class="n mono">%s</td>
      </tr>''' % (SITE, vid, tit, corto, dur,
                  usd(costo) if costo else u"&mdash;", mil(vistas),
                  (pagas * 100.0 / vistas) if vistas else 0, mil(pagas), mil(organ),
                  u" win" if visto >= 90 else u"", pc(visto), media, dur,
                  mil(subs), mil(likes), cps))
    tO = tV - tP

    pais = u"\n".join(
        u'      <tr><td>%s</td><td class="n mono">%s</td><td class="n mono%s">%s</td></tr>'
        % (nom, mil(v), u" win" if p > 50 else u"", pc(p)) for nom, v, p in YT_PAIS)

    cuerpo = u'''<h2>Lo que compr&oacute; la plata &middot; YouTube</h2>
<div class="grand">
  <div><span>Gastado</span><b class="vteal">%s</b></div>
  <div><span>De un presupuesto de</span><b class="vdim">%s</b></div>
  <div><span>Vistas compradas</span><b class="vink">%s</b></div>
  <div><span>Vistas ganadas solas</span><b class="vteal">%s</b></div>
  <div><span>Suscriptores</span><b class="vink">%s</b></div>
  <div><span>Costo por suscriptor</span><b class="vteal">%s</b></div>
</div>

<div class="tw" style="margin-top:14px">
  <table>
    <thead>
      <tr><th>Video</th><th class="n">Costo</th><th class="n">Vistas</th><th class="n">Visto</th>
        <th class="n">Subs</th><th class="n">Me gusta</th><th class="n">Costo por sub</th></tr>
    </thead>
    <tbody>
%s
      <tr class="tot">
        <td class="vid"><span><b>Los cinco</b><span class="sub">17 y 21 de octubre</span></span></td>
        <td class="n mono">%s</td>
        <td class="n mono">%s<span class="mbar"><i style="width:%.1f%%"></i></span>
          <span class="sub">%s pagas &middot; %s ganadas</span></td>
        <td class="n mono">&mdash;</td>
        <td class="n mono">%s</td>
        <td class="n mono">%s</td>
        <td class="n mono">%s</td>
      </tr>
    </tbody>
  </table>
</div>
<p class="pie">La barra verde es lo que pag&oacute; la pauta; la gris, lo que el video consigui&oacute;
  solo en el feed de Shorts.</p>

<h2>De d&oacute;nde viene el p&uacute;blico</h2>
<div class="tw">
  <table>
    <thead><tr><th>Pa&iacute;s</th><th class="n">Vistas</th><th class="n">Del total</th></tr></thead>
    <tbody>
%s
    </tbody>
  </table>
</div>
''' % (usd(YT_GASTADO), usd(YT_PRES), mil(tP), mil(tO), mil(tS), usd(tC / tS),
       u"\n".join(filas), usd(tC), mil(tV), tP * 100.0 / tV, mil(tP), mil(tO),
       mil(tS), mil(tL), usd(tC / tS), pais)
    return cuerpo, {"gastado": tC, "vistas": tV, "seg": tS}

# ---------------------------------------------------------------- videos largos

def videos():
    filas, tV, tP, tS, tL = [], 0, 0, 0, 0
    for vid, tit, dur, vistas, pagoPct, media, visto, subs, likes in YT_VIDEOS:
        pagas = int(round(vistas * pagoPct / 100.0))
        organ = vistas - pagas
        tV += vistas; tP += pagas; tS += subs; tL += likes
        porSub = mil(round(pagas / float(subs))) if subs else u"&mdash;"
        filas.append(u'''      <tr>
        <td class="vid w"><img src="%sposteos/media/yt-%s.webp" alt="">
          <span><b>%s</b><span class="sub">%s</span></span></td>
        <td class="n mono">%s<span class="mbar"><i style="width:%.1f%%"></i></span>
          <span class="sub">%s pagas &middot; %s ganadas</span></td>
        <td class="n mono">%s<span class="sub">%s de %s</span></td>
        <td class="n mono">%s</td>
        <td class="n mono">%s</td>
        <td class="n mono">%s</td>
      </tr>''' % (SITE, vid, tit, dur, mil(vistas), pagoPct,
                  mil(pagas), mil(organ), pc(visto), media, dur,
                  mil(subs), mil(likes), porSub))
    tO = tV - tP

    return u'''<h2>Lo que compr&oacute; la plata &middot; YouTube Videos</h2>
<div class="grand">
  <div><span>Gastado</span><b class="vdim">No visible</b></div>
  <div><span>Vistas compradas</span><b class="vink">%s</b></div>
  <div><span>Vistas ganadas solas</span><b class="vteal">%s</b></div>
  <div><span>Suscriptores</span><b class="vink">%s</b></div>
  <div><span>Vistas pagas por suscriptor</span><b class="vteal">%s</b></div>
</div>
<p class="pie">Estas campa&ntilde;as se corrieron desde otra cuenta de Google&nbsp;Ads, as&iacute; que el monto no
  se ve desde ac&aacute;. En cuanto nos pasen la cifra, esta fila se completa y el costo por suscriptor
  sale solo.</p>

<div class="tw" style="margin-top:14px">
  <table>
    <thead>
      <tr><th>Episodio</th><th class="n">Vistas</th><th class="n">Visto</th>
        <th class="n">Subs</th><th class="n">Me gusta</th><th class="n">Vistas pagas por sub</th></tr>
    </thead>
    <tbody>
%s
      <tr class="tot">
        <td class="vid w"><span><b>Los cinco</b><span class="sub">septiembre y octubre</span></span></td>
        <td class="n mono">%s<span class="mbar"><i style="width:%.1f%%"></i></span>
          <span class="sub">%s pagas &middot; %s ganadas</span></td>
        <td class="n mono">&mdash;</td>
        <td class="n mono">%s</td>
        <td class="n mono">%s</td>
        <td class="n mono">%s</td>
      </tr>
    </tbody>
  </table>
</div>
<p class="pie">Cada suscriptor del canal cost&oacute; %s vistas pagas en los episodios largos. En los
  shorts cost&oacute; 559. La misma plata rinde dos veces y media m&aacute;s en shorts.</p>
''' % (mil(tP), mil(tO), mil(tS), mil(round(tP / float(tS))),
       u"\n".join(filas), mil(tV), tP * 100.0 / tV, mil(tP), mil(tO),
       mil(tS), mil(tL), mil(round(tP / float(tS))), mil(round(tP / float(tS))))

# ---------------------------------------------------------------- pendientes

def seg(x):
    return (u"%.2f" % x).replace(u".", u",") + u"&nbsp;s"

def tiktok():
    filas, tV, tS, tI = [], 0, 0, 0
    for vid, tit, corto, dur, vistas, media, full, segs, inter in TT_VIDEOS:
        tV += vistas; tS += segs; tI += inter
        filas.append(u'''      <tr>
        <td class="vid"><img src="%sposteos/media/thumb-%s-sm.webp" alt="">
          <span><b>%s</b><span class="sub">%s &middot; %s</span></span></td>
        <td class="n mono">%s</td>
        <td class="n mono%s">%s<span class="sub">de %s</span></td>
        <td class="n mono">%s</td>
        <td class="n mono">%s</td>
        <td class="n mono">%s</td>
      </tr>''' % (SITE, vid, tit, corto, dur, mil(vistas),
                  u"" if media >= 5 else u" mal", seg(media) if vistas else u"&mdash;", dur,
                  pc(full) if vistas else u"&mdash;", mil(segs), mil(inter)))

    pais = u"\n".join(u'      <tr><td>%s</td><td class="n mono%s">%s</td></tr>'
                      % (nom, u" win" if p > 50 else u"", pc(p)) for nom, p in TT_PAIS)

    return u'''<h2>Lo que compr&oacute; la plata &middot; TikTok</h2>
<div class="grand">
  <div><span>Gastado</span><b class="vteal">%s</b></div>
  <div><span>Vistas</span><b class="vink">%s</b></div>
  <div><span>Visitas al perfil</span><b class="vink">%s</b></div>
  <div><span>Seguidores</span><b class="vink">%s</b></div>
  <div><span>Costo por seguidor</span><b class="vteal">%s</b></div>
</div>
<p class="pie">Una sola promoci&oacute;n, cerrada el 21 de octubre. La app no abre el gasto por video,
  as&iacute; que la columna de costo va solo en el total.</p>

<div class="tw" style="margin-top:14px">
  <table>
    <thead>
      <tr><th>Video</th><th class="n">Vistas</th><th class="n">Vista media</th>
        <th class="n">Vio completo</th><th class="n">Seguidores</th><th class="n">Interacciones</th></tr>
    </thead>
    <tbody>
%s
      <tr class="tot">
        <td class="vid"><span><b>Los cinco</b><span class="sub">%s gastados</span></span></td>
        <td class="n mono">%s</td>
        <td class="n mono">&mdash;</td>
        <td class="n mono">&mdash;</td>
        <td class="n mono">%s</td>
        <td class="n mono">%s</td>
      </tr>
    </tbody>
  </table>
</div>
<p class="pie">Los dos de arriba son los que recibieron la promoci&oacute;n: juntaron 2.651 vistas que
  duraron poco m&aacute;s de un segundo cada una. Los dos de abajo no recibieron nada y casi no se
  mostraron, pero a los que llegaron se quedaron entre 8 y 21 segundos.</p>

<h2>De d&oacute;nde viene el p&uacute;blico</h2>
<div class="tw">
  <table>
    <thead><tr><th>Pa&iacute;s</th><th class="n">Del total</th></tr></thead>
    <tbody>
%s
    </tbody>
  </table>
</div>
''' % (usd(TT_GASTADO), mil(tV), mil(TT_PERFIL), mil(tS),
       usd(TT_GASTADO / tS) if tS else u"&mdash;",
       u"\n".join(filas), usd(TT_GASTADO), mil(tV), mil(tS), mil(tI), pais)


def instagram():
    filas, tV, tP, tG, tPerf, tS, tI = [], 0, 0, 0.0, 0, 0, 0
    for vid, tit, corto, dur, vistas, pagas, gasto, perf, segs, inter in IG_VIDEOS:
        organ = vistas - pagas
        tV += vistas; tP += pagas; tG += gasto; tPerf += perf; tS += segs; tI += inter
        cps = usd(gasto / segs) if (segs and gasto) else u"&mdash;"
        wp = (pagas * 100.0 / vistas) if vistas else 0
        filas.append(u'''      <tr>
        <td class="vid"><img src="%sposteos/media/thumb-%s-sm.webp" alt="">
          <span><b>%s</b><span class="sub">%s &middot; %s</span></span></td>
        <td class="n mono">%s</td>
        <td class="n mono">%s<span class="mbar"><i style="width:%.1f%%"></i></span>
          <span class="sub">%s pagas &middot; %s ganadas</span></td>
        <td class="n mono">%s</td>
        <td class="n mono">%s</td>
        <td class="n mono">%s</td>
        <td class="n mono">%s</td>
      </tr>''' % (SITE, vid, tit, corto, dur,
                  usd(gasto) if gasto else u"&mdash;", mil(vistas), wp,
                  mil(pagas), mil(organ), mil(perf), mil(segs), mil(inter), cps))
    tO = tV - tP

    return u'''<h2>Lo que compr&oacute; la plata &middot; Instagram</h2>
<div class="grand">
  <div><span>Gastado</span><b class="vteal">%s</b></div>
  <div><span>Vistas compradas</span><b class="vink">%s</b></div>
  <div><span>Vistas ganadas solas</span><b class="vteal">%s</b></div>
  <div><span>Visitas al perfil</span><b class="vink">%s</b></div>
  <div><span>Seguidores</span><b class="vink">%s</b></div>
  <div><span>Costo por seguidor</span><b class="vteal">%s</b></div>
</div>
<p class="pie">Cuatro promociones por separado, %s de presupuesto cada una, tres d&iacute;as,
  p&uacute;blico de %s, en Instagram y Facebook.</p>

<div class="tw" style="margin-top:14px">
  <table>
    <thead>
      <tr><th>Reel</th><th class="n">Costo</th><th class="n">Vistas</th>
        <th class="n">Visitas al perfil</th><th class="n">Seguidores</th>
        <th class="n">Interacciones</th><th class="n">Costo por seguidor</th></tr>
    </thead>
    <tbody>
%s
      <tr class="tot">
        <td class="vid"><span><b>Los cinco</b><span class="sub">17 y 21 de octubre</span></span></td>
        <td class="n mono">%s</td>
        <td class="n mono">%s<span class="mbar"><i style="width:%.1f%%"></i></span>
          <span class="sub">%s pagas &middot; %s ganadas</span></td>
        <td class="n mono">%s</td>
        <td class="n mono">%s</td>
        <td class="n mono">%s</td>
        <td class="n mono">%s</td>
      </tr>
    </tbody>
  </table>
</div>
<p class="pie">La barra verde es lo que pag&oacute; la pauta; la gris, lo que el reel consigui&oacute; solo.</p>

<h2>De d&oacute;nde viene el p&uacute;blico</h2>
<div class="tw">
  <table>
    <thead><tr><th>Ubicaci&oacute;n</th><th class="n">Del total</th></tr></thead>
    <tbody>
%s
    </tbody>
  </table>
</div>
<p class="pie">Las promociones se segmentaron a %s, as&iacute; que el p&uacute;blico sale de ah&iacute;.</p>
''' % (usd(tG), mil(tP), mil(tO), mil(tPerf), mil(tS), usd(tG / tS),
       usd(IG_PRES), _ig["ubicacion"], u"\n".join(filas), usd(tG), mil(tV), tP * 100.0 / tV,
       mil(tP), mil(tO), mil(tPerf), mil(tS), mil(tI), usd(tG / tS),
       u"\n".join(u'      <tr><td>%s</td><td class="n mono%s">%s</td></tr>'
                   % (n, u" win" if x > 50 else u"", pc(x)) for n, x in IG_PAIS),
       _ig["ubicacion"])

# ---------------------------------------------------------------- hub

def hub(yt, tt, ig):
    datos = [(u"youtube-shorts", u"YouTube Shorts", yt["gastado"], yt["vistas"], yt["seg"]),
             (u"tiktok", u"TikTok", tt["gastado"], tt["vistas"], tt["seg"]),
             (u"instagram", u"Instagram", ig["gastado"], ig["vistas"], ig["seg"])]
    gT = sum(d[2] for d in datos); vT = sum(d[3] for d in datos); sT = sum(d[4] for d in datos)

    filas = []
    for slug, nom, g, v, s in datos:
        cps = usd(g / s) if (s and g) else u"&mdash;"
        filas.append(u'      <tr><td><b>%s</b></td><td class="n mono">%s</td>'
                     u'<td class="n mono">%s</td><td class="n mono">%s</td>'
                     u'<td class="n mono%s">%s</td></tr>'
                     % (nom, usd(g), mil(v), mil(s), u" win" if (s and g) else u"", cps))

    btns = u"\n".join(
        u'  <a class="red" href="%sseguimiento/%s/"><b>%s</b><span>%s</span>'
        u'<em>Ver el detalle &rarr;</em></a>' % (SITE, slug, nom, det)
        for slug, nom, det in REDES)

    return u'''<h2>Las tres redes</h2>
<div class="grand">
  <div><span>Gastado en total</span><b class="vteal">%s</b></div>
  <div><span>Vistas</span><b class="vink">%s</b></div>
  <div><span>Seguidores sumados</span><b class="vink">%s</b></div>
  <div><span>Costo por seguidor</span><b class="vteal">%s</b></div>
</div>

<div class="tw" style="margin-top:14px">
  <table>
    <thead><tr><th>Red</th><th class="n">Gastado</th><th class="n">Vistas</th>
      <th class="n">Seguidores</th><th class="n">Costo por seguidor</th></tr></thead>
    <tbody>
%s
      <tr class="tot"><td><b>Las tres</b></td><td class="n mono">%s</td>
        <td class="n mono">%s</td><td class="n mono">%s</td><td class="n mono">%s</td></tr>
    </tbody>
  </table>
</div>

<h2>El detalle de cada red</h2>
<div class="redes">
%s
</div>
''' % (usd(gT), mil(vT), mil(sT), usd(gT / sT) if sT else u"&mdash;",
       u"\n".join(filas), usd(gT), mil(vT), mil(sT), usd(gT / sT) if sT else u"&mdash;",
       btns)

# ---------------------------------------------------------------- salida

def escribir(sub, html):
    d = os.path.join(REPO, "seguimiento", sub) if sub else os.path.join(REPO, "seguimiento")
    if not os.path.isdir(d):
        os.makedirs(d)
    p = os.path.join(d, "index.html")
    io.open(p, "w", encoding="utf-8").write(html)
    print(u"%s: %d KB" % (os.path.relpath(p, REPO).replace("\\", "/"), os.path.getsize(p) // 1024))

cuerpoYT, totYT = youtube()
totTT = {"gastado": TT_GASTADO, "vistas": sum(v[4] for v in TT_VIDEOS),
         "seg": sum(v[7] for v in TT_VIDEOS)}
totIG = {"gastado": sum(v[6] for v in IG_VIDEOS), "vistas": sum(v[4] for v in IG_VIDEOS),
         "seg": sum(v[8] for v in IG_VIDEOS)}

escribir("", pagina(u"Seguimiento", u"Seguimiento", u"", hub(totYT, totTT, totIG)))
escribir("youtube-shorts", pagina(u"Seguimiento &middot; YouTube Shorts", u"YouTube Shorts",
                                  u"youtube-shorts", cuerpoYT))
escribir("tiktok", pagina(u"Seguimiento &middot; TikTok", u"TikTok", u"tiktok", tiktok()))
escribir("instagram", pagina(u"Seguimiento &middot; Instagram", u"Instagram", u"instagram",
                             instagram()))
escribir("youtube-videos", pagina(u"Seguimiento &middot; YouTube Videos", u"YouTube Videos",
                                  u"youtube-videos", videos()))
