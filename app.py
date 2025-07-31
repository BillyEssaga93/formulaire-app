# Importation des modules nécessaires
from flask import Flask, render_template, request, redirect  # Flask pour créer le serveur web
import pandas as pd      # Pandas pour gérer les données sous forme de tableau
import os                # os pour vérifier si un fichier existe

# Création de l'application Flask
app = Flask(__name__)

# Chemin vers le fichier Excel dans lequel on va enregistrer les données
EXCEL_FILE = "data/donnees.xlsx"

# Route principale : quand on accède à la page d'accueil ("/")
@app.route("/")
def formulaire():
    # On affiche le fichier HTML form.html (le formulaire)
    return render_template("form.html")

# Route qui traite l'envoi du formulaire (POST uniquement)
@app.route("/submit", methods=["POST"])
def submit():
    # On récupère les données envoyées dans le formulaire
    nom = request.form.get("nom")
    prenom = request.form.get("prenom")
    email = request.form.get("email")
    telephone = request.form.get("telephone")
    code_postal = request.form.get("code_postal")

    # On vérifie que toutes les données ont bien été saisies
    if all([nom, prenom, email, telephone, code_postal]):
        # On prépare un dictionnaire de données sous forme de colonnes
        data = {
            "Nom": [nom],
            "Prénom": [prenom],
            "Email": [email],
            "Téléphone": [telephone],
            "Code postal": [code_postal]
        }

        # On transforme les données en DataFrame (tableau) avec pandas
        df_new = pd.DataFrame(data)

        # Si le fichier Excel existe déjà, on lit les anciennes données
        if os.path.exists(EXCEL_FILE):
            df_existing = pd.read_excel(EXCEL_FILE)          # on charge les anciennes données
            df_combined = pd.concat([df_existing, df_new], ignore_index=True)  # on ajoute la nouvelle ligne
        else:
            # Si le fichier n'existe pas, on crée un nouveau tableau avec la seule nouvelle ligne
            df_combined = df_new

        # On enregistre le tableau (ancien + nouveau ou juste nouveau) dans le fichier Excel
        df_combined.to_excel(EXCEL_FILE, index=False)

    # Une fois les données traitées, on retourne à la page d'accueil (formulaire)
    return redirect("/")

# Point d'entrée principal : on démarre le serveur Flask
if __name__ == "__main__":
    # L'application tourne sur toutes les interfaces réseau du conteneur, sur le port 80
    app.run(host="0.0.0.0", port=80)
