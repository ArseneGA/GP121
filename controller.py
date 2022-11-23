# -*- coding: utf-8 -*-
"""

"""

import ULM
import tkinter as tk

def formulaireEnvoye():
    tk.messagebox.showinfo("Statut de l'inscription", "Fomulaire envoyé")

def enregister_donnees_artiste(nom, prenom, numero_telephone, date, chair_position, prix_place):
    artiste = ULM.Artiste(nom.get(), prenom.get(), numero_telephone.get(), date.get(), chair_position.get(), prix_place.get())

    