import os
import shutil
from datetime import datetime

data = datetime.now().strftime("%Y-%m-%d_%H-%M")
dest = f"backup_{data}"

os.makedirs(dest, exist_ok=True)

# Backup DB e traduzioni
files_to_backup = [
    "instance/booking.db",
    "migrations/translations/ar/LC_MESSAGES/messages.po",
    "migrations/translations/en/LC_MESSAGES/messages.po",
    "migrations/translations/it/LC_MESSAGES/messages.po",
    "static/images/",
    "static/pdf/"
]

for item in files_to_backup:
    if os.path.exists(item):
        if os.path.isfile(item):
            shutil.copy(item, dest)
            print(f"✅ Copiato file: {item}")
        else:
            shutil.copytree(item, os.path.join(dest, os.path.basename(item)), dirs_exist_ok=True)
            print(f"✅ Copiata cartella: {item}")
