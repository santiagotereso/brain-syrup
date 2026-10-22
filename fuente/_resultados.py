# -*- coding: utf-8 -*-
"""Mete en Seguimiento el bloque de resultados reales de YouTube: plata por video,
vistas compradas vs. ganadas, retencion y de donde viene el publico."""
import io

P = "seguimiento_src.html"
s = io.open(P, encoding="utf-8").read()

def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70])
    s = s.replace(a, b, 1)

# Analytics al 21/10/2026. Costos de Google Ads al 22/10, campana
# "Shorts - Super Seniors - US - oct 2026" (cuenta 544-426-9582).
V = [
 ("seniors", u"Which power would you pick?", u"Super Seniors", u"0:23",
  19.77, 3921, 50.4, u"0:21", 91.6, 8, 35),
 ("algo", u"This is your boss. Thoughts?", u"Who controls the Internet", u"0:25",
  17.61, 3239, 74.8, u"0:24", 97.0, 1, 18),
 ("gravity", u"Most will last under a minute.", u"Gravity undo", u"0:24",
  8.70, 2003, 41.3, u"0:23", 98.2, 2, 37),
 ("iphone-1960", u"How much space would an iPhone take in 1960?", u"iPhone 1960", u"0:19",
  9.09, 1673, 55.3, u"0:19", 104.5, 0, 13),
 ("gianni", u"He'll multiply your followers. Call 1800-GIANNI", u"1800-GIANNI", u"0:40",
  0.0, 224, 0.0, u"0:13", 33.4, 0, 0),
]

def mil(n):
    return u"{:,}".format(int(n)).replace(u",", u".")

def usd(x):
    return u"USD&nbsp;" + (u"%.2f" % x).replace(u".", u",")

def pc(x):
    return (u"%.1f" % x).replace(u".", u",") + u"%"

filas = []
tC = tV = tP = tS = tL = 0
for vid, tit, corto, dur, costo, vistas, pagoPct, media, visto, subs, likes in V:
    pagas = int(round(vistas * pagoPct / 100.0))
    organ = vistas - pagas
    tC += costo; tV += vistas; tP += pagas; tS += subs; tL += likes
    cps = usd(costo / subs) if (subs and costo) else u"&mdash;"
    costoTxt = usd(costo) if costo else u"&mdash;"
    wp = (pagas * 100.0 / vistas) if vistas else 0
    filas.append(u'''      <tr>
        <td class="vid"><img src="__SITE__posteos/media/thumb-%s-sm.webp" alt="">
          <span><b>%s</b><span class="sub">%s &middot; %s</span></span></td>
        <td class="n mono">%s</td>
        <td class="n mono">%s<span class="mbar"><i style="width:%.1f%%"></i></span>
          <span class="sub">%s pagas &middot; %s ganadas</span></td>
        <td class="n mono%s">%s<span class="sub">%s de %s</span></td>
        <td class="n mono">%s</td>
        <td class="n mono">%s</td>
        <td class="n mono">%s</td>
      </tr>''' % (vid, tit, corto, dur, costoTxt, mil(vistas), wp,
                 mil(pagas), mil(organ),
                 u" win" if visto >= 90 else u"", pc(visto), media, dur,
                 mil(subs), mil(likes), cps))

tO = tV - tP
cpsT = usd(tC / tS)
tabla = u"\n".join(filas)

BLOQUE = u'''
<h2>Lo que compr&oacute; la plata &middot; YouTube</h2>
<p class="pie" style="margin:0 0 14px">Los cinco shorts publicados. Vistas y retenci&oacute;n de YouTube
  Analytics al 21 de octubre; costos de Google&nbsp;Ads al 22. La campa&ntilde;a corri&oacute; del 20 al 23 de
  octubre sobre los cuatro primeros: el quinto se public&oacute; despu&eacute;s y no recibi&oacute; un peso.</p>

<div class="grand">
  <div><span>Gastado</span><b class="vteal">USD&nbsp;55,17</b></div>
  <div><span>De un presupuesto de</span><b class="vdim">USD&nbsp;100</b></div>
  <div><span>Vistas compradas</span><b class="vink">__TP__</b></div>
  <div><span>Vistas ganadas solas</span><b class="vteal">__TO__</b></div>
  <div><span>Suscriptores</span><b class="vink">__TS__</b></div>
  <div><span>Costo por suscriptor</span><b class="vteal">__CPS__</b></div>
</div>

<div class="tw" style="margin-top:14px">
  <table>
    <thead>
      <tr>
        <th>Video</th>
        <th class="n">Costo</th>
        <th class="n">Vistas</th>
        <th class="n">Visto</th>
        <th class="n">Subs</th>
        <th class="n">Me gusta</th>
        <th class="n">Costo por sub</th>
      </tr>
    </thead>
    <tbody>
__FILAS__
      <tr class="tot">
        <td class="vid"><span><b>Los cinco</b><span class="sub">17 y 21 de octubre</span></span></td>
        <td class="n mono">USD&nbsp;55,17</td>
        <td class="n mono">__TV__<span class="mbar"><i style="width:__WP__%"></i></span>
          <span class="sub">__TP__ pagas &middot; __TO__ ganadas</span></td>
        <td class="n mono">&mdash;</td>
        <td class="n mono">__TS__</td>
        <td class="n mono">__TL__</td>
        <td class="n mono">__CPS__</td>
      </tr>
    </tbody>
  </table>
</div>
<p class="pie">La barra verde es lo que pag&oacute; la pauta; la gris, lo que el video consigui&oacute; solo en el
  feed de Shorts. Cada vista cost&oacute; medio centavo de d&oacute;lar.</p>

<h2>De d&oacute;nde viene el p&uacute;blico</h2>
<div class="tw">
  <table>
    <thead><tr><th>Pa&iacute;s</th><th class="n">Vistas</th><th class="n">Del total</th></tr></thead>
    <tbody>
      <tr><td>Estados Unidos</td><td class="n mono">66.655</td><td class="n mono win">94,7%</td></tr>
      <tr><td>Reino Unido</td><td class="n mono">23</td><td class="n mono">0,0%</td></tr>
      <tr><td>Canad&aacute;</td><td class="n mono">19</td><td class="n mono">0,0%</td></tr>
      <tr><td>Argentina</td><td class="n mono">16</td><td class="n mono">0,0%</td></tr>
      <tr class="tot"><td><b>Canal completo</b><span class="sub">28 d&iacute;as, al 21 de octubre</span></td>
        <td class="n mono">70.355</td><td class="n mono">100%</td></tr>
    </tbody>
  </table>
</div>
<p class="pie">El canal es pr&aacute;cticamente un canal estadounidense: 94,7% de las vistas. El resto del mundo
  junto no llega a 100 vistas. El p&uacute;blico es 81,6% masculino y la mitad tiene entre 18 y 34 a&ntilde;os.</p>

<h2>Qu&eacute; dicen estos n&uacute;meros</h2>
<div class="nota">
  <p><span class="hl">USD&nbsp;55 compraron __TP__ vistas y el contenido se gan&oacute; __TO__ m&aacute;s sin costo.</span>
    Casi la mitad de las vistas no las pagamos. Eso solo pasa cuando el video retiene: los cuatro de la
    campa&ntilde;a se miran entre el 91,6% y el 104,5%, y ese 104,5% significa que lo vuelven a ver.</p>
  <p><span class="hl">Super Seniors trae un suscriptor por USD&nbsp;2,47; el de Internet, por USD&nbsp;17,61.</span>
    Mismo presupuesto, misma semana, mismo p&uacute;blico: siete veces de diferencia. La plata que queda va a
    Super Seniors, no repartida en partes iguales.</p>
  <p><span class="hl">El de 40 segundos retiene 33,4% y junt&oacute; 224 vistas.</span> Los de 19 a 25 segundos
    retienen arriba del 91% y juntaron entre 1.673 y 3.921. No es el tema ni el humor: es el largo.
    De ac&aacute; en adelante, ning&uacute;n short pasa de 25 segundos.</p>
  <p><span class="hl">Las 70.355 vistas del canal no son nuestras.</span> El 88,6% del tr&aacute;fico del canal
    viene de publicidad de YouTube sobre los dos episodios largos, que es otra pauta. Lo que produjo esta
    inversi&oacute;n son las __TV__ vistas de los cinco shorts, no el n&uacute;mero grande del panel.</p>
</div>
'''

BLOQUE = (BLOQUE.replace(u"__FILAS__", tabla)
                .replace(u"__TV__", mil(tV)).replace(u"__TP__", mil(tP))
                .replace(u"__TO__", mil(tO)).replace(u"__TS__", mil(tS))
                .replace(u"__TL__", mil(tL)).replace(u"__CPS__", cpsT)
                .replace(u"__WP__", u"%.1f" % (tP * 100.0 / tV)))

rep(u'\n<h2>Cuánto cuesta un seguidor en cada red</h2>',
    BLOQUE + u'\n<h2>Cuánto cuesta un seguidor en cada red</h2>')

CSS = u'''
td.vid{white-space:normal;min-width:300px}
td.vid img{float:left;width:52px;height:92px;object-fit:cover;border-radius:6px;
  border:1px solid var(--line2);margin-right:12px}
td.vid span{display:block;overflow:hidden}
td.vid b{color:var(--ink);font-weight:600}
.mbar{display:block;height:5px;border-radius:3px;background:var(--line2);margin:6px 0 2px;overflow:hidden}
.mbar i{display:block;height:100%;background:var(--teal)}
tr.tot td{background:var(--panel2);font-weight:700;border-top:1px solid var(--line2)}
tr.tot td.vid b{font-weight:800}
'''
rep(u"\n@media (max-width:700px){ .grand div{min-width:150px} }",
    CSS + u"\n@media (max-width:700px){ .grand div{min-width:150px} }")

io.open(P, "w", encoding="utf-8").write(s)
print(u"bloque de resultados agregado")
