# Utiliser une image Python
FROM python:3.11.4-alpine3.18

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copier le script Python principal
COPY ./run.py /app/

# Copier le script entrypoint
COPY entrypoint.sh /app/entrypoint.sh

# Donner les permissions d'exécution au script entrypoint
RUN chmod +x /app/entrypoint.sh

# Définir FLASK_APP
ENV FLASK_APP=run.py

# Exposer le port
EXPOSE 8080

RUN chmod +x /app/entrypoint.sh

# Définir l'entrée par défaut
ENTRYPOINT ["/app/entrypoint.sh"]

# Commande pour lancer Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
