@echo off
chcp 65001 > nul
echo ============================================
echo  Programmation de la tâche quotidienne
echo  Crypto Screening — 08h00 chaque jour
echo ============================================
echo.

set SCRIPT="%~dp0LANCER_COMPLET.bat"

schtasks /create ^
  /tn "Crypto Screening Quotidien" ^
  /tr "cmd /c %SCRIPT%" ^
  /sc daily ^
  /st 08:00 ^
  /ru "%USERNAME%" ^
  /f

if %ERRORLEVEL% EQU 0 (
    echo.
    echo [OK] Tache planifiee avec succes !
    echo      Le pipeline tournera chaque matin a 08h00.
    echo      Ton PC doit etre allume et debloque a cette heure.
    echo.
    echo Pour verifier : Planificateur de taches Windows
    echo   ^> chercher "Crypto Screening Quotidien"
    echo.
    echo Pour supprimer la tache :
    echo   schtasks /delete /tn "Crypto Screening Quotidien" /f
) else (
    echo.
    echo [ERREUR] La planification a echoue.
    echo Essaie de lancer ce fichier en tant qu'administrateur.
)

pause
