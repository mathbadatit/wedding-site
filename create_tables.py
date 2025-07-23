import sqlite3
import os

# Percorso del DB: instance/booking.db
db_path = os.path.join('instance', 'booking.db')

# Connessione al DB (crea il file se non esiste)
con = sqlite3.connect(db_path)
cur = con.cursor()

# Creazione tabella services
cur.execute("""
CREATE TABLE IF NOT EXISTS services (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  description TEXT NOT NULL,
  image_url TEXT
)
""")

con.commit()
con.close()

print("Tabella 'services' creata (se non esisteva).")
