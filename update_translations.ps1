# Wedding Site - Aggiorna e Compila Traduzioni
Write-Host "=====================================" -ForegroundColor Magenta
Write-Host " Wedding Site - Aggiorna Traduzioni" -ForegroundColor Yellow
Write-Host "=====================================" -ForegroundColor Magenta

# Attiva venv
if (Test-Path ".venv\Scripts\Activate.ps1") {
    & ".\.venv\Scripts\Activate.ps1"
    Write-Host "✅ Ambiente virtuale attivato." -ForegroundColor Green
} else {
    Write-Host "❌ Ambiente virtuale non trovato." -ForegroundColor Red
    exit 1
}

# Controllo PyBabel
if (-not (Get-Command pybabel -ErrorAction SilentlyContinue)) {
    Write-Host "⚠️ PyBabel non trovato. Installo..." -ForegroundColor Yellow
    pip install Babel
}

# Controllo UTF-8 senza BOM nei .po
Write-Host "➡️  Controllo encoding file .po..." -ForegroundColor Cyan
Get-ChildItem -Path "translations" -Recurse -Filter "*.po" | ForEach-Object {
    $content = Get-Content $_.FullName -Encoding Byte
    if ($content.Length -ge 3 -and $content[0] -eq 239 -and $content[1] -eq 187 -and $content[2] -eq 191) {
        Write-Host "  ⚠️ Rimuovo BOM da:" $_.FullName -ForegroundColor Yellow
        $text = Get-Content $_.FullName -Encoding UTF8
        $text | Set-Content $_.FullName -Encoding UTF8
    }
}

# Estrazione
Write-Host "➡️  Estrazione stringhe in messages.pot..." -ForegroundColor Cyan
pybabel extract -F babel.cfg -o translations/messages.pot .
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Errore in estrazione." -ForegroundColor Red
    exit 1
}
Write-Host "✅ Estrazione completata." -ForegroundColor Green

# Aggiornamento
Write-Host "➡️  Aggiornamento file .po..." -ForegroundColor Cyan
pybabel update -i translations/messages.pot -d translations
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Errore in aggiornamento." -ForegroundColor Red
    exit 1
}
Write-Host "✅ Aggiornamento completato." -ForegroundColor Green

# Compilazione
Write-Host "➡️  Compilazione file .mo..." -ForegroundColor Cyan
pybabel compile -d translations
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Errore in compilazione." -ForegroundColor Red
    exit 1
}
Write-Host "✅ Compilazione completata." -ForegroundColor Green

# Fine
Write-Host "🎉 Tutto fatto! Traduzioni aggiornate e pronte." -ForegroundColor Magenta
