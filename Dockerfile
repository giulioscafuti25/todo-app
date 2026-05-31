#Usiamo Python 3.13 come immagine base
FROM python:3.13-slim

#Impostiamo la cartella di lavoro dentro il container
WORKDIR /app

#Copriamo il file delle dipendenze
COPY requirements.txt .

#Installiamo le dipendenze
RUN pip install -r requirements.txt

#Copiamo tutto il resto del progetto
COPY . .

#Esponiamo la porta 5000
EXPOSE 5000

#Comando per avviare l'applicazione
CMD ["python", "app.py"]