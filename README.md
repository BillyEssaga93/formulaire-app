#  Formulaire Web avec Flask + Docker

Une application web minimaliste développée avec **Python Flask**, permettant de **saisir un formulaire** depuis un navigateur et d’enregistrer les données **dans un fichier Excel local**. L'application est déployée dans un **conteneur Docker Linux**.

##  Fonctionnalités

- Formulaire web (nom, prénom, email, téléphone, code postal)
- Enregistrement dans un fichier `Excel (.xlsx)`
- Application Dockerisée avec accès web via `localhost:8080`
- Données sauvegardées en local grâce à un volume Docker

##Technologies

- Python 3.12
- Flask
- Pandas
- Openpyxl
- Docker (base : `python:3.12-slim`)

## Structure du projet

formulaire-app/  
|----app.py # Script principal Flask  
|----Dockerfile # Construction de l'image Docker  
|----requirements.txt # Dépendances Python  
|----templates/  
|----|---formulaire.html # Template HTML  
|----data/ # Dossier monté pour enregistrer les fichiers Excel  


## Lancement rapide

### 1. Cloner le projet
```bash
git clone https://github.com/billyessaga/formulaire-app.git
cd formulaire-app

## 2. Construire l’image Docker

```bash
docker build -t image_formulaire-app .

## 3. Lancer le conteneur

```bash
docker run --name conteneur_formulaire-app -p 8080:80 -v $(pwd)/data:/app/data image_formulaire-app

## 4. Accéder à l’application

http://localhost:8080

## 5. Résultat

Les données soumises sont enregistrées dans data/donnees.xlsx.

📄  Licence
MIT – Utilisation libre avec attribution.

Auteur
Billy Armel Essaga Anaba
📧  beachessag93@gmail.com
🔗  LinkedIn https://www.linkedin.com/in/billy-armel-essaga-anaba-aa4248242
