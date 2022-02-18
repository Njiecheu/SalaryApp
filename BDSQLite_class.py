# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 14:49:59 2022

@author: raphaël
"""

from distutils.log import error
from msilib.schema import Error
from BD_class import *

class BDSQLite(object):
    def __init__(self) -> None:
        pass
    def insererEmploye(self):
                connection = sqlite3.connect('Employe.db')
                cursor = connection.cursor()
                new_user = (cursor.lastrowid, Employe.nom, Employe.prenom, Employe.matricule, Employe.dateNaissance, Employe.lieuNaissance, Employe.nationalite, Employe.statutMatrimonial, Employe.fonction, Employe.typeContrat, Employe.dateRecrutement, Employe.dateFinEmploi, Employe.salaireBase, Employe.salaireNet)
                requete = cursor.execute("INSERT INTO t_Employe VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",new_user)
                connection.commit()
                print("Employé ajouté")
                connection.close()
    def supprimerEmploye(self):
                connection = sqlite3.connect('Employe.db')
                cursor = connection.cursor()
                new_user = (cursor.lastrowid, Employe.nom, Employe.prenom, Employe.matricule, Employe.dateNaissance, Employe.lieuNaissance, Employe.nationalite, Employe.statutMatrimonial, Employe.fonction, Employe.typeContrat, Employe.dateRecrutement, Employe.dateFinEmploi, Employe.salaireBase, Employe.salaireNet)
                requete = cursor.execute("DELETE FROM t_Employe WHERE matricule = ?",new_user)
                connection.commit()
                print("Employé supprimé")
                connection.close
    def insererEntreprise(self):
                connection = sqlite3.connect('Entreprise.db')
                cursor = connection.cursor()
                new_user = (cursor.lastrowid, Entreprise.nom, Entreprise.anneeCreation, Entreprise.siegeSocial, Entreprise.boitePostale, Entreprise.telephone, Entreprise.fax, Entreprise.email, Entreprise.activite, Entreprise.effectif, Entreprise.capital, Entreprise.siteInternet, Entreprise.nomDirecteur, Entreprise.numeroContribuable, Entreprise.formeJuridique, Entreprise.chiffreAffaire)
                requete = cursor.execute("INSERT INTO t_Entreprise VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",new_user)
                connection.commit()
                print("Entreprise ajouté")
                connection.close()
    def MAJEmploye(self):
                print(TRUE)