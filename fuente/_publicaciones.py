# -*- coding: utf-8 -*-
"""Carga las 4 publicaciones reales del 17/10 en la tabla de Seguimiento."""
import io

P = "seguimiento_src.html"
s = io.open(P, encoding="utf-8").read()

def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70])
    s = s.replace(a, b, 1)

# 1. Nueva clave de localStorage (si no, el navegador sigue mostrando los ejemplos)
#    y presupuesto del trimestre alineado con los $2.500 del resto del sitio.
rep(u'var KEY = "brainsyrup:seguimiento:v1", PRES = 3000, META = 60;',
    u'var KEY = "brainsyrup:seguimiento:v2", PRES = 2500, META = 60;')
rep(u'<b class="vdim" id="kRest">$3.000</b>',
    u'<b class="vdim" id="kRest">$2.500</b>')

# 2. Los datos reales reemplazan a los ejemplos inventados.
VIEJO = u'''  function ejemplos(){
    var a = mkFila("2026-10-13", "El del teléfono gigante", true);
    a.tt = { p: 60, v: 7400, s: 38 }; a.ig = { p: 0, v: 910, s: 6 }; a.yt = { p: 0, v: 2300, s: 21 };
    var b = mkFila("2026-10-14", "Cuando el micrófono traiciona", true);
    b.tt = { p: 0, v: 1200, s: 9 }; b.ig = { p: 60, v: 5100, s: 17 }; b.yt = { p: 0, v: 1800, s: 14 };
    var c = mkFila("2026-10-15", "La respuesta que nadie esperaba", true);
    c.tt = { p: 0, v: 2600, s: 15 }; c.ig = { p: 0, v: 740, s: 4 }; c.yt = { p: 60, v: 9800, s: 61 };
    filas = [a, b, c];
  }'''

NUEVO = u'''  function ejemplos(){
    /* Publicadas el sábado 17/10/2026. Números leídos el lunes 19, a 48 horas.
       Plata en 0: la primera campaña de Google Ads todavía no gastó. */
    var a = mkFila("2026-10-17", "Super Seniors", false);
    a.tt = { p: 0, v: 7, s: 0 }; a.ig = { p: 0, v: 1352, s: 0 }; a.yt = { p: 0, v: 1950, s: 7 };
    var b = mkFila("2026-10-17", "Gravity · How long would you last", false);
    b.tt = { p: 0, v: 4, s: 0 }; b.ig = { p: 0, v: 169, s: 0 }; b.yt = { p: 0, v: 1215, s: 2 };
    var c = mkFila("2026-10-17", "Who controls the Internet", false);
    c.tt = { p: 0, v: 4, s: 0 }; c.ig = { p: 0, v: 137, s: 0 }; c.yt = { p: 0, v: 820, s: 1 };
    var d = mkFila("2026-10-17", "iPhone 1960", false);
    d.tt = { p: 0, v: 4, s: 0 }; d.ig = { p: 0, v: 137, s: 0 }; d.yt = { p: 0, v: 766, s: 0 };
    filas = [a, b, c, d];
  }'''
rep(VIEJO, NUEVO)

# 3. Lectura de esos numeros, debajo de la tabla.
NOTA = u'''
<div class="nota" style="margin-top:4px">
  <p><span class="hl">475 vistas por suscriptor.</span> Las 4.751 vistas de YouTube dejaron 10
    suscriptores: 0,21%. Esta página venía asumiendo cerca del 1%, así que la conversión real es
    cinco veces peor que la hipótesis. Es el número que define si el plan cierra, y ahora está
    medido en vez de supuesto.</p>
  <p><span class="hl">Super Seniors ganó en las dos redes que funcionan.</span> 1,6 veces en YouTube
    y 8 veces en Instagram. No es el repunte de una red: es la pieza. Ahí va el 60%.</p>
  <p><span class="hl">TikTok no entregó: 19 reproducciones y cero seguidores.</span> No es el
    contenido, es arranque en frío — cuenta de cero días, sin seguir a nadie, cuatro videos subidos
    en dos minutos desde la web. No se le pone plata hasta que un posteo haga números solo.</p>
  <p><span class="hl">Todos los videos se miran 16 segundos.</span> Duración promedio de 0:16 a 0:18
    en las cuatro piezas, midan 0:19 o 0:25. Y el más corto es el que más se repite. Los trailers
    nuevos van a 20 segundos, no a 30.</p>
</div>

<h2>Qué se decide con esto</h2>'''
rep(u'\n<h2>Qué se decide con esto</h2>', NOTA)

io.open(P, "w", encoding="utf-8").write(s)
print("seguimiento_src.html actualizado")
