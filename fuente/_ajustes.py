# -*- coding: utf-8 -*-
"""Reordena las pestanias, renombra Referencias, aclara el tablero y
deja la pagina de cuentas en los pasos."""
import io, re

PAGS = [(u"Objetivo", u""), (u"Seguimiento", u"seguimiento/"), (u"Videos", u"videos/"),
        (u"Picadora", u"picadora/"), (u"Cuentas", u"cuentas/"),
        (u"Material de estudio", u"referencias/")]

def rep(s, a, b, n=1):
    assert a in s, a[:90]
    return s.replace(a, b, n)

# ---------- 1. el orden nuevo en build.py ----------
p = "build.py"
s = io.open(p, encoding="utf-8").read()
ini = s.index(u"PAGS = [")
fin = s.index(u"\n\ndef nav(")
nuevo = u"PAGS = [" + u",\n        ".join(u'(u"%s", u"%s")' % (a, b) for a, b in PAGS) + u"]"
s = s[:ini] + nuevo + s[fin:]
io.open(p, "w", encoding="utf-8").write(s)
print("build.py: orden nuevo")

# ---------- 2. el mismo orden en gen_videos.py ----------
p = "gen_videos.py"
s = io.open(p, encoding="utf-8").read()
m = re.search(r"    its = \[.*?\]\n", s)
s = s[:m.start()] + u"    its = [" + u", ".join(u'(u"%s", u"%s")' % (a, b) for a, b in PAGS) + u"]\n" + s[m.end():]
io.open(p, "w", encoding="utf-8").write(s)
print("gen_videos.py: orden nuevo")

# ---------- 3. referencias pasa a material de estudio ----------
p = "referencias_src.html"
s = io.open(p, encoding="utf-8").read()
s = rep(s, u"<title>Referencias</title>", u"<title>Material de estudio</title>")
s = rep(s, u'<p class="kicker">Referencias</p>', u'<p class="kicker">Material de estudio</p>')
s = rep(s, u"<h2>Shorts y YouTube</h2>",
        u"<h2>Referencias</h2>\n<p class=\"pie\" style=\"margin:0 0 18px\">A qui&eacute;n mirar en cada "
        u"plataforma. Diez canales verificados uno por uno.</p>\n\n<h3>Shorts y YouTube</h3>")
for a in [u"<h2>TikTok</h2>", u"<h2>Instagram y Reels</h2>"]:
    s = rep(s, a, a.replace(u"h2", u"h3"))
s = rep(s, u"<h2>P&aacute;ginas de carga</h2>", u"<h3>P&aacute;ginas de carga</h3>")
s = rep(s, u"h2{font-size:21px;letter-spacing:-.015em;font-weight:700;margin:42px 0 14px;display:flex;align-items:center;gap:14px}",
        u"h2{font-size:21px;letter-spacing:-.015em;font-weight:700;margin:46px 0 14px;display:flex;align-items:center;gap:14px}\n"
        u"h3{font-size:15px;font-weight:700;letter-spacing:.04em;color:var(--ink2);margin:28px 0 12px}")
io.open(p, "w", encoding="utf-8").write(s)
print("referencias: material de estudio")

# ---------- 4. el tablero, con las unidades a la vista ----------
p = "seguimiento_src.html"
s = io.open(p, encoding="utf-8").read()
s = rep(s, u"<h2>C&oacute;mo viene cada red</h2>",
        u"<h2>Cu&aacute;nto cuesta un seguidor en cada red</h2>\n"
        u'<p class="pie" style="margin:0 0 14px">Es la plata invertida dividida por los seguidores que trajo. '
        u'Cuanto m&aacute;s bajo, mejor: esa red es la que rinde.</p>')
viejo = u'''      var sp = document.createElement("span"); sp.textContent = R.nm;
      var b = document.createElement("b");
      b.className = "vteal";
      b.textContent = cps === null ? "—" : "$" + dos(cps);
      var sub = document.createElement("span");
      sub.style.marginTop = "6px"; sub.style.letterSpacing = "0"; sub.style.textTransform = "none";
      sub.style.fontSize = "12px"; sub.className = "mono";
      sub.textContent = money(p) + " · " + nf(v) + " vistas · " + nf(s) + " segs.";
      d.appendChild(sp); d.appendChild(b); d.appendChild(sub);'''
nuevo2 = u'''      var sp = document.createElement("span"); sp.textContent = R.nm;
      var b = document.createElement("b");
      b.className = "vteal";
      b.textContent = cps === null ? "sin datos" : "$" + dos(cps);
      var u1 = document.createElement("span");
      u1.style.marginTop = "2px"; u1.style.letterSpacing = "0"; u1.style.textTransform = "none";
      u1.style.fontSize = "13px"; u1.style.color = "var(--ink2)";
      u1.textContent = cps === null ? "todavía no hay seguidores cargados" : "por cada seguidor";
      var sub = document.createElement("span");
      sub.style.marginTop = "8px"; sub.style.letterSpacing = "0"; sub.style.textTransform = "none";
      sub.style.fontSize = "12px"; sub.className = "mono";
      sub.textContent = money(p) + " invertidos · " + nf(v) + " vistas · " + nf(s) + " seguidores";
      d.appendChild(sp); d.appendChild(b); d.appendChild(u1); d.appendChild(sub);'''
s = rep(s, viejo, nuevo2)
s = rep(s, u'<p class="pie" id="veredicto">Cargá las primeras publicaciones y acá va a aparecer cuál red trae seguidores más baratos.</p>',
        u'<p class="pie" id="veredicto">Cargá las primeras publicaciones y acá va a aparecer cuál red trae seguidores más baratos.</p>')
s = rep(s, u'      <th rowspan="2" class="n">$ por seguidor</th>',
        u'      <th rowspan="2" class="n">Costo por seguidor</th>')
io.open(p, "w", encoding="utf-8").write(s)
print("seguimiento: unidades claras")

# ---------- 5. cuentas: directo a los pasos ----------
p = "cuentas_src.html"
s = io.open(p, encoding="utf-8").read()
i = s.index(u'<p class="intro">Para que los videos')
j = s.index(u'<div class="quien">')
s = s[:i] + s[j:]
s = rep(s, u'''<h2>Antes de empezar: los tres datos</h2>
<p class="intro">Santiago prepara esto y se lo pasa a la persona en Estados Unidos. <b>Sin estos tres datos
no hay que arrancar</b>, porque despu&eacute;s cambiarlos es un dolor de cabeza.</p>''',
        u'''<h2>Antes de empezar: los tres datos</h2>
<p class="intro">Santiago los prepara y se los pasa. <b>Sin estos tres no hay que arrancar.</b></p>''')
s = rep(s, u'''        Algo del estilo <span class="dato">brainsyrup@3dar.com</span>.
        <b>Nunca el mail personal de la persona que abre la cuenta.</b> Si ma&ntilde;ana esa persona desaparece,
        con el mail nuestro recuperamos todo; con el de ella, perdemos las cuentas.''',
        u'''Algo del estilo <span class="dato">brainsyrup@3dar.com</span>.
        <b>Nunca el mail personal de nadie.</b>''')
s = rep(s, u'''La elige Santiago y la guarda en el gestor de contrase&ntilde;as de
        la empresa. Se la pasa a la persona por un canal privado, no por mail.''',
        u'''La elige Santiago y la guarda en el gestor de la empresa.
        Se la pasa por un canal privado, no por mail.''')
s = rep(s, u'''El mismo en las dos redes, para que sea f&aacute;cil de encontrar.
        Por ejemplo <span class="dato">@brainsyrup</span>. Conviene chequear antes que est&eacute; libre en las dos.''',
        u'''El mismo en las dos redes. Por ejemplo
        <span class="dato">@brainsyrup</span>. Chequear antes que est&eacute; libre en las dos.''')
s = rep(s, u'''    <p>Esto es lo que despu&eacute;s nos deja programar publicaciones desde la computadora y ver las estad&iacute;sticas.</p>
''', u"")
s = rep(s, u'''    <span class="ojo"><b>Tiene que ser Business.</b> Es la &uacute;nica opci&oacute;n que despu&eacute;s permite que
      Santiago administre la cuenta desde Argentina sin pedirle la contrase&ntilde;a cada vez.</span>''',
        u'''    <span class="ojo"><b>Tiene que ser Business, no Creator.</b> Es la &uacute;nica que despu&eacute;s deja
      administrar la cuenta desde Argentina.</span>''')
s = rep(s, u'''    <p>Instagram le va a ofrecer conectar una p&aacute;gina de Facebook. Que cree una nueva, con el nombre
      <b>Brain Syrup</b>. No hace falta que esa p&aacute;gina tenga contenido ni que nadie la vea: es el puente
      t&eacute;cnico que permite administrar Instagram desde otra computadora.</p>''',
        u'''    <p>Instagram le va a ofrecer conectar una p&aacute;gina de Facebook. Que cree una nueva con el nombre
      <b>Brain Syrup</b>. No hace falta que tenga contenido.</p>''')
s = rep(s, u'''    <p>Desde Argentina, normal, sin VPN. Las dos redes le van a pedir verificar que es &eacute;l: mandan un
      c&oacute;digo al mail de la empresa, que Santiago tiene. Por eso el mail ten&iacute;a que ser nuestro.</p>
    <span class="ojo"><b>Esto es esperable y no es un problema.</b> Un cambio de pa&iacute;s una sola vez es
      com&uacute;n. Lo que trae problemas es andar saltando de pa&iacute;s todos los d&iacute;as con una VPN.</span>''',
        u'''    <p>Desde Argentina, normal, sin VPN. Las dos redes mandan un c&oacute;digo de verificaci&oacute;n al mail
      de la empresa. Es esperable.</p>''')
s = rep(s, u'''    <p>Este es el paso que convierte las cuentas en cuentas de la empresa: a partir de ac&aacute;, el c&oacute;digo
      para entrar lo genera el tel&eacute;fono de Santiago y la persona en Estados Unidos ya no puede entrar
      aunque tenga la contrase&ntilde;a.</p>''',
        u'''    <p>A partir de ac&aacute; el c&oacute;digo lo genera el tel&eacute;fono de Santiago, y la persona en Estados
      Unidos ya no puede entrar aunque tenga la contrase&ntilde;a.</p>''')
s = rep(s, u'''    <li><b>No usar el mail personal de nadie.</b> Ni el de la persona en Estados Unidos ni el de
      Santiago. Si la cuenta queda atada a una persona, el d&iacute;a que esa persona se va, se va la cuenta.</li>''',
        u'''    <li><b>No usar el mail personal de nadie.</b> El d&iacute;a que esa persona se va, se va la cuenta.</li>''')
s = rep(s, u'''    <li><b>No poner el segundo factor por mensaje de texto.</b> Si el c&oacute;digo llega al tel&eacute;fono de
      Estados Unidos, cada vez que haya que entrar desde ac&aacute; hay que molestar a esa persona.</li>''',
        u'''    <li><b>No poner el segundo factor por mensaje de texto.</b> El c&oacute;digo quedar&iacute;a en el tel&eacute;fono
      equivocado.</li>''')
s = rep(s, u'''    <li><b>No registrarse con &laquo;Continuar con Google&raquo; ni &laquo;Continuar con Apple&raquo;.</b>
      Deja la cuenta atada a una cuenta de Google o Apple que no controlamos.</li>''',
        u'''    <li><b>No registrarse con &laquo;Continuar con Google&raquo; ni con Apple.</b> Deja la cuenta
      atada a algo que no controlamos.</li>''')
s = rep(s, u'''    <li><b>No usar VPN.</b> Ni para crear ni para entrar. Es la forma m&aacute;s r&aacute;pida de que TikTok
      limite la cuenta.</li>''',
        u'''    <li><b>No usar VPN.</b> Ni para crear ni para entrar.</li>''')
s = rep(s, u'''    <li><b>No publicar nada todav&iacute;a.</b> Las cuentas se crean y se dejan quietas hasta que est&eacute;
      el material listo. La primera publicaci&oacute;n marca el arranque del calendario.</li>''',
        u'''    <li><b>No publicar nada todav&iacute;a.</b> La primera publicaci&oacute;n marca el arranque del calendario.</li>''')
io.open(p, "w", encoding="utf-8").write(s)
print("cuentas: directo a los pasos")
