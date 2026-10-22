# -*- coding: utf-8 -*-
"""Titulos de la pagina de call to action: mas grandes y con los logos."""
import io

p = "gen_cta.py"
s = io.open(p, encoding="utf-8").read()

def rep(a, b, n=1):
    global s
    assert a in s, a[:90]
    s = s.replace(a, b, n)

ICONOS = u'''YT = (u'<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#FF0033" d="M23.5 6.2a3 3 0 0 0-2.1-2.1'
      u'C19.5 3.5 12 3.5 12 3.5s-7.5 0-9.4.6A3 3 0 0 0 .5 6.2 31 31 0 0 0 0 12a31 31 0 0 0 .5 5.8 3 3 0 0 0 '
      u'2.1 2.1c1.9.6 9.4.6 9.4.6s7.5 0 9.4-.6a3 3 0 0 0 2.1-2.1A31 31 0 0 0 24 12a31 31 0 0 0-.5-5.8z"/>'
      u'<path fill="#0F1418" d="M9.5 15.6 15.8 12 9.5 8.4z"/></svg>')
TT = (u'<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#E7EDF2" d="M16.6 5.8a4.3 4.3 0 0 1-1-2.8h-3.3'
      u'v13.2a2.6 2.6 0 1 1-1.9-2.5v-3.3a5.9 5.9 0 1 0 5.2 5.8V9.7a7.5 7.5 0 0 0 4.4 1.4V7.8a4.3 4.3 0 0 1-3.4-2z"/></svg>')
IG = (u'<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="#E1306C" stroke-width="2">'
      u'<rect x="2.5" y="2.5" width="19" height="19" rx="5.5"/><circle cx="12" cy="12" r="4.2"/>'
      u'<circle cx="17.6" cy="6.4" r="1.2" fill="#E1306C" stroke="none"/></svg>')

'''
rep(u'def frame(path, t):', ICONOS + u'def frame(path, t):')

rep(u'''  <div class="cols">
    <div>
      <p class="lbl">Call to action &middot; YouTube Shorts</p>
      <ul class="en">%s</ul>
      <p class="lbl">Call to action &middot; TikTok e Instagram</p>
      <ul class="en">%s</ul>
    </div>
    <div>
      <p class="lbl">Caption</p>
      <ul class="en cap">%s</ul>
    </div>
  </div>
</article>
''' + u"' % (im, titulo, li(shorts), li(tt), li(caps))",
    u'''  <div class="cols">
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
''' + u"' % (im, titulo, YT, li(shorts), TT, IG, li(tt), li(caps))")

rep(u'''.lbl{font-size:11.5px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--dim);margin:0 0 10px}
.cols>div>.lbl:nth-of-type(2){margin-top:22px}
ul.en{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:7px}
ul.en li{background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--teal);
  border-radius:8px;padding:11px 14px;font-size:15.5px;color:var(--ink)}
ul.en.cap li{border-left-color:var(--blue);color:var(--ink2)}''',
    u'''.lbl{display:flex;align-items:center;gap:9px;margin:0 0 13px;padding-bottom:10px;
  border-bottom:1px solid var(--line)}
.lbl svg{width:22px;height:22px;flex:none;display:block}
.lbl .k{font-size:11.5px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--dim)}
.lbl .p{font-size:20px;font-weight:700;letter-spacing:-.015em;color:var(--ink)}
.cols>div>.lbl:nth-of-type(2){margin-top:26px}
ul.en{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:7px}
ul.en li{background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--teal);
  border-radius:8px;padding:11px 14px;font-size:15.5px;color:var(--ink)}
ul.en.tt li{border-left-color:var(--blue)}
ul.en.cap li{border-left-color:var(--warn);color:var(--ink2)}''')

io.open(p, "w", encoding="utf-8").write(s)
print("titulos con logos")
