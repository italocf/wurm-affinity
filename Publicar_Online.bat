@echo off
chcp 65001 > nul
title Publicador Online - Wurm Affinity Calculator

echo ========================================================
echo   Publicando Calculadora de Afinidade na Web...
echo ========================================================
echo.

if not exist dist mkdir dist
copy /Y index.html dist\index.html > nul

echo Enviando para a nuvem...
call npx --yes @shipstatic/ship dist

echo.
echo ========================================================
echo   Publicação concluída!
echo ========================================================
pause
