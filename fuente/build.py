# -*- coding: utf-8 -*-
"""Arma el sitio: navegacion comun, logo, y copia todo al repo."""
import io, json, os, re, shutil, subprocess

SITE = u"https://santiagotereso.github.io/brain-syrup/"
AQUI = os.path.dirname(os.path.abspath(__file__))
_padre = os.path.dirname(AQUI)
REPO = (_padre if os.path.isdir(os.path.join(_padre, "posteos"))
        else os.path.join(os.path.expanduser("~"), "SHIET", "brain-syrup"))
LOGO = json.load(io.open("_assets.json", encoding="utf-8"))["logo"]

PAGS = [(u"Objetivo", u""),
        (u"Seguimiento", u"seguimiento/"),
        (u"Videos", u"videos/"),
        (u"Picadora", u"picadora/"),
        (u"Cuentas", u"cuentas/"),
        (u"Mejor call to action", u"cta/"),
        (u"Posteos", u"posteos/"),
        (u"Material de estudio", u"referencias/")]

def nav(act, indent=u"    "):
    o = []
    for nm, sub in PAGS:
        on = u" on" if nm == act else u""
        ac = u' aria-current="page"' if nm == act else u""
        o.append(u'%s<a class="tab%s" href="%s%s"%s>%s</a>' % (indent, on, SITE, sub, ac, nm))
    return u"\n".join(o)

def bloque(act):
    return u'  <nav class="nav">\n%s\n  </nav>' % nav(act)

def poner(texto, act, py=False):
    n = bloque(act)
    if py:
        n = n.replace("\\", "\\\\")
    return re.sub(r'(?s)  <nav class="nav">.*?</nav>', lambda m: n, texto, count=1)

# --- documento ---
g = io.open("gen_plan.py", encoding="utf-8").read()
io.open("gen_plan.py", "w", encoding="utf-8").write(poner(g, u"Objetivo", py=True))
r = subprocess.run(["python", "gen_plan.py"], capture_output=True, text=True,
                   env=dict(os.environ, PYTHONIOENCODING="utf-8"))
print((r.stdout or r.stderr).strip()[:160])

# --- seguimiento: hub + una pagina por red ---
r = subprocess.run(["python", "gen_seguimiento.py"], capture_output=True, text=True,
                   env=dict(os.environ, PYTHONIOENCODING="utf-8"))
print((r.stdout or r.stderr).strip()[:300])

# --- paginas sueltas ---
SUELTAS = [("picadora_src.html", "picadora.html", u"Picadora"),
           ("referencias_src.html", "referencias.html", u"Material de estudio"),
           ("cuentas_src.html", "cuentas.html", u"Cuentas")]
for src, out, act in SUELTAS:
    t = io.open(src, encoding="utf-8").read()
    if u'<nav class="nav">__NAV__</nav>' in t:
        t = t.replace(u'<nav class="nav">__NAV__</nav>', bloque(act).strip())
    else:
        t = poner(t, act)
    io.open(src, "w", encoding="utf-8").write(t)
    io.open(out, "w", encoding="utf-8").write(
        t.replace(u"__LOGO__", LOGO).replace(u"__SITE__", SITE))
    print("%s: %d KB" % (out, os.path.getsize(out) // 1024))

# --- al repo ---
for a, b in [("plan-brain-syrup.html", "index.html"), ("picadora.html", "picadora/index.html"),
             ("referencias.html", "referencias/index.html"),
             ("cuentas.html", "cuentas/index.html"), ("cta.html", "cta/index.html")]:
    d = os.path.join(REPO, b)
    if not os.path.isdir(os.path.dirname(d)):
        os.makedirs(os.path.dirname(d))
    shutil.copyfile(a, d)
if os.path.isdir("videos"):
    dv = os.path.join(REPO, "videos")
    if os.path.isdir(dv):
        shutil.rmtree(dv)
    shutil.copytree("videos", dv)
print("repo listo")
