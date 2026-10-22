# Actualizar los números de Instagram

Procedimiento que corre el acceso directo `Actualizar Instagram.bat`, **desde la máquina
de Los Ángeles**, que es la que tiene la sesión de Instagram abierta.

Esta máquina toca **un solo archivo**: `fuente/datos/instagram.json`. Nada más.
YouTube y TikTok los actualiza la otra computadora, así que no se pisan nunca.

Cuenta: `_BrainSyrup` · Reels publicados el 17 y el 21 de octubre de 2026.

## 0. Traer lo último y verificar la sesión

    cd <carpeta del repo>
    git pull

Todas las llamadas al navegador van **con `browser_id: "instagram"`**, sin excepción.

Eso es obligatorio y es el detalle que hace que esto funcione. El navegador sin nombre
es distinto en cada corrida y arranca sin sesión; el que se llama `instagram` es siempre
el mismo y conserva el login entre corridas. Si usás el sin nombre, vas a ver la pantalla
de "Log In" aunque la cuenta esté perfectamente logueada.

Abrí, con ese `browser_id`:

    https://www.instagram.com/_brainsyrup/

Si aparece "Log In" o "Sign Up", **no cambies nada y no publiques**: avisá en pantalla que
hay que entrar a Instagram en el navegador `instagram` del panel de PATAPIM, y terminá.
Números viejos presentados como nuevos son peor que no actualizar.

## 1. Leer cada reel

Entrá al perfil, abrí cada reel y andá a sus estadísticas. De cada uno hacen falta dos vistas:

**Solapa "All"** — el total del reel, pauta incluida:
- `vistas` ← Views
- `inter` ← Interactions (el total: likes + saves + shares + comments)
- `seg` ← Profile activity → Follows

**Solapa "Ad"** — solo lo que trajo la promoción:
- `pagas` ← Views
- `perfil` ← Profile activity → Profile visits
- `gasto` ← Details → Spend (el primer número: lo gastado, no el presupuesto)

Si un reel no tiene solapa "Ad" porque nunca se promocionó, poné `pagas: 0`, `gasto: 0`
y `perfil: 0`, y dejá `vistas`, `inter` y `seg` con lo de "All".

Los cinco reels, en el orden en que están hoy en el archivo:

| id | reel | duración |
|---|---|---|
| seniors | Which power would you pick? | 0:23 |
| iphone-1960 | How much space would an iPhone take in 1960? | 0:19 |
| gravity | Most will last under a minute. | 0:24 |
| algo | This is your boss. Thoughts? | 0:25 |
| gianni | He'll multiply your followers. Call 1800-GIANNI | 0:40 |

El `id` es el que enlaza cada fila con su miniatura en la página: **no lo cambies**.

## 2. Ubicación del público

En la solapa "Ad" de cualquier reel promocionado, abajo de todo: **Who saw your ad →
Top Locations**. Va a `paises` (nombre y porcentaje) y la segmentación a `ubicacion`.
Si las promociones siguen apuntando a Los Ángeles, eso no cambia.

Para acentos y eñes usá entidades HTML: `Los &Aacute;ngeles`, `M&eacute;xico`.

## 3. Escribir el archivo

Editá `fuente/datos/instagram.json`. Actualizá también el campo `leido` con la fecha de hoy
en castellano, por ejemplo `"22 de octubre de 2026"`.

Si aparece un reel nuevo que no está en la lista, agregalo con su `id` nuevo — y avisá en
el resumen, porque también hay que sumarle la miniatura en `posteos/media/thumb-<id>-sm.webp`
desde la otra computadora.

## 4. Regenerar y publicar

    cd fuente
    python gen_seguimiento.py
    cd ..
    git add -A
    git commit -m "Instagram: numeros al <fecha>"
    git pull --rebase
    git push

El `git pull --rebase` antes del push es importante: la otra computadora puede haber
subido cambios de YouTube mientras tanto. Como cada una toca archivos distintos, se
combinan sin conflicto.

**No corras `build.py`** desde esta máquina. Ese script necesita videos pesados que solo
están en la computadora principal. `gen_seguimiento.py` alcanza y se basta solo.

## 5. Terminar

Imprimí un resumen corto: vistas, seguidores y gasto nuevos contra los anteriores, y si
algo no se pudo leer.

## Reglas

- **Siempre `browser_id: "instagram"`.** El navegador sin nombre no tiene la sesión.
- Si un número no se puede leer, **dejá el anterior y decilo**. Nunca inventes ni estimes.
- No toques `datos/youtube.json` ni `datos/tiktok.json`. No son de esta máquina.
- No toques ningún otro archivo del repo.
