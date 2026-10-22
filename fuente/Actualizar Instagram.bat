@echo off
setlocal
title Actualizar Instagram
rem --------------------------------------------------------------------
rem  Corre en la maquina de Los Angeles, la que tiene Instagram logueado.
rem  Copia este archivo al Escritorio y, si hace falta, corregi la linea
rem  de REPO para que apunte a donde clonaste brain-syrup.
rem --------------------------------------------------------------------

set "REPO=%USERPROFILE%\brain-syrup"
if not exist "%REPO%\fuente\gen_seguimiento.py" set "REPO=%USERPROFILE%\SHIET\brain-syrup"

if not exist "%REPO%\fuente\gen_seguimiento.py" (
  echo.
  echo   No encuentro el repo. Lo busque en:
  echo     %USERPROFILE%\brain-syrup
  echo     %USERPROFILE%\SHIET\brain-syrup
  echo.
  echo   Edita este archivo y corregi la linea que dice "set REPO=".
  echo.
  pause
  exit /b 1
)

cd /d "%REPO%"
set "LOG=%~dp0Actualizar Instagram - ultima corrida.txt"

echo.
echo   ACTUALIZAR INSTAGRAM
echo   --------------------
echo.
echo   Repo: %REPO%
echo   Leyendo las estadisticas de Instagram...
echo   Tarda unos minutos. No cierres esta ventana.
echo.

git pull --rebase

claude --print ^
 "Segui el procedimiento de fuente/ACTUALIZAR-INSTAGRAM.md, de principio a fin, sin pedirme confirmacion en ningun paso. Es una corrida desatendida: nadie va a contestar preguntas. Si la sesion de Instagram esta cortada, no publiques nada y decilo. Termina con un resumen corto de que cambio respecto de los numeros anteriores." ^
 --permission-mode acceptEdits ^
 --allowedTools "Bash" "Read" "Write" "Edit" "Glob" "Grep" "mcp__patapim-browser__browser_navigate" "mcp__patapim-browser__browser_content" "mcp__patapim-browser__browser_evaluate" "mcp__patapim-browser__browser_screenshot" "mcp__patapim-browser__browser_click" "mcp__patapim-browser__browser_scroll" > "%LOG%" 2>&1

set "RC=%errorlevel%"

echo.
echo   --------------------
type "%LOG%"
echo.
echo   --------------------
if not "%RC%"=="0" (
  echo   LA CORRIDA FALLO ^(codigo %RC%^). No des por buenos los numeros.
) else (
  echo   Listo.
)
echo   El detalle quedo en:
echo   %LOG%
echo.
start "" "https://santiagotereso.github.io/brain-syrup/seguimiento/instagram/"
echo.
pause
