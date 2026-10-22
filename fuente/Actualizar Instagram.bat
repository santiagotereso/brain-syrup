@echo off
setlocal enabledelayedexpansion
title Actualizar Instagram
rem --------------------------------------------------------------------
rem  Corre en la maquina de Los Angeles, la que tiene Instagram logueado.
rem  Copia este archivo al Escritorio y hace doble clic.
rem --------------------------------------------------------------------

echo.
echo   ACTUALIZAR INSTAGRAM
echo   --------------------
echo.

rem ---- 1. Encontrar el repo -------------------------------------------
set "REPO="
for %%D in ("%USERPROFILE%\brain-syrup" "%USERPROFILE%\SHIET\brain-syrup" "%USERPROFILE%\Documents\brain-syrup" "%USERPROFILE%\Desktop\brain-syrup") do (
  if exist "%%~D\fuente\gen_seguimiento.py" if not defined REPO set "REPO=%%~D"
)
if not defined REPO (
  echo   No encuentro el repo. Lo busque en:
  echo     %USERPROFILE%\brain-syrup
  echo     %USERPROFILE%\SHIET\brain-syrup
  echo     %USERPROFILE%\Documents\brain-syrup
  echo     %USERPROFILE%\Desktop\brain-syrup
  echo.
  echo   Clonalo con:  git clone https://github.com/santiagotereso/brain-syrup.git
  echo   o edita este archivo y agrega tu carpeta en la linea del "for".
  echo.
  pause & exit /b 1
)

rem ---- 2. Encontrar claude --------------------------------------------
set "CLAUDE="
for %%C in (claude.cmd claude.exe claude) do (
  if not defined CLAUDE for /f "delims=" %%P in ('where %%C 2^>nul') do if not defined CLAUDE set "CLAUDE=%%P"
)
for %%D in ("%USERPROFILE%\.local\bin\claude.exe" "%USERPROFILE%\.local\bin\claude" "%USERPROFILE%\AppData\Roaming\npm\claude.cmd" "%LOCALAPPDATA%\Programs\claude\claude.exe") do (
  if not defined CLAUDE if exist "%%~D" set "CLAUDE=%%~D"
)
if not defined CLAUDE (
  echo   No encuentro Claude Code. Abri una terminal y proba escribir:  claude
  echo   Si no responde, hay que instalarlo o volver a abrir la sesion de Windows
  echo   para que tome el PATH.
  echo.
  pause & exit /b 1
)

rem ---- 3. Chequeos rapidos --------------------------------------------
where git >nul 2>&1 || (echo   Falta git. Instalalo y volve a probar. & echo. & pause & exit /b 1)
where python >nul 2>&1 || (echo   Falta Python. Instalalo y volve a probar. & echo. & pause & exit /b 1)

cd /d "%REPO%"
set "LOG=%~dp0Actualizar Instagram - ultima corrida.txt"

echo   Repo:   %REPO%
echo   Claude: %CLAUDE%
echo.
echo   Leyendo las estadisticas de Instagram...
echo   Tarda unos minutos. No cierres esta ventana.
echo.

git pull --rebase

"%CLAUDE%" --print ^
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
