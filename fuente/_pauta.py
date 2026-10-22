# -*- coding: utf-8 -*-
"""Lo que salio de la reunion del 15/10: segmentacion geografica, donde se
compra la pauta, y los objetivos como hipotesis y no como promesa."""
import io

def rep(p, a, b):
    s = io.open(p, encoding="utf-8").read()
    assert a in s, (p, a[:80])
    assert b not in s, (p, "ya estaba")
    io.open(p, "w", encoding="utf-8").write(s.replace(a, b, 1))

# ---------------------------------------------------------------- gen_plan
P = "gen_plan.py"

CSS = (u".pie{font-size:16.5px;line-height:1.55;color:var(--ink-soft);"
       u"margin:12px 0 0;max-width:none}")
rep(P, CSS, CSS + u"""
.aviso{margin:16px 0 0;padding:18px 22px;border:1px solid var(--line);
  border-left:3px solid #E9B949;border-radius:10px;background:var(--panel)}
.aviso p{margin:0;font-size:17px;line-height:1.5;color:var(--ink-soft);max-width:none}
.aviso b{color:#E9B949}""")

HIP = u"""<p class="pie">Estos n&uacute;meros son una <b>hip&oacute;tesis para validar</b>, no una meta
  comprometida. Todav&iacute;a no sabemos c&oacute;mo convierte esta audiencia: cu&aacute;nta gente que ve
  un corto termina suscribi&eacute;ndose al canal. Esta tanda de publicaciones existe para averiguarlo.
  Con ese dato, los n&uacute;meros de arriba se confirman o se corrigen.</p>

<h2>Estrategias para generar mec&aacute;nicas virales</h2>"""
rep(P, u"<h2>Estrategias para generar mec&aacute;nicas virales</h2>", HIP)

GEO = u"""<div class="aviso">
  <p><b>Ojo con estos n&uacute;meros.</b> Salen de suponer que cada vista cuesta $0,01, y ese precio
    lo medimos con campa&ntilde;as sin segmentar: trajeron vistas de Kazajist&aacute;n en vez de
    California. Una vista de Estados Unidos cuesta varias veces m&aacute;s, as&iacute; que la tabla de
    arriba es el techo optimista, no la expectativa.</p>
</div>
<div class="tw fit">
  <table>
    <thead><tr><th>Si la vista segmentada a Estados Unidos cuesta&hellip;</th>
      <th class="n">Vistas con $750 por mes</th><th class="n">Suscriptores</th></tr></thead>
    <tbody>
      <tr><th>$0,01 <span class="sublabel">lo que supone la tabla de arriba</span></th>
        <td class="n">~225.000</td><td class="n">~2.250</td></tr>
      <tr><th>$0,03</th><td class="n">~75.000</td><td class="n">~750</td></tr>
      <tr><th>$0,05</th><td class="n">~45.000</td><td class="n">~450</td></tr>
    </tbody>
  </table>
</div>
<p class="pie">Cu&aacute;l de las tres es la real lo sabemos la semana que viene, con la primera
campa&ntilde;a segmentada a Estados Unidos. Hasta entonces, cualquier n&uacute;mero de
suscriptores comprados es una estimaci&oacute;n.</p>

<h2>Org&aacute;nico + pauta</h2>"""
rep(P, u"<h2>Org&aacute;nico + pauta</h2>", GEO)

# ------------------------------------------------------------- seguimiento
S = "seguimiento_src.html"

rep(S, u".hl{color:var(--teal);font-weight:700}",
    u""".hl{color:var(--teal);font-weight:700}
a.lnk{color:var(--teal);text-decoration:none;border-bottom:1px solid var(--line2)}
a.lnk:hover{border-color:var(--teal)}
td.txt{white-space:normal;color:var(--ink2);min-width:320px}
td.txt b{color:var(--ink)}
.sub{display:block;font-size:11.5px;color:var(--dim);margin-top:2px}""")

PAUTA = u"""<h2>D&oacute;nde se compra la pauta</h2>
<div class="tw">
  <table>
    <thead><tr><th>Red</th><th>D&oacute;nde</th><th>C&oacute;mo</th></tr></thead>
    <tbody>
      <tr><th class="grp tt">TikTok</th>
        <td><a class="lnk" href="https://ads.tiktok.com" target="_blank" rel="noopener">ads.tiktok.com</a>
          <span class="sub">TikTok Ads Manager</span></td>
        <td class="txt"><b>Spark Ads</b> sobre el posteo ya publicado. El bot&oacute;n
          <b>Promote</b> del perfil no sirve: es el de la app y pide pagar desde el celular.</td></tr>
      <tr><th class="grp ig">Instagram</th>
        <td><a class="lnk" href="https://business.facebook.com/adsmanager" target="_blank" rel="noopener">Meta Ads Manager</a>
          <span class="sub">business.facebook.com</span></td>
        <td class="txt">La cuenta tiene que estar como <b>Business</b> y vinculada a una p&aacute;gina
          de Facebook. El bot&oacute;n <b>Boost</b> de la app es la versi&oacute;n recortada.</td></tr>
      <tr><th class="grp yt">YouTube Shorts</th>
        <td><a class="lnk" href="https://ads.google.com" target="_blank" rel="noopener">Google Ads</a>
          <span class="sub">campa&ntilde;a de video</span></td>
        <td class="txt">Sobre el short que ya est&aacute; publicado, no sobre una copia subida
          aparte.</td></tr>
    </tbody>
  </table>
</div>

<h2>Las tres reglas</h2>
<div class="nota">
  <p><span class="hl">Toda campa&ntilde;a segmentada a Estados Unidos.</span> Los $100 que se
    invirtieron sin segmentar trajeron 50.000 vistas de Kazajist&aacute;n. Esas vistas no dejan
    suscriptores ni sirven para conseguir una marca.</p>
  <p><span class="hl">Siempre sobre el posteo org&aacute;nico</span>, nunca un aviso suelto. Si la
    pauta corre por fuera, las vistas y los seguidores no se le suman a la publicaci&oacute;n, y el
    costo por seguidor de esta p&aacute;gina deja de significar algo.</p>
  <p><span class="hl">Todo se paga con la tarjeta BX de Santiago</span>, que reemplaza a la de la
    oficina que ven&iacute;a usando Federico.</p>
</div>

</div>

<script>"""
rep(S, u"\n</div>\n\n<script>", u"\n" + PAUTA)

print("listo")
