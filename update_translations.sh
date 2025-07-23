#!/bin/bash

echo "➡️  Estrazione stringhe con PyBabel..."
pybabel extract -F babel.cfg -o messages.pot .

echo "✅ Estrazione completata."

echo "➡️  Aggiornamento file di traduzione (.po)..."
pybabel update -i messages.pot -d translations

echo "✅ Aggiornamento completato."

echo "➡️  Compilazione file di traduzione (.mo)..."
pybabel compile -d translations

echo "✅ Compilazione completata."

echo "🎉 Tutto fatto!"
