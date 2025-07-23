@echo off
set TIMESTAMP=%DATE:~-4%%DATE:~3,2%%DATE:~0,2%_%TIME:~0,2%%TIME:~3,2%%TIME:~6,2%
set TIMESTAMP=%TIMESTAMP: =0%
docker exec -t wedding-site-db-1 pg_dump -U postgres weddingdb > backup_%TIMESTAMP%.sql
echo ✅ Backup creato: backup_%TIMESTAMP%.sql
pause
