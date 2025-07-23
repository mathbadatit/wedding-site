# Aggiorna i file .po partendo dal .pot e compila i .mo
# Assumendo che pybabel sia nel PATH o nel venv attivo

# Estrai le stringhe in .pot
pybabel extract -F babel.cfg -o messages.pot .

# Aggiorna i .po per ogni lingua
pybabel update -i messages.pot -d translations

# Compila i .mo
pybabel compile -d translations

Write-Output "Traduzioni aggiornate e compilate."
