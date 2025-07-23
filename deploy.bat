@echo off
echo === Attivo ambiente virtuale ===
call .venv\Scripts\activate

echo === Costruisco immagini docker ===
docker-compose build

echo === Lancio docker-compose in produzione ===
docker-compose up -d

echo === Pulizia container orfani ===
docker system prune -f

echo === Controlla stato container ===
docker ps

echo === Segui i log live (Ctrl+C per uscire) ===
docker-compose logs -f
