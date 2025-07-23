#!/bin/bash
if [ -z "$1" ]; then
  echo "❗ Devi specificare il file backup da ripristinare (es: ./restore_db.sh backup_20250722.sql)"
  exit 1
fi

cat $1 | docker exec -i wedding-site-db-1 psql -U postgres weddingdb
echo "✅ Restore completato da $1"
