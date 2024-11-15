# Utiliser une image Python
FROM python:3.11.4-alpine3.18

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copier le code source
COPY ./app.py /app/

# Exposer le port
EXPOSE 8080

# Commande pour lancer Flask

CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
