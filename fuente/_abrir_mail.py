# -*- coding: utf-8 -*-
"""Abre Gmail con el mail cargado. Chrome directo: por cmd los & cortan la URL."""
import io, os, subprocess
try:
    from urllib.parse import quote
except ImportError:
    from urllib import quote

SUBJECT = u"Pauta de los 5 cortos: propuesta de cu\u00e1ndo gastarla"
BODY = io.open("_mailbody.txt", encoding="utf-8").read()

url = (u"https://mail.google.com/mail/u/0/?view=cm&fs=1&tf=1&su=%s&body=%s"
       % (quote(SUBJECT.encode("utf-8"), safe=""),
          quote(BODY.encode("utf-8"), safe="")))

CH = [os.path.join(os.environ.get("ProgramFiles", r"C:\Program Files"),
                   "Google", "Chrome", "Application", "chrome.exe"),
      os.path.join(os.environ.get("ProgramFiles(x86)", r"C:\Program Files (x86)"),
                   "Google", "Chrome", "Application", "chrome.exe")]
exe = next((c for c in CH if os.path.exists(c)), None)
print("largo de la url:", len(url), "| chrome:", bool(exe))
if exe:
    subprocess.Popen([exe, url])
else:
    os.startfile(url)
