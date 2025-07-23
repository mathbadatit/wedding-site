@echo off
if "%1"=="" (
    echo ❗ Devi specificare il file di backup
    pause
    exit /b
)
type %1 | docker exec -i wedding-site-db-1 psql -U postgres weddingdb
echo ✅ Restore completato da %1
pause
