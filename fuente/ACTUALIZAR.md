# Actualizar los números de Brain Syrup

Procedimiento que corre el acceso directo `Actualizar Brain Syrup.bat` del Escritorio.
Objetivo: releer YouTube y Google Ads, rehacer las páginas de Seguimiento y publicarlas.

Esta máquina toca **un solo archivo**: `fuente/datos/youtube.json`. Nada más.
Instagram lo actualiza la computadora de Los Ángeles y TikTok entra a mano, así que
las dos nunca se pisan.

Generador: `fuente/gen_seguimiento.py` · Repo: la carpeta que contiene a `fuente/`
Canal: `UC2bdgvi3A9nPdpFN0uGC23g` · Cuenta de Ads: ocid `8616256713`

## 0. Traer lo último y verificar la sesión

    git pull


Navegá con el navegador de PATAPIM (sin `browser_id`, el que tiene la sesión de Google) a:

    https://studio.youtube.com/channel/UC2bdgvi3A9nPdpFN0uGC23g/analytics/tab-overview/period-default

Si la URL termina en `accounts.google.com` o el texto dice **"Verify it's you"**, la sesión
se cortó. En ese caso **no publiques nada**: dejá el sitio como está, escribí en pantalla
que hay que volver a loguearse en el panel de PATAPIM, y terminá. Números viejos presentados
como nuevos son peor que no actualizar.

## 1. YouTube Shorts → `shorts` de `datos/youtube.json`

Vistas, retención y suscriptores, desde el principio:

    https://studio.youtube.com/channel/UC2bdgvi3A9nPdpFN0uGC23g/analytics/tab-overview/period-default/explore?entity_type=CHANNEL&entity_id=UC2bdgvi3A9nPdpFN0uGC23g&time_period=lifetime&explore_type=TABLE_AND_CHART&metric=VIEWS&granularity=DAY&t_metrics=VIEWS&t_metrics=AVERAGE_WATCH_TIME&t_metrics=AVERAGE_WATCH_PERCENTAGE&t_metrics=SUBSCRIBERS_NET_CHANGE&t_metrics=RATINGS_LIKES&dimension=VIDEO&o_column=VIEWS&o_direction=ANALYTICS_ORDER_DIRECTION_DESC

Leé con `browser_content` (type text). El orden de cada fila es:
duración, título, vistas, % del total, duración promedio, porcentaje promedio reproducido,
suscriptores, %, me gusta, %.

El porcentaje pago de cada short sale de su propia pestaña de alcance, campo
"Publicidad de YouTube":

    https://studio.youtube.com/video/<ID>/analytics/tab-reach_viewers/period-default

IDs de los shorts:

| id | video | ID de YouTube |
|---|---|---|
| seniors | Which power would you pick? | O3qoxAqGqvk |
| algo | This is your boss. Thoughts? | gCiIwjoYCuo |
| gravity | Most will last under a minute. | u2rL0p_NdhU |
| iphone-1960 | How much space would an iPhone take in 1960? | Be7CbfUnJt4 |
| gianni | Call 1800-GIANNI | 2sYSE3wv5jQ |

## 2. Costo por short → campo `costo` de cada short, y `gastado`

    https://ads.google.com/aw/ads?campaignId=24371544474&ocid=8616256713

La tabla trae una fila por anuncio con impresiones, vistas de TrueView, CPV y **Costo**.
Cada fila nombra abajo el video al que corresponde. El total de la campaña es `YT_GASTADO`.
Si la campaña terminó y hay otra nueva, sumá las campañas desde
`https://ads.google.com/aw/campaigns?ocid=8616256713` y actualizá también `presupuesto`.

## 3. Países → `paises`

    https://studio.youtube.com/channel/UC2bdgvi3A9nPdpFN0uGC23g/analytics/tab-build_your_audience/period-default/explore?entity_type=CHANNEL&entity_id=UC2bdgvi3A9nPdpFN0uGC23g&time_period=4_weeks&explore_type=TABLE_AND_CHART&metric=VIEWS&granularity=DAY&t_metrics=VIEWS&t_metrics=WATCH_TIME&t_metrics=SUBSCRIBERS_NET_CHANGE&dimension=COUNTRY&o_column=VIEWS&o_direction=ANALYTICS_ORDER_DIRECTION_DESC

Dejá Estados Unidos y "Otros" (el total menos Estados Unidos), como está ahora.

## 4. YouTube Videos → `episodios`

Misma tabla del punto 1, filas de los episodios largos. El porcentaje pago sale de la
pestaña de alcance de cada uno:

| id | episodio | ID |
|---|---|---|
| 5UslxvWHEjw | They understand The Internet | 5UslxvWHEjw |
| s4N5KpNrNT8 | Why Are People Afraid of This? | s4N5KpNrNT8 |
| WipHGSwLZLU | Gravity undo | WipHGSwLZLU |
| PTaXQ2x57Kk | SUPER SENIORS | PTaXQ2x57Kk |
| i9-pZxyqAQk | An iphone built with 1960s Tech | i9-pZxyqAQk |

El gasto de estas campañas **no está en esta cuenta de Ads**. Si sigue sin estar, dejá el
bloque "Gastado / No visible" como está. No lo estimes.

## 5. TikTok e Instagram

**No se tocan.** Esos números entran a mano desde screenshots, porque se leen con otra
cuenta y desde otra computadora. No toques `datos/instagram.json` ni `datos/tiktok.json`.

## 6. Publicar

    cd fuente && python build.py && cd ..
    git add -A
    git commit -m "Seguimiento: numeros al <fecha>"
    git pull --rebase
    git push

El `git pull --rebase` antes del push es importante: la máquina de Los Ángeles puede
haber subido cambios de Instagram mientras tanto. Como cada una toca archivos distintos,
se combinan sin conflicto.

La marca "Leído el ..." de las páginas se pone sola con la fecha de la corrida.

Al terminar, imprimí en pantalla un resumen corto: qué cambió respecto de los números
anteriores (vistas, suscriptores, gastado) y si algo no se pudo leer.

## Reglas

- Si un número no se puede leer, **dejá el anterior y decilo**. Nunca inventes ni estimes.
- No toques nada fuera de `datos/youtube.json` salvo que el procedimiento lo pida.
- Si YouTube o Ads cambiaron de layout y la lectura no coincide con lo esperado, no publiques:
  informá qué pasó.
