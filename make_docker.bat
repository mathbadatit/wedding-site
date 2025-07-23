@echo off
echo === Fermando Docker Compose ===
docker-compose down

echo === Avvio + Build Docker Compose ===
docker-compose up --build
