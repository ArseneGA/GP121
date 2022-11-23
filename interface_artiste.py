# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 14:51:45 2022

@author: Mai
"""
import tkinter as tk
import controller






interface = tk.Tk()
interface.title("Artiste")

date = tk.StringVar()
chair_position = tk.StringVar()
prix_place = tk.StringVar()
nom = tk.StringVar()
numero_telephone = tk.StringVar()
prenom = tk.StringVar()

label = tk.Label(interface, text="Artiste",font=("arial italic", 15))
label.grid(column=5, row=1)



T1= tk.Label(interface, text="Afin de réserver la salle, complétez les données ci dessous:" )
T1.grid(column=5, row=2)
T2= tk.Label(interface, text="Nom:", highlightbackground="blue", fg="blue" )
T2.grid(column=1, row=3)
T3= tk.Label(interface, text="Prénom:", highlightbackground="blue", fg="blue" )
T3.grid(column=1, row=4)
T4= tk.Label(interface, text="Numéro de téléphone:", highlightbackground="blue", fg="blue" )
T4.grid(column=1, row=5)
T5= tk.Label(interface, text="Date de réservation:", highlightbackground="blue", fg="blue" )
T5.grid(column=1, row=6)
T6= tk.Label(interface, text="Choisir la disposition des chaises:", highlightbackground="blue", fg="blue" )
T6.grid(column=1, row=7)
T7 = tk.Label(interface, text = "A quel prix voulez vous vendre la place?  :", highlightbackground="blue", fg="blue")
T7.grid(column=1, row=8)



entree1 = tk.Entry(interface, width=15, textvariable=date)
entree1.grid(column=2, row=6)
entree2 = tk.Radiobutton(interface, text = "Places debout", value = 'Debout', variable = chair_position).grid(row = 7, column = 2)
entree3 = tk.Radiobutton(interface, text = "Places assises" , value = 'Assis',variable = chair_position).grid(row = 7, column = 3)
entree4 = tk.Entry(interface, width=15, textvariable=prix_place)
entree4.grid(column=2, row=8)
entree5 = tk.Entry(interface, width=15,textvariable=nom)
entree5.grid(column=2, row=3)
entree6 = tk.Entry(interface, width=15,textvariable=numero_telephone)
entree6.grid(column=2, row=5)
entree7 = tk.Entry(interface, width=15,textvariable=prenom)
entree7.grid(column=2, row=4)

submit = tk.Button(interface, text = 'Submit', command = controller.formulaireEnvoye).grid(row = 9, column = 3)

interface.mainloop()

controller.enregister_donnees_artiste(nom, prenom, numero_telephone, date, chair_position, prix_place)
