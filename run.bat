@echo off
echo 🚀 Build e avvio del progetto con Docker Compose

docker-compose build
if ERRORLEVEL 1 (
    echo ❌ Errore nella build
    exit /b 1
)

docker-compose up -d
if ERRORLEVEL 1 (
    echo ❌ Errore nell'avvio dei container
    exit /b 1
)

echo ✅ Tutto avviato correttamente!
pause
