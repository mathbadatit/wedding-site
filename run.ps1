# run.ps1

Write-Host "---- Attivo ambiente virtuale ----"
. .\.venv\Scripts\Activate.ps1

Write-Host "---- Resetto database ----"
flask reset-db

Write-Host "---- Eseguo migrazioni ----"
flask migrate-db

Write-Host "---- Creo admin default ----"
flask create-admin

Write-Host "---- Avvio server Flask ----"
flask run
