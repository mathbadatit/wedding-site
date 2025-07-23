import os

os.system('pybabel extract -F babel.cfg -o messages.pot .')
os.system('pybabel update -i messages.pot -d translations')
os.system('pybabel compile -d translations')
print("✅ Traduzioni aggiornate e compilate.")
