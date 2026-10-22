# -*- coding: utf-8 -*-
"""Pagina de call to action: por video, por plataforma, y los captions aparte."""
import base64, io, json, os, subprocess

DIR = os.path.join(os.path.expanduser("~"), "Desktop", "BRAIN SYRUP", "videos", "LQ")
SITE = u"https://santiagotereso.github.io/brain-syrup/"
LOGO = json.load(io.open("_assets.json", encoding="utf-8"))["logo"]
OUT = "cta.html"

VIDEOS = [
 ("An iPhone built with 1960s tech",
  "An iphone built with 1960s Tech. Guess how big_.mp4", 43.5,
  [u"Watch the full episode on the channel",
   u"The answer is one and a half Manhattans. Full episode on the channel",
   u"We did the math. Full episode on the channel",
   u"Is that good for humanity? Full episode on the channel"],
  [u"Watch the full episode on YouTube, link in bio",
   u"The answer is one and a half Manhattans. Full episode on YouTube, link in bio",
   u"We did the math. Full episode on YouTube, link in bio",
   u"Is that good for humanity? Full episode on YouTube, link in bio"],
  [u"Guess how big. Comment before you watch.",
   u"How much space would an iPhone take in 1960?",
   u"One and a half Manhattans. We&rsquo;re not kidding.",
   u"An iPhone with 1960s tech would cover 89 square kilometers."]),

 ("They understand The Internet",
  "They understand The Internet. Apparently you don't.mp4", 1.3,
  [u"Watch the full episode on the channel",
   u"Meet your boss. Full episode on the channel",
   u"A single day produces 500 years of content. Full episode on the channel",
   u"The whole thing is on the channel"],
  [u"Watch the full episode on YouTube, link in bio",
   u"Meet your boss. Full episode on YouTube, link in bio",
   u"A single day produces 500 years of content. Full episode on YouTube, link in bio",
   u"The whole thing is on YouTube, link in bio"],
  [u"Who decides what you see? Fight us in the comments.",
   u"This is your boss. Thoughts?",
   u"A single day produces 500 years of content. You see 0.00005%.",
   u"Say hi to the algorithm."]),

 ("SUPER SENIORS",
  "SUPER SENIORS. Bizarre animation. You've never felt THIS young.mp4", 139.0,
  [u"FULL EPISODE ON THE CHANNEL",
   u"THE REST IS ON THE CHANNEL",
   u"FOUR MINUTES OF RETIRED SUPERHEROES. ON THE CHANNEL",
   u"WATCH THE FULL EPISODE ON THE CHANNEL"],
  [u"FULL EPISODE ON YOUTUBE. LINK IN BIO",
   u"THE REST IS ON YOUTUBE. LINK IN BIO",
   u"FOUR MINUTES OF RETIRED SUPERHEROES. YOUTUBE, LINK IN BIO",
   u"WATCH THE FULL EPISODE ON YOUTUBE. LINK IN BIO"],
  [u"Which power would you pick?",
   u"Five retired superheroes. Pick one.",
   u"Indestructible muscle stiffness. Unlimited skin deployment. Immortality.",
   u"Their ailments are their superpowers."]),

 ("Why Are People Afraid of This?",
  "Why Are People Afraid of This_.mp4", 14.0,
  [u"Watch the full episode on the channel",
   u"There&rsquo;s nine more minutes of this on the channel",
   u"We explain why on the channel",
   u"Knees. Balloons. Paper. Full episode on the channel"],
  [u"Watch the full episode on YouTube, link in bio",
   u"There&rsquo;s nine more minutes of this on YouTube, link in bio",
   u"We explain why on YouTube, link in bio",
   u"Knees. Balloons. Paper. Full episode on YouTube, link in bio"],
  [u"Tell us the dumbest thing you&rsquo;re afraid of.",
   u"Knees. Balloons. Paper. Which one is yours?",
   u"You can fear almost anything. Really?",
   u"Worry is a machine that produces pain and solves nothing."]),

 ("Gravity undo",
  "Gravity undo_ Most will last under a minute.mp4", 40.0,
  [u"Watch the full episode on the channel",
   u"Who dies last? The answer is on the channel",
   u"There&rsquo;s eleven more minutes of this on the channel",
   u"The answer is in the full episode. On the channel"],
  [u"Watch the full episode on YouTube, link in bio",
   u"Who dies last? The answer is on YouTube, link in bio",
   u"There&rsquo;s eleven more minutes of this on YouTube, link in bio",
   u"The answer is in the full episode. YouTube, link in bio"],
  [u"Try it: circle with one hand, square with the other. Tell us how it went.",
   u"If gravity stopped right now, who dies first?",
   u"Most will last under a minute.",
   u"The fastest death isn&rsquo;t suffocation. It&rsquo;s inertia."]),
]

YT = (u'<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#FF0033" d="M23.5 6.2a3 3 0 0 0-2.1-2.1'
      u'C19.5 3.5 12 3.5 12 3.5s-7.5 0-9.4.6A3 3 0 0 0 .5 6.2 31 31 0 0 0 0 12a31 31 0 0 0 .5 5.8 3 3 0 0 0 '
      u'2.1 2.1c1.9.6 9.4.6 9.4.6s7.5 0 9.4-.6a3 3 0 0 0 2.1-2.1A31 31 0 0 0 24 12a31 31 0 0 0-.5-5.8z"/>'
      u'<path fill="#0F1418" d="M9.5 15.6 15.8 12 9.5 8.4z"/></svg>')
TT = (u'<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#E7EDF2" d="M16.6 5.8a4.3 4.3 0 0 1-1-2.8h-3.3'
      u'v13.2a2.6 2.6 0 1 1-1.9-2.5v-3.3a5.9 5.9 0 1 0 5.2 5.8V9.7a7.5 7.5 0 0 0 4.4 1.4V7.8a4.3 4.3 0 0 1-3.4-2z"/></svg>')
IG = (u'<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="#E1306C" stroke-width="2">'
      u'<rect x="2.5" y="2.5" width="19" height="19" rx="5.5"/><circle cx="12" cy="12" r="4.2"/>'
      u'<circle cx="17.6" cy="6.4" r="1.2" fill="#E1306C" stroke="none"/></svg>')

def frame(path, t):
    r = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(t), "-i", path, "-frames:v", "1",
                        "-vf", "scale=560:-2", "-q:v", "4", "-f", "image2", "-vcodec", "mjpeg", "-"],
                       capture_output=True)
    return u"data:image/jpeg;base64," + base64.b64encode(r.stdout).decode()

def nav():
    its = [(u"Objetivo", u""), (u"Seguimiento", u"seguimiento/"), (u"Videos", u"videos/"),
           (u"Picadora", u"picadora/"), (u"Cuentas", u"cuentas/"),
           (u"Mejor call to action", u"cta/"), (u"Posteos", u"posteos/"), (u"Material de estudio", u"referencias/")]
    o = [u'  <nav class="nav">']
    for nm, sub in its:
        on = u" on" if nm == u"Mejor call to action" else u""
        ac = u' aria-current="page"' if on else u""
        o.append(u'    <a class="tab%s" href="%s%s"%s>%s</a>' % (on, SITE, sub, ac, nm))
    o.append(u"  </nav>")
    return chr(10).join(o)

bloques = u""
for titulo, arch, t, shorts, tt, caps in VIDEOS:
    im = frame(os.path.join(DIR, arch), t)
    print(u"%-34s %d KB" % (titulo, len(im) // 1024))
    li = lambda xs: u"".join(u"<li>%s</li>" % x for x in xs)
    bloques += u'''<article class="v">
  <div class="vh"><img src="%s" alt=""><h3>%s</h3></div>
  <div class="cols">
    <div>
      <p class="lbl">%s<span class="k">Call to action</span><span class="p">YouTube Shorts</span></p>
      <ul class="en yt">%s</ul>
      <p class="lbl">%s%s<span class="k">Call to action</span><span class="p">TikTok e Instagram</span></p>
      <ul class="en tt">%s</ul>
    </div>
    <div>
      <p class="lbl"><span class="p">Caption</span></p>
      <ul class="en cap">%s</ul>
    </div>
  </div>
</article>
''' % (im, titulo, YT, li(shorts), TT, IG, li(tt), li(caps))

HTML = u'''<title>Call to action</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap">
<style>
:root{color-scheme:dark;
  --bg:#0F1418;--panel:#161D23;--panel2:#111920;--line:#242E36;--line2:#38454F;
  --ink:#E7EDF2;--ink2:#AFBCC7;--dim:#7A8995;--teal:#2DD4BF;--blue:#93B4FD;--warn:#E9B949;
  --ui:"Inter","Segoe UI",system-ui,-apple-system,Helvetica,Arial,sans-serif;
  --mono:'JetBrains Mono',ui-monospace,Consolas,monospace}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--ui);font-size:15px;line-height:1.55}
.app{max-width:1600px;margin:0 auto;padding-block:20px 64px;padding-left:20px;padding-right:20px}
header{display:flex;align-items:center;gap:22px;flex-wrap:wrap;padding-bottom:20px;border-bottom:1px solid var(--line)}
.logo{flex:none;width:88px;height:88px;border-radius:50%;display:block}
header>.id{min-width:0}
h1{margin:0;font-size:clamp(30px,4.2vw,46px);font-weight:800;letter-spacing:-.03em;line-height:1.02}
.h1b{color:var(--teal)}
.kicker{font-size:12.5px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--teal);margin:0 0 10px}
.nav{margin-left:auto;display:flex;gap:8px;flex-wrap:wrap}
.tab{text-decoration:none;border:1px solid var(--line2);color:var(--dim);font-size:13.5px;font-weight:600;padding:8px 16px;border-radius:999px;white-space:nowrap}
.tab:hover{color:var(--ink);border-color:var(--teal)}
.tab.on{background:var(--teal);border-color:var(--teal);color:#06211E}

.v{margin-top:34px;border-top:1px solid var(--line);padding-top:26px}
.v:first-of-type{border-top:0}
.vh{display:flex;align-items:center;gap:18px;flex-wrap:wrap;margin-bottom:18px}
.vh img{width:240px;aspect-ratio:16/9;object-fit:cover;border-radius:9px;border:1px solid var(--line);display:block}
.vh h3{margin:0;font-size:24px;font-weight:700;letter-spacing:-.02em}
.cols{display:grid;grid-template-columns:minmax(0,1.25fr) minmax(0,1fr);gap:24px;align-items:start}
.lbl{display:flex;align-items:center;gap:9px;margin:0 0 13px;padding-bottom:10px;
  border-bottom:1px solid var(--line)}
.lbl svg{width:22px;height:22px;flex:none;display:block}
.lbl .k{font-size:11.5px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--dim)}
.lbl .p{font-size:20px;font-weight:700;letter-spacing:-.015em;color:var(--ink)}
.cols>div>.lbl:nth-of-type(2){margin-top:26px}
ul.en{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:7px}
ul.en li{background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--teal);
  border-radius:8px;padding:11px 14px;font-size:15.5px;color:var(--ink)}
ul.en.tt li{border-left-color:var(--blue)}
ul.en.cap li{border-left-color:var(--warn);color:var(--ink2)}
@media(max-width:900px){.cols{grid-template-columns:minmax(0,1fr)}}
</style>

<div class="app">
<header>
  <img class="logo" src="__LOGO__" alt="Logo de Brain Syrup">
  <div class="id">
    <p class="kicker">Mejor call to action</p>
    <h1>Brain Syrup <span class="h1b">YouTube Channel</span></h1>
  </div>
__NAV__
</header>

__BLOQUES__
</div>
'''
HTML = (HTML.replace(u"__LOGO__", LOGO).replace(u"__NAV__", nav())
            .replace(u"__BLOQUES__", bloques))
io.open(OUT, "w", encoding="utf-8").write(HTML)
print(u"escrito %s | %d KB" % (OUT, len(HTML) // 1024))
