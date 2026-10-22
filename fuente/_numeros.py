# -*- coding: utf-8 -*-
"""Unifica el presupuesto en $1.000 por mes y reparte 60/40 cada semana.

$250 por semana: $150 (60%) a la pieza que mejor anduvo, $50 en cada red,
y $100 (40%) a las otras cuatro, $25 cada una.
Arranca el lunes 19 de octubre: octubre $500, noviembre $1.000, diciembre $1.000.
"""
import io

P = "gen_plan.py"
S = "seguimiento_src.html"
cambios = []

def rep(p, a, b, n=1):
    s = io.open(p, encoding="utf-8").read()
    assert s.count(a) == n, (p, s.count(a), a[:70])
    io.open(p, "w", encoding="utf-8").write(s.replace(a, b))
    cambios.append(a.split("\n")[0][:58])

# --- aritmetica, para no escribir un numero a ojo ---
SEM, MES = 250, 1000
GAN, RESTO = int(SEM * .6), int(SEM * .4)
assert GAN == 150 and RESTO == 100 and GAN + RESTO == SEM
OCT, NOV, DIC = 500, 1000, 1000
TRIM = OCT + NOV + DIC
assert TRIM == 2500
FIJO = 4000 + 1500 + 392
TOT = [FIJO + OCT, FIJO + NOV, FIJO + DIC]
assert TOT == [6392, 6892, 6892], TOT
NEXT = sum(TOT)
assert NEXT == 20176, NEXT
ANIO = 34413 + NEXT
assert ANIO == 54589, ANIO
VISTAS = TRIM * 100          # a $0,01 la vista
SUBS = VISTAS // 100         # 1 de cada 100
assert (VISTAS, SUBS) == (250000, 2500)

# ------------------------------------------------------------ calendario
rep(P, u"""    (u'<td class="c"><span class="pa">$225</span></td>' if i >= 2""",
       u"""    (u'<td class="c"><span class="pa">$250</span></td>' if i >= 1""")

# ------------------------------------------------------------ el plan
rep(P, u'<div><span>Pauta por semana</span><b class="vnext">$225</b></div>',
       u'<div><span>Pauta por semana</span><b class="vnext">$250</b></div>')
rep(P, u'<div><span>Pauta del trimestre</span><b class="vnext">$2.250</b></div>',
       u'<div><span>Pauta del trimestre</span><b class="vnext">$2.500</b></div>')
rep(P, u"La plata va a una sola pieza por semana, la que ya est&aacute; funcionando sola.",
       u"El 60% de la pauta va a la pieza que ya est&aacute; funcionando sola y el 40% se reparte "
       u"en las otras cuatro.")

# ------------------------------------------------------------ donde va la plata
rep(P, u"""      <thead><tr><th>Red</th><th class="n">Por pieza</th><th class="n">Pruebas</th>
        <th class="n">Inversi&oacute;n del trimestre</th></tr></thead>
      <tbody>
        <tr><th>TikTok</th><td class="n next">$75</td><td class="n next">10</td><td class="n next">$750</td></tr>
        <tr><th>Instagram Reels</th><td class="n next">$75</td><td class="n next">10</td><td class="n next">$750</td></tr>
        <tr><th>YouTube Shorts</th><td class="n next">$75</td><td class="n next">10</td><td class="n next">$750</td></tr>
        <tr class="sumrow"><th>Total por semana</th><td class="n next">$225</td><td class="n next">30</td>
          <td class="n next">$2.250</td></tr>
      </tbody>""",
       u"""      <thead><tr><th>Destino</th><th class="n">Por semana</th><th class="n">Reparto</th>
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
      </tbody>""")

rep(P, u"""    <h4>Una pieza por semana, la misma en las tres</h4>
    <ol class="steps">
      <li><b>Las cinco salen sin plata.</b> A las 48 horas ya se ve cu&aacute;l se mueve sola.</li>
      <li><b>Esa pieza lleva $75 en cada red</b>, la misma semana y con el mismo monto.</li>
      <li><b>A los siete d&iacute;as</b> se anota costo por seguidor en cada una y se compara.</li>
    </ol>
    <p class="answer">Es la &uacute;nica forma de saber qu&eacute; red funciona: misma pieza, misma plata,
      misma semana. Si cada prueba usa un video distinto, lo que se mide es el video, no la red.</p>""",
       u"""    <h4>C&oacute;mo se reparte cada semana</h4>
    <ol class="steps">
      <li><b>Las cinco salen sin plata.</b> A las 48 horas ya se ve cu&aacute;l se mueve sola.</li>
      <li><b>El 60% va a esa pieza:</b> $50 en cada una de las tres redes, la misma semana.</li>
      <li><b>El 40% se reparte en las otras cuatro:</b> $25 cada una, en la red donde mejor anduvo.</li>
      <li><b>A los siete d&iacute;as</b> se anota el costo por seguidor y se compara.</li>
    </ol>
    <p class="answer">La ganadora lleva el mismo monto en las tres redes, as&iacute; el costo por
      seguidor compara redes y no videos. El 40% restante existe para que ninguna pieza quede sin
      una sola oportunidad de empuje.</p>""")

rep(P, u"""        <tr class="sumrow"><th>Desde la semana 3</th>
          <td class="n next">5 por semana</td><td class="n next">$225 a una sola</td></tr>""",
       u"""        <tr class="sumrow"><th>Desde la semana 2</th>
          <td class="n next">5 por semana</td><td class="n next">$250 repartidos 60/40</td></tr>""")

# ------------------------------------------------------------ con pauta
rep(P, u"""        <tr class="sumrow"><th>$750 por mes
          <span class="sublabel">$2.250 en los tres meses &middot; el plan actual</span></th>
          <td class="n">~225.000</td><td class="n">~2.250</td></tr>""",
       u"""        <tr class="sumrow"><th>$1.000 por mes
          <span class="sublabel">$2.500 hasta fin de a&ntilde;o &middot; el plan actual</span></th>
          <td class="n">~250.000</td><td class="n">~2.500</td></tr>""")

rep(P, u"""      <li><b>$225 por semana</b>, dentro del tope de $1.000 por mes.</li>
      <li><b>$75 en cada red</b>, sobre la misma pieza.</li>""",
       u"""      <li><b>$1.000 por mes</b>, $250 por semana.</li>
      <li><b>$150 a la pieza que anduvo</b> y $100 repartidos en las otras cuatro.</li>""")

rep(P, u"""      <th class="n">Vistas con $750 por mes</th><th class="n">Suscriptores</th></tr></thead>
    <tbody>
      <tr><th>$0,01 <span class="sublabel">lo que supone la tabla de arriba</span></th>
        <td class="n">~225.000</td><td class="n">~2.250</td></tr>
      <tr><th>$0,03</th><td class="n">~75.000</td><td class="n">~750</td></tr>
      <tr><th>$0,05</th><td class="n">~45.000</td><td class="n">~450</td></tr>""",
       u"""      <th class="n">Vistas con $1.000 por mes</th><th class="n">Suscriptores</th></tr></thead>
    <tbody>
      <tr><th>$0,01 <span class="sublabel">lo que supone la tabla de arriba</span></th>
        <td class="n">~250.000</td><td class="n">~2.500</td></tr>
      <tr><th>$0,03</th><td class="n">~83.000</td><td class="n">~830</td></tr>
      <tr><th>$0,05</th><td class="n">~50.000</td><td class="n">~500</td></tr>""")

# ------------------------------------------------------------ organico + pauta
rep(P, u"""      <tr class="sumrow"><th>Y encima, los $225 por semana</th>
        <td class="n next">~795.000</td><td class="n next">~4.800</td></tr>""",
       u"""      <tr class="sumrow"><th>Y encima, los $250 por semana</th>
        <td class="n next">~820.000</td><td class="n next">~5.050</td></tr>""")
rep(P, u"La pauta pone 225.000 de ese mill&oacute;n.",
       u"La pauta pone 250.000 de ese mill&oacute;n.")

# ------------------------------------------------------------ budget
rep(P, u"""        <tr><th>Pauta <span class="sublabel">$225 por semana &middot; arranca en la semana 3</span></th>""",
       u"""        <tr><th>Pauta <span class="sublabel">$250 por semana &middot; tope de $1.000 por mes</span></th>""")
rep(P, u"""          <td class="n next hoy">$225</td><td class="n next">$1.125</td><td class="n next">$900</td></tr>""",
       u"""          <td class="n next hoy">$500</td><td class="n next">$1.000</td><td class="n next">$1.000</td></tr>""")
rep(P, u"""          <td class="n next hoy">$6.117</td><td class="n next">$7.017</td><td class="n next">$6.792</td></tr>""",
       u"""          <td class="n next hoy">$6.392</td><td class="n next">$6.892</td><td class="n next">$6.892</td></tr>""")
rep(P, u'<b class="vnext">$19.926</b>', u'<b class="vnext">$20.176</b>')
rep(P, u'<b class="vtot">$54.339</b>', u'<b class="vtot">$54.589</b>')

# ------------------------------------------------------------ seguimiento
rep(S, u'<b class="vdim" id="kRest">$3.600</b>', u'<b class="vdim" id="kRest">$3.000</b>')
rep(S, u'KEY = "brainsyrup:seguimiento:v1", PRES = 3600, META = 60;',
       u'KEY = "brainsyrup:seguimiento:v1", PRES = 3000, META = 60;')
rep(S, u"""  <p>Al mes, la red que traiga el <span class="hl">seguidor más barato</span> se queda con más turnos de los $60.
    Las otras siguen recibiendo las publicaciones, pero sin pauta.</p>""",
       u"""  <p>Cada semana, la pieza que mejor anduvo se lleva el <span class="hl">60% de la pauta</span>
    y el 40% restante se reparte en las otras cuatro.</p>""")

VIEJA = io.open(S, encoding="utf-8").read()
a = VIEJA.index(u"<h2>Cu&aacute;ndo entra la plata</h2>")
b = VIEJA.index(u"<h2>D&oacute;nde se compra la pauta</h2>")
NUEVA = u"""<h2>Cu&aacute;ndo entra la plata</h2>
<p class="pie" style="margin:0 0 14px">Dos d&iacute;as de org&aacute;nico antes de pagar: son los que
definen a qu&eacute; pieza va el 60%.</p>
<div class="tw">
  <table>
    <thead><tr><th>Cu&aacute;ndo</th><th>Qu&eacute; pasa</th><th class="n">Cu&aacute;nto</th></tr></thead>
    <tbody>
      <tr><th>Hoy</th>
        <td class="txt">Salen las 15 publicaciones: 5 piezas en 3 redes.</td>
        <td class="n">$0</td></tr>
      <tr><th>Dos d&iacute;as</th>
        <td class="txt">Org&aacute;nico. Se miden <b>retenci&oacute;n, guardados y visitas al
          perfil</b>, no vistas.</td>
        <td class="n">$0</td></tr>
      <tr><th>Lunes &middot; 60%</th>
        <td class="txt">A la pieza con mejor retenci&oacute;n: <b>$50 en cada una de las tres
          redes</b>.</td>
        <td class="n">$150</td></tr>
      <tr><th>Lunes &middot; 40%</th>
        <td class="txt">A las otras cuatro: <b>$25 cada una</b>, en la red donde mejor anduvo.</td>
        <td class="n">$100</td></tr>
      <tr><th>Por semana</th>
        <td class="txt">Mismo esquema todas las semanas.</td>
        <td class="n">$250</td></tr>
      <tr><th>Por mes</th>
        <td class="txt">Tope.</td>
        <td class="n">$1.000</td></tr>
    </tbody>
  </table>
</div>
<div class="nota" style="margin-top:16px">
  <p><span class="hl">Por qu&eacute; no desde el minuto cero.</span> Si las 15 publicaciones
    arrancan con plata, todas tienen vistas y ninguna dice cu&aacute;l es buena: se gasta el
    presupuesto y encima se pierde la informaci&oacute;n.</p>
  <p><span class="hl">Por qu&eacute; 60 y no 100.</span> Concentrar rinde m&aacute;s, pero las otras
    cuatro siguen con pauta: cuatro de cinco piezas no se mueren sin haber tenido empuje.</p>
  <p><span class="hl">Por qu&eacute; queda margen.</span> Si una pieza arranca sola a mitad de
    semana, tiene que haber presupuesto para empujarla.</p>
</div>

"""
io.open(S, "w", encoding="utf-8").write(VIEJA[:a] + NUEVA + VIEJA[b:])
cambios.append(u"Cuando entra la plata (reescrita)")

print("\n".join(u"  - " + c for c in cambios))
print("%d cambios" % len(cambios))
