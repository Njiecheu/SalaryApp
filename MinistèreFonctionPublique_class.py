# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 14:49:59 2022

@author: raphaël
"""

import sqlite3


class MinistereFonctionPublique(object):
    def __init__(self) -> None:
        pass
    def EnregistrerEntreprise(self, nom, anneeCreation, siegeSocial, boitePostale, telephone, fax, email, activite, effectif, capital, siteInternet, nomDirecteur, numeroContribuable, formeJuridique, chiffreAffaire):
        connection = sqlite3.connect("Entreprise.db")
        cursor = connection.cursor()
        new_user = (cursor.lastrowid, nom, anneeCreation, siegeSocial, boitePostale, telephone, fax, email, activite, effectif, capital, siteInternet, nomDirecteur, numeroContribuable, formeJuridique, chiffreAffaire)
        requete = cursor.execute("INSERT INTO t_Entreprise VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",new_user)
        connection.commit()
        print("Entreprise ajouté")
        connection.close()