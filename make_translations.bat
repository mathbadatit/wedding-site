@echo off
setlocal enabledelayedexpansion

echo ===================================
echo   Wedding Site - Traduzioni PyBabel
echo ===================================

REM === 1. Attiva virtualenv ===
if exist ".venv\Scripts\activate.bat" (
    call .venv\Scripts\activate
) else (
    echo ❌ Ambiente virtuale non trovato: .venv
    exit /b 1
)

REM === 2. Rimuovi BOM dai .po ===
echo 🔍 Controllo BOM nei file .po...
for /r translations %%f in (*.po) do (
    powershell -Command ^
        "$content = Get-Content -Encoding Byte '%%f'; ^
        if ($content[0] -eq 239 -and $content[1] -eq 187 -and $content[2] -eq 191) { ^
            Write-Host '⚠️ BOM trovato in %%f → rimosso.'; ^
            $content = $content[3..($content.Length-1)]; ^
            [IO.File]::WriteAllBytes('%%f', $content) ^
        } else { ^
            Write-Host '✅ Nessun BOM in %%f' ^
        }"
)

REM === 3. Estrai stringhe ===
echo === Estrazione stringhe con PyBabel ===
pybabel extract -F babel.cfg -o translations/messages.pot .

REM === 4. Aggiorna file .po ===
echo === Aggiornamento file .po ===
pybabel update -i translations/messages.pot -d translations

REM === 5. Compila file .mo ===
echo === Compilazione file .mo ===
pybabel compile -d translations

echo 🎉 Traduzioni aggiornate e compilate con successo.
pause
