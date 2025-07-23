@echo off
echo ---- Resetting Database ----
flask reset-db
echo ---- Migrating Database ----
flask migrate-db
echo ---- Creating Default Admin ----
flask create-admin
echo ---- All done ----
pause
