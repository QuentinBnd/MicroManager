# Utiliser une image Python
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copier le code source
COPY . .

# Exposer le port
EXPOSE 5000

# Commande pour lancer Flask
CMD ["python", "run.py"]
