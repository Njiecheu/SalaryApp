# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 14:49:59 2022

@author: raphaël
"""
from Employe_class import Employe
from multiprocessing import connection

class DRH(object):
    def __init__(self) -> None:
        pass
    def enregistrerEmploye(self):
        nom = input("Entrer le nom                 : ")
        prenom = input("Entrer le prenom              : ")
        matricule = input("Entrer le matricule           : ")
        dateNaissance = input("Entrer la date de naissance   : ")
        lieuNaissance = input("Entrer le lieu de naissance   : ")
        nationalite = input("Entrer la nationalite         : ")
        statutMatrimonial = input("Entrer le statut matrimonial  : ")
        fonction = input("Entrer la fonction            : ")
        typeContrat = input("Entrer le type de contrat     : ")
        dateRecrutement = input("Entrer la date de recrutement : ")
        dateFinEmploi = input("Entrer la date de fin d'emploi: ")
        salaireBase = int(input("Entrer le salaire de base     : "))
        salaireNet = int(input("Entrer le salaire net         : "))

        employe = Employe(nom,prenom,matricule,dateNaissance,lieuNaissance,nationalite,statutMatrimonial,fonction,typeContrat,dateRecrutement,dateFinEmploi,salaireBase,salaireNet)
        print(employe.getNom())

    def nombreAnneeTravailEmploye(self, matricule):
        pass
    
    def salaireEmploye(self, matricule):
        pass
    
    def statutEmploye(self, matricule):
        pass
    
    def modifierEmploye(self, matricule):
        pass
    
    def supprimerEmploye(self, matricule):
        pass

p = DRH()
p.enregistrerEmploye()
    

