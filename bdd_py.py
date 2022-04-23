import sqlite3


class Bdd:
    def __init__(self, chemin_bdd):
        self.chemin_bdd = chemin_bdd

    def recuperer_personnes(self):
        connexion = sqlite3.connect(self.chemin_bdd)
        curseur = connexion.cursor()
        requete_sql = """SELECT * FROM projet;"""
        resultat = curseur.execute(requete_sql)
        personnes = resultat.fetchall()
        connexion.close()
        return personnes

    def rechercher_eleves(self, matricule):
        connexion = sqlite3.connect(self.chemin_bdd)
        curseur = connexion.cursor()

        requete_sql = f"""SELECT * FROM projet p WHERE p.Matricule= '{matricule}';"""
        resultat = curseur.execute(requete_sql)
        eleves = resultat.fetchall()
        connexion.close()
        return eleves

    def ajouter_eleve(self, eleve):
        (nom, prenom, naissance, academie, etablissement) = eleve
        connexion = sqlite3.connect(self.chemin_bdd)
        curseur = connexion.cursor()

        requete_sql = f"""INSERT INTO projet (Nom, Prenom, DateDeNaissance, Etablissement, Academie) VALUES ('{nom}', '{prenom}', '{naissance}', '{etablissement}', '{academie}');"""
        print(requete_sql)
        resultat = curseur.execute(requete_sql)
        eleves = resultat.fetchall()
        connexion.commit()
        connexion.close()
        return None
    
    def supprimer_eleve(self, matricule):
        connexion = sqlite3.connect(self.chemin_bdd)
        curseur = connexion.cursor()
        requete_sql = f"""DELETE FROM projet WHERE Matricule = '{matricule}'"""
        resultat = curseur.execute(requete_sql)
        connexion.commit()
        connexion.close()
        
        
    def modifier_eleves(self, eleve):
        (matricule, nom, prenom, naissance, academie, etablissement) = eleve
        connexion = sqlite3.connect(self.chemin_bdd)
        curseur = connexion.cursor()
        requete_sql = f"""UPDATE projet SET Nom = '{nom}', Prenom='{prenom}', DateDeNaissance = '{naissance}', Etablissement = '{etablissement}', Academie ='{academie}' WHERE matricule = '{matricule}'"""
        resultat = curseur.execute(requete_sql)
        eleves = resultat.fetchall()
        connexion.commit()
        connexion.close()
        return None
    
