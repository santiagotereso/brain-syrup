# -*- coding: utf-8 -*-
"""Suma el plan de los proximos diez dias y el formato de trailer."""
import io

p = "gen_plan.py"
s = io.open(p, encoding="utf-8").read()

def rep(a, b, n=1):
    global s
    assert a in s, a[:90]
    s = s.replace(a, b, n)

NUEVO = u'''<h2>Los pr&oacute;ximos diez d&iacute;as</h2>
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
<p class="pie">Seis opciones para el call to action. La primera es la que qued&oacute; acordada.
Ninguna pide suscripciones: se percibe como manipulador y espanta.</p>
<div class="tw fit" style="margin-top:12px">
  <table>
    <thead><tr><th>Opci&oacute;n</th><th>Por qu&eacute;</th></tr></thead>
    <tbody>
      <tr class="sumrow"><th>Watch the full episode</th>
        <td>La acordada. No pide nada: se&ntilde;ala d&oacute;nde est&aacute; el resto y se va.</td></tr>
      <tr><th>The full episode is on the channel</th>
        <td>La misma idea con el destino expl&iacute;cito. Sirve donde no hay link clickeable.</td></tr>
      <tr><th>There&rsquo;s nine more minutes of this</th>
        <td>Usa la duraci&oacute;n real como argumento. Cambia el n&uacute;mero seg&uacute;n el video.</td></tr>
      <tr><th>The answer is in the full episode</th>
        <td>Para los trailers que dejan una pregunta abierta, como el de la gravedad.</td></tr>
      <tr><th>We explain the whole thing on YouTube</th>
        <td>La m&aacute;s directa de todas. Funciona bien en TikTok, donde el tono es m&aacute;s hablado.</td></tr>
      <tr><th>Full episode, link in bio</th>
        <td>Para Instagram y TikTok, donde el link no se puede poner en el video.</td></tr>
    </tbody>
  </table>
</div>

'''
rep(u"<h2>D&oacute;nde va la plata</h2>", NUEVO + u"<h2>D&oacute;nde va la plata</h2>")

# ---- estrategias: el formato nuevo ----
rep(u'''      <li>Cinco por semana, cortados del video largo</li>
      <li>Hook en los primeros 3 segundos</li>
      <li>La misma pieza en las tres plataformas</li>
      <li>Cada uno remite al video completo</li>
      <li><b>Call to action:</b> invitar a visitar el canal</li>''',
    u'''      <li>Un trailer por video largo, no varios recortes</li>
      <li>Hook en los primeros 3 segundos</li>
      <li>La misma pieza en las tres plataformas</li>
      <li>Voz en off uniforme entre todos</li>
      <li><b>Call to action:</b> ver el episodio completo</li>''')
rep(u'''      <li>Formato de 2 minutos</li>
      <li><b>Call to action:</b> pedir comentarios, no solo suscripciones</li>''',
    u'''      <li>Formato de 2 minutos</li>
      <li>Prueba A/B con la velocidad a 1,1&times;</li>
      <li><b>Call to action:</b> pedir comentarios, no suscripciones</li>''')

# ---- calendario: la entrega del viernes 16 ----
rep(u'''<h2>Calendario</h2>
<div class="legend">
  <span><span class="chip chip--short">5</span> &nbsp;Cinco publicaciones por semana, a las tres redes</span>
  <span><span class="chip chip--pub">V05</span> &nbsp;El video largo, los viernes</span>
</div>''',
    u'''<h2>Calendario</h2>
<div class="legend">
  <span><span class="chip chip--short">5</span> &nbsp;Publicaciones por semana, a las tres redes</span>
  <span><span class="chip chip--pub">V05</span> &nbsp;El video largo, los viernes</span>
  <span><span class="chip chip--ent">16 oct</span> &nbsp;Los 5 trailers listos</span>
</div>''')
rep(u"""fila_post = u"".join(
    u'<td class="c"><span class="chip chip--short">%d</span></td>' % (7 if i == 0 else 5)
    for i, w in enumerate(semanas))""",
    u"""fila_post = u"".join(
    u'<td class="c"><span class="chip chip--short">%d</span></td>' % (5 if i == 0 else 6 if i == 1 else 5)
    for i, w in enumerate(semanas))
fila_prod = u"".join(
    (u'<td class="c"><span class="chip chip--ent">5 trailers</span></td>' if i == 0 else
     u'<td class="c"><span class="chip chip--ent">6 cortos</span></td>' if i == 1 else
     u'<td class="c"><span class="na">&mdash;</span></td>')
    for i, w in enumerate(semanas))""")
rep(u'''      <tr><th>Publicaciones</th>__FILA_POST__</tr>''',
    u'''      <tr><th>Entrega</th>__FILA_PROD__</tr>
      <tr><th>Publicaciones</th>__FILA_POST__</tr>''')
rep(u'(u"__FILA_PAUTA__", fila_pauta),',
    u'(u"__FILA_PAUTA__", fila_pauta), (u"__FILA_PROD__", fila_prod),')
rep(u".chip--short{background:var(--blue-soft);color:var(--blue)}",
    u".chip--short{background:var(--blue-soft);color:var(--blue)}\n"
    u".chip--ent{background:#2A2413;color:var(--warn)}")

# ---- el pedido de fondos, pendiente ----
rep(u'''  <div class="only-open"><span>Total del a&ntilde;o</span><b class="vtot">$54.339</b></div>
</div>''',
    u'''  <div class="only-open"><span>Total del a&ntilde;o</span><b class="vtot">$54.339</b></div>
</div>
<p class="pie">Pedido aparte, todav&iacute;a sin aprobar: <b>$7.000</b> hasta fin de a&ntilde;o para anuncios y
herramientas, en dos pagos, para que la cuenta de la oficina deje de quedar en descubierto.</p>''')

io.open(p, "w", encoding="utf-8").write(s)
print("produccion de diez dias")
