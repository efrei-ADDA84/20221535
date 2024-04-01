# Utilise l'image de base Python 3.9
FROM python:3.9

# Copie les fichiers de l'application dans l'image Docker
COPY . /app

# Définit le répertoire de travail
WORKDIR /app

# Installe les dépendances
RUN pip install requests

# Exécute le script Python
