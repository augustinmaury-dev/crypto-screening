@echo off
chcp 65001 >nul
echo.
echo ============================================
echo  Crypto Screening - Run pilote 30 tokens
echo ============================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo [ERREUR] Python n'est pas installe.
    echo Telecharge-le sur https://python.org/downloads
    pause & exit /b 1
)

cd /d "%~dp0scripts"

echo Lancement en cours - les logs s'affichent ci-dessous...
echo.

python -X utf8 run_pipeline.py --pilot 30 --no-cg-detail

echo.
if exist "..\report.md" (
    echo ============================================
    echo  Succes ! Fichiers generes.
    echo  - report.md
    echo  - data\computed\scores_*.csv
    echo  - dashboard.html
    echo ============================================
) else (
    echo ============================================
    echo  Le report.md n'a pas ete genere.
    echo  Relisez les logs ci-dessus pour l'erreur.
    echo ============================================
)
echo.
pause
