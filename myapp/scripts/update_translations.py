import subprocess
import sys

def run_command(cmd, desc):
    print(f"🔹 {desc}...")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"❌ Errore in: {desc}")
        sys.exit(result.returncode)

def main():
    print("=== Aggiornamento Traduzioni (Python CLI) ===")
    run_command("pybabel extract -F babel.cfg -o translations/messages.pot .", "Estrazione messaggi")
    run_command("pybabel update -i translations/messages.pot -d translations", "Aggiornamento .po")
    run_command("pybabel compile -d translations", "Compilazione .mo")
    print("✅ Tutto fatto con successo!")

if __name__ == "__main__":
    main()
