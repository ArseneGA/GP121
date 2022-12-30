# -*- coding: utf-8 -*-


'''
Interface Olympia
'''

import tkinter as tk
from modele import*







def interface_main():

    interface = tk.Tk()
    interface.title("Olympia")
    

    label = tk.Label(interface, text="Salle de l'Olympia",font=("arial italic", 15))
    label.grid(column=5, row=1)
    
    #Ici se retrouve les commandes
    
    
    #là on note toutes les variables
    
    email_art = tk.StringVar()
    mdp_art = tk.StringVar()
    email_spect = tk.StringVar()
    mdp_spect = tk.StringVar()
    new_email_art = tk.StringVar()
    new_mdp_art = tk.StringVar()
    new_email_spect = tk.StringVar()
    new_mdp_spect = tk.StringVar()
    
    
    #ici se retrouvent toutes les entrees
    Entree = tk.Entry(interface, width=15, textvariable=email_art)
    Entree.grid(column=2, row=3)
    Entree1 = tk.Entry(interface, width=15, textvariable=mdp_art)
    Entree1.grid(column=2, row=4)
    Entree2 = tk.Entry(interface, width=15, textvariable=email_spect)
    Entree2.grid(column=9, row=3)
    Entree3 = tk.Entry(interface, width=15, textvariable=mdp_spect)
    Entree3.grid(column=9, row=4)
    
    Entree4 = tk.Entry(interface, width=15, textvariable=new_email_art)
    Entree4.grid(column=2, row=6)
    Entree5 = tk.Entry(interface, width=15, textvariable=new_mdp_art)
    Entree5.grid(column=2, row=7)
    Entree6 = tk.Entry(interface, width=15, textvariable=new_email_spect)
    Entree6.grid(column=9, row=6)
    Entree7 = tk.Entry(interface, width=15, textvariable=new_mdp_spect)
    Entree7.grid(column=9, row=7)
    
    #Ici se retrouvent les labels (les textes)
    T1= tk.Label(interface, text="Si vous êtes un artiste c'est par ici:", highlightbackground="blue", fg="blue" )
    T1.grid(column=2, row=2)
    T2= tk.Label(interface, text="Si vous êtes un spectateur c'est par ici:",highlightbackground="blue", fg="blue")
    T2.grid(column=9, row=2)
    
    T11= tk.Label(interface, text="Pas encore client :", highlightbackground="blue", fg="blue" )
    T11.grid(column=2, row=5)
    T12= tk.Label(interface, text="Pas encore client :",highlightbackground="blue", fg="blue")
    T12.grid(column=9, row=5)
    
    T3= tk.Label(interface, text="email: ", highlightbackground="blue", fg="blue" )
    T3.grid(column=1, row=3)
    T4= tk.Label(interface, text="mot de passe: ",highlightbackground="blue", fg="blue")
    T4.grid(column=1, row=4)
    T5= tk.Label(interface, text="email: ", highlightbackground="blue", fg="blue" )
    T5.grid(column=8, row=3)
    T6= tk.Label(interface, text="mot de passe: ",highlightbackground="blue", fg="blue")
    T6.grid(column=8, row=4)
    
    T7= tk.Label(interface, text="email: ", highlightbackground="blue", fg="blue" )
    T7.grid(column=1, row=6)
    T8= tk.Label(interface, text="mot de passe: ",highlightbackground="blue", fg="blue")
    T8.grid(column=1, row=7)
    T9= tk.Label(interface, text="email: ", highlightbackground="blue", fg="blue" )
    T9.grid(column=8, row=6)
    T10=tk.Label(interface, text="mot de passe: ",highlightbackground="blue", fg="blue")
    T10.grid(column=8, row=7)
    
    # Ici se retrouvent les boutons
    bouton1 = tk.Button(interface, text = 'Valider', command = valider_art(email_art,mdp_art))
    bouton1.grid(column=3, row=4)
    bouton2 = tk.Button(interface, text = 'Valider', command = valider_spect(email_spect,mdp_spect))
    bouton2.grid(column=10, row=4)
    bouton3 = tk.Button(interface, text = 'Valider', command = valider_new_art(new_email_art,new_mdp_art))
    bouton3.grid(column=3, row=7)
    bouton4 = tk.Button(interface, text = 'Valider', command = valider_new_spect(new_email_spect,new_mdp_spect))
    bouton4.grid(column=10, row=7)
    
    interface.mainloop()
    

    
def interface_artiste():
    

    interface = tk.Tk()
    interface.title("Artiste")
    
    date = tk.StringVar()
    chair_position = tk.StringVar()
    prix_place = tk.StringVar()
    nom = tk.StringVar()
    number = tk.StringVar()
    prenom = tk.StringVar()
    
    label = tk.Label(interface, text="Artiste",font=("arial italic", 15))
    label.grid(column=5, row=1)
    
    
    Entree2 = tk.Entry(interface, width=15, textvariable=nom)
    Entree2.grid(column=2, row=3)
    Entree3 = tk.Entry(interface, width=15, textvariable=prenom)
    Entree3.grid(column=2, row=4)
    Entree4 = tk.Entry(interface, width=15, textvariable=number)
    Entree4.grid(column=2, row=5)
    Entree5 = tk.Entry(interface, width=15, textvariable=date)
    Entree5.grid(column=2, row=6)
    Entree6 = tk.Entry(interface, width=15, textvariable=chair_position)
    Entree6.grid(column=2, row=7)
    Entree7 = tk.Entry(interface, width=15, textvariable=prix_place)
    Entree7.grid(column=2, row=8)
    
    
    
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
    
    bouton1 = tk.Button(interface, text = 'Valider', command = formulaireEnvoye)
    bouton1.grid(column=5, row=9)
    
    interface.mainloop()
    


def interface_spectateur():
    
    
    interface = tk.Tk()
    interface.title("Spectateur")
    
    

    prenom = tk.StringVar() 
    nom = tk.StringVar()
    
    label = tk.Label(interface, text="Spectateur",font=("arial italic", 15))
    label.grid(column=5, row=1)
    
    
    T1= tk.Label(interface, text="Afin de réserver une place, choisissez l'artiste et complétez vos coordonneés:" )
    T1.grid(column=5, row=2)
    T2= tk.Label(interface, text="Nom:", highlightbackground="blue", fg="blue" )
    T2.grid(column=1, row=3)
    T3= tk.Label(interface, text="Prénom:", highlightbackground="blue", fg="blue" )
    T3.grid(column=1, row=4)
    
    
    Entree1 = tk.Entry(interface, width=15, textvariable=nom)
    Entree1.grid(column=2, row=3)
    Entree2 = tk.Entry(interface, width=15, textvariable=prenom)
    Entree2.grid(column=2, row=4)
    
    
    bouton1 = tk.Button(interface, text = 'Valider', command = formulaireEnvoye)
    bouton1.grid(column=5, row=5)
    
    interface.mainloop()
    
