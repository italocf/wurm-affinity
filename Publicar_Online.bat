@echo off
chcp 65001 > nul
title Publicador Online - Wurm Affinity Calculator

echo ========================================================
echo   Publicando Calculadora no link oficial...
echo ========================================================
echo.

if not exist dist mkdir dist
copy /Y index.html dist\index.html > nul

echo Enviando para: https://wurm-affinity.surge.sh
call npx.cmd --yes surge dist --domain wurm-affinity.surge.sh --token 351829a776e656d9417b460cc1539100

echo.
echo Atualizando repositorio no GitHub...
git add index.html banco_de_dados.json wurm_affinity.db
git commit -m "update: site content updated" > nul 2>&1
git push origin main > nul 2>&1

echo.
echo ========================================================
echo   Sucesso! O site esta online e atualizado em:
echo   https://wurm-affinity.surge.sh
echo ========================================================
pause
