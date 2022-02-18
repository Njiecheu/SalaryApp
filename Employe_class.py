# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 14:49:59 2022

@author: raphaël
"""

class Employe(object):
    def __init__(self, nom, prenom, matricule, dateNaissance, lieuNaissance, nationalite, statutMatrimonial, fonction, typeContrat, dateRecrutement, dateFinEmploi, salaireBase, salaireNet):
        self.__nom = nom
        self.__prenom = prenom
        self.__matricule = matricule
        self.__dateNaissance = dateNaissance
        self.__lieuNaissance = lieuNaissance
        self.__nationalite = nationalite
        self.__statutMatrimonial = statutMatrimonial
        self.__fonction = fonction
        self.typeContrat = typeContrat
        self.__dateRecrutement = dateRecrutement
        self.__dateFinEmploi = dateFinEmploi
        self.__salaireBase = salaireBase
        self.__salaireNet = salaireNet
        
    def getNom(self):
        return self.__nom
    def setNom(self, nom):
        self.__nom = nom

    def getPrenom(self):
        return self.__prenom
    def setPrenom(self, prenom):
        self.__prenom = prenom

    def getMatricule(self):
        return self.__matricule
    def setMatricule(self, mat):
        self.__matricule = mat

    def getDateNaissance(self):
        return self.__dateNaissance
    def setDateNaissance(self, dNaiss):
        self.__dateNaissance = dNaiss

    def getLieuNaissance(self):
        return self.__lieuNaissance
    def setLieuNaissance(self, lNaiss):
        self.__LieuNaissance = lNaiss

    def getNationalite(self):
        return self.__nationalite
    def setNationalite(self, nat):
        self.__nationalite = nat

    def getStatutMatrimonial(self):
        return self.__statutMatrimonial
    def setStatutMatrimonial(self, statutM):
        self.__statutMatrimonial = statutM

    def getFonction(self):
        return self.__fonction
    def setFonction(self, fnc):
        self.__fonction = fnc

    def getTypeContrat(self):
        return self.__typeContrat
    def setTypeContrat(self, typeC):
        self.__typeContrat = typeC

    def getDateRecrutement(self):
        return self.__dateRecrutement
    def setDateRecrutement(self, dRecrut):
        self.__dateRecrutement = dRecrut

    def getDateFinEmploi(self):
        return self.__dateFinEmploi
    def setDateFinEmploi(self, dFinE):
        self.__dateFinEmploi = dFinE

    def getSalaireBase(self):
        return self.__salaireBase
    def setSalaireBase(self, sBase):
        self.__salaireBase = sBase

    def getSalaireNet(self):
        return self.__salaireNet
    def setSalaireNet(self, sNet):
        self.__salaireNet = sNet
        
    def Employe(self, nom, prenom, matricule, dateNaissance, lieuNaissance, nationalite, statutMatrimonial, fonction, typeContrat, dateRecrutement, dateFinEmploi, salaireBase, salaireNet):
        Employe.__init__(self, nom, prenom, matricule, dateNaissance, lieuNaissance, nationalite, statutMatrimonial, fonction, typeContrat, dateRecrutement, dateFinEmploi, salaireBase, salaireNet)
    def nombreAnneesTravail(self, anneeTravail):
        self.anneeTravail = self.__dateFinEmploi - self.__dateRecrutement
        return (int(self.anneeTravail))
    def  Salaire(self, salaire):
        pass
        
        
        
        