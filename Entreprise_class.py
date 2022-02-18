# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 16:55:18 2022

@author: raphaël
"""

class Entreprise(object):
    def __init__(self, nom, anneeCreation, siegeSocial, boitePostale, telephone, fax, email, activite, effectif, capital, siteInternet, nomDirecteur, numeroContribuable, formeJuridique, chiffreAffaire):
       self.__nom = nom
       self.__anneeCreation = anneeCreation
       self.__siegeSocial = siegeSocial
       self.__boitePostale = boitePostale
       self.__telephone = telephone
       self.__fax = fax
       self.__email = email
       self.__activite = activite
       self.__effectif = effectif
       self.__capital = capital
       self.__siteInternet = siteInternet
       self.__nomDirecteur = nomDirecteur
       self.__numeroContribuable = numeroContribuable
       self.__formeJuridique = formeJuridique
       self.__chiffreAffaire = chiffreAffaire

    def getNom(self):
        return self.__nom
    def setNom(self, nom):
        self.__nom = nom

    def getAnneeCreation(self):
        return self.__anneeCreation
    def setAnneeCreation(self, anneeCreat):
        self.__anneeCreation = anneeCreat

    def getSiegeSocial(self):
        return self.__siegeSocial
    def setSiegeSocial(self, siegeSoc):
        self.__siegeSocial = siegeSoc

    def getBoitePostale(self):
        return self.__boitePostale
    def setBoitePostale(self, boitePost):
        self.__boitePostale = boitePost

    def getTelephone(self):
        return self.__telephone
    def setTelephone(self, tel):
        self.__telephone = tel

    def getFax(self):
        return self.__fax
    def setFax(self, fax):
        self.__fax = fax

    def getEmail(self):
        return self.__email
    def setEmail(self, email):
        self.__email = email

    def getActivite(self):
        return self.__activite
    def setActivite(self, act):
        self.__activite = act

    def getEffectif(self):
        return self.__effectif
    def setEffectif(self, eff):
        self.__effectif = eff

    def getCapital(self):
        return self.__capital
    def setCapital(self, cap):
        self.__capital = cap

    def getSiteInternet(self):
        return self.__siteInternet
    def setSiteInternet(self, siteInt):
        self.__siteInternet = siteInt

    def getNomDirecteur(self):
        return self.__nomDirecteur
    def setNomDirecteur(self, nomDir):
        self.__nomDirecteur = nomDir

    def getNumeroContribuable(self):
        return self.__numeroContribuable
    def setNumeroContribuable(self, numCont):
        self.__numeroContribuable = numCont
    
    def getFormeJuridique(self):
        return self.__formeJuridique
    def setFormeJuridique(self, formJur):
        self.__formeJuridique = formJur
    
    def getChiffreAffaire(self):
        return self.__chiffreAffaire
    def setChiffreAffaire(self, chiAff):
        self.__chiffreAffaire = chiAff

    def entreprise(self, nom, anneeCreation, siegeSocial, boitePostale, telephone, fax, email, activite, effectif, capital, siteInternet, nomDirecteur, numeroContribuable, formeJuridique, chiffreAffaire):
        Entreprise.__init__(self, nom, anneeCreation, siegeSocial, boitePostale, telephone, fax, email, activite, effectif, capital, siteInternet, nomDirecteur, numeroContribuable, formeJuridique, chiffreAffaire)

