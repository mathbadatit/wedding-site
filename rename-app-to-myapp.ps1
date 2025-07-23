# Verifica che esista la cartella app
if (-Not (Test-Path ".\app")) {
    Write-Host "❌ Cartella 'app' non trovata nella directory corrente." -ForegroundColor Red
    exit 1
}

# Rinomina la cartella app in myapp
Rename-Item -Path ".\app" -NewName "myapp"
Write-Host "✅ Cartella 'app' rinominata in 'myapp'." -ForegroundColor Green

# Cerca e sostituisci 'app' con 'myapp' nei file di testo più comuni (py, txt, md, html)
$fileTypes = @("*.py", "*.txt", "*.md", "*.html", "*.cfg")

$files = Get-ChildItem -Path . -Recurse -Include $fileTypes

$filesModificati = 0

foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw

    # Usa regex con \b per sostituire solo 'app' come parola intera (case sensitive)
    $contentNuovo = [regex]::Replace($content, '\bapp\b', 'myapp')

    if ($content -ne $contentNuovo) {
        Set-Content -Path $file.FullName -Value $contentNuovo
        $filesModificati++
        Write-Host "Modificato: $($file.FullName)"
    }
}

Write-Host ""
Write-Host "🎉 Operazione completata!"
Write-Host "Totale file modificati: $filesModificati"
