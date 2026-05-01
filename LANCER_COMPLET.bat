@echo off
chcp 65001 >nul
echo.
echo ============================================
echo  Crypto Screening — Run COMPLET (~400 tokens)
echo  Duree estimee : 45-60 minutes
echo  Laisse cette fenetre ouverte.
echo ============================================
echo.
python --version >nul 2>&1
if errorlevel 1 (echo [ERREUR] Python non trouve. & pause & exit /b 1)
cd /d "%~dp0scripts"
python run_pipeline.py
echo.
echo Run complet termine. Ouvre report.md et dashboard.html.
pause
