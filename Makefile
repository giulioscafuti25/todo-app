# Installa tutte le dipendenze del progetto
build:
	pip install -r requirements.txt

# Esegue i test automatici
test:
	pytest tests/test_app.py -v

# Esegue l'analisi dello stile del codice
lint:
	flake8 app.py

# Esegue l'analisi di sicurezza
security:
	bandit -r app.py

# Avvia l'applicazione
run:
	python app.py