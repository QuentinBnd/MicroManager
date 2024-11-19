#!/bin/sh

# Attendre 10 secondes avant de démarrer l'application
echo "Waiting for db start, before starting the application..."
sleep 5

# Exécuter la commande passée au conteneur
exec "$@"
