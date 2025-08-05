# ================================
# Wedding Site - Gestione Traduzioni con Controllo Encoding
# ================================

# Percorsi
VENV = .venv
BABEL_CFG = babel.cfg
POT_FILE = translations/messages.pot
TRANS_DIR = translations
PYBABEL = $(VENV)/Scripts/pybabel.exe

# Rimuove BOM dai file PO se presenti
.PHONY: fix_bom
fix_bom:
	@echo "🔍 Controllo BOM nei file .po..."
	@find $(TRANS_DIR) -type f -name "*.po" | while read f; do \
		if head -c 3 $$f | grep -q $'\xef\xbb\xbf'; then \
			echo "⚠️  BOM trovato in $$f → rimosso."; \
			tail -c +4 $$f > $$f.tmp && mv $$f.tmp $$f; \
		else \
			echo "✅ Nessun BOM in $$f"; \
		fi \
	done

# Aggiorna e compila le traduzioni
.PHONY: translations
translations: fix_bom
	@echo "=== Attivo ambiente virtuale ==="
	@if [ -f "$(VENV)/Scripts/activate" ]; then \
		. "$(VENV)/Scripts/activate"; \
	else \
		echo "❌ Ambiente virtuale non trovato."; \
		exit 1; \
	fi
	@echo "=== Estrazione stringhe ==="
	@$(PYBABEL) extract -F $(BABEL_CFG) -o $(POT_FILE) .
	@echo "=== Aggiornamento file .po ==="
	@$(PYBABEL) update -i $(POT_FILE) -d $(TRANS_DIR)
	@echo "=== Compilazione file .mo ==="
	@$(PYBABEL) compile -d $(TRANS_DIR)
	@echo "🎉 Traduzioni aggiornate e compilate."

# Pulizia file temporanei
.PHONY: clean_translations
clean_translations:
	@echo "🧹 Pulizia file temporanei..."
	@find $(TRANS_DIR) -type f -name '*.mo' -delete
	@find $(TRANS_DIR) -type f -name '*.pot' -delete
	@echo "✅ Pulizia completata."
