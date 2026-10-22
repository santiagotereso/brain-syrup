# -*- coding: utf-8 -*-
"""Como se decide a que pieza ponerle plata: 48 horas organicas y despues la pauta."""
import io

P = "seguimiento_src.html"
s = io.open(P, encoding="utf-8").read()

A = u"<h2>D&oacute;nde se compra la pauta</h2>"
assert A in s and u"Cu&aacute;ndo entra la plata" not in s

NUEVO = u"""<h2>Cu&aacute;ndo entra la plata</h2>
<p class="pie" style="margin:0 0 14px">Las primeras 48 horas no se paga nada. No es ahorrar: es dejar que
el algoritmo elija la pieza antes de gastar en ella.</p>
<div class="tw">
  <table>
    <thead><tr><th>Cu&aacute;ndo</th><th>Qu&eacute; pasa</th><th class="n">Cu&aacute;nto</th></tr></thead>
    <tbody>
      <tr><th>Viernes a domingo</th>
        <td class="txt">Salen las 15 publicaciones. Se miden <b>retenci&oacute;n, guardados y visitas
          al perfil</b>, no vistas.</td>
        <td class="n">$0</td></tr>
      <tr><th>Lunes</th>
        <td class="txt">Se elige la pieza que mejor anduvo sola y se le pone pauta en las tres redes
          a la vez: <b>misma pieza, misma plata, misma semana</b>. Ese es el &uacute;nico modo de que
          el costo por seguidor compare redes y no creatividades.</td>
        <td class="n">$225<span class="sub">$75 por red</span></td></tr>
      <tr><th>La semana siguiente</th>
        <td class="txt">La segunda pieza, o la red que trajo el seguidor m&aacute;s barato.</td>
        <td class="n">$225</td></tr>
      <tr><th>Si ninguna se despega</th>
        <td class="txt">Plan B: $25 en cada una de las cinco, en la red que haya mostrado m&aacute;s
          vida, para forzar una se&ntilde;al.</td>
        <td class="n">$125</td></tr>
    </tbody>
  </table>
</div>
<div class="nota" style="margin-top:16px">
  <p><span class="hl">Por qu&eacute; no desde el minuto cero.</span> Si las 15 publicaciones arrancan
    con plata, todas tienen vistas y ninguna dice cu&aacute;l es buena: se gasta el presupuesto y
    encima se pierde la informaci&oacute;n.</p>
  <p><span class="hl">Porque sale m&aacute;s barato despu&eacute;s.</span> Las plataformas cobran
    menos alcance cuando la pieza ya tiene engagement propio. La misma plata rinde m&aacute;s sobre
    algo que ya funciona que empujando algo fr&iacute;o.</p>
  <p><span class="hl">Porque hay que poder reaccionar.</span> Si el presupuesto se gasta el primer
    d&iacute;a y al tercero una pieza arranca sola, no queda con qu&eacute; empujarla.</p>
</div>

"""

io.open(P, "w", encoding="utf-8").write(s.replace(A, NUEVO + A, 1))
print("listo")
