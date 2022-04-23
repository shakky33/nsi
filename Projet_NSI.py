from flask import *
from bdd_py import Bdd
app = Flask(__name__)
classbdd = Bdd("bdd/Projet.db")


@app.route("/")
def rediriger():
    return redirect("/home")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/edit")
def afficher():
    personnes = classbdd.recuperer_personnes()
    return render_template(
        "Lire_SQL_bdd02.html",
        personnes=personnes
    )

@app.route("/recherche", methods=['POST'])
def rechercher():
    # Récupération du nom
    nom_rechercher = request.form["nom"]
    return render_template(
        "recheche.html",
        personnes=classbdd.rechercher_eleves(nom_rechercher)
    )

@app.route("/afficher-formulaire")
def ajouter():
    return render_template(
        "ajouter.html"
    )

@app.route("/add-student", methods=['POST'])
def ajouter_eleve():
    nom = request.form["nom"]
    prenom = request.form["prenom"]
    naissance = request.form["naissance"]
    academie = request.form["etablissement"]
    etablissement = request.form["etablissement"]

    eleve = (nom, prenom, naissance, etablissement, academie)

    classbdd.ajouter_eleve(eleve=eleve)

    return redirect("/edit")



@app.route("/delete-student/<int:matricule>", methods=['POST'])
def supprimer_eleve(matricule):
    classbdd.supprimer_eleve(matricule=matricule)
    return redirect("/edit")


@app.route("/modify-student/<int:matricule>")
def modifier_eleve(matricule):
    personne = classbdd.rechercher_eleves(matricule)
    #print(f"Modification de l'eleve avec le matricule : {matricule}")
    return render_template(
        "modifier.html",
        personne=personne[0]
    )
    return redirect("/edit")
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1664, debug=True)
