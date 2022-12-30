"""
fichier fonction
"""
import pandas as pd
import tkinter as tk


def valider_new_art(new_email_art,new_mdp_art):
    df = pd.read_csv('artiste.csv',sep = ',')
    a = 0
    b,c = df['email'], df['mot de passe']
    nombre_element = len(b) + 1
    
    for csv_email in b :
        if str(csv_email).strip() == str(new_email_art.get()):
            tk.messagebox.showinfo("Validation de votre compte", "Vous avez deja un compte")
            a = 1
            
    position_user = nombre_element + 1
            
    if a == 0:
        df2 = {'email':new_email_art.get(), 'mot de passe':new_mdp_art.get(), 'prenom' : '','nom': '','telephone':''}
        df= df.append(df2, ignore_index = True)
        df.to_csv('artiste.csv',index=False)
        tk.messagebox.showinfo("Validation de votre compte", "Vous venez de creer votre compte")

    

def valider_new_spect(new_email_spect,new_mdp_spect):
    df = pd.read_csv('spect.csv',sep = ',')
    a = 0
    b,c = df['email'], df['mot de passe']
    nombre_element = len(b) + 1
    
    for csv_email in b :
        if str(csv_email).strip() == str(new_email_spect.get()):
            tk.messagebox.showinfo("Validation de votre compte", "Vous avez deja un compte")
            a = 1
            
    position_user = nombre_element + 1
            
    if a == 0:
        df2 = {'email':new_email_spect.get(), 'mot de passe':new_mdp_spect.get(), 'prenom' : '','nom': '','telephone':''}
        df= df.append(df2, ignore_index = True)
        df.to_csv('spect.csv',index=False)
        tk.messagebox.showinfo("Validation de votre compte", "Vous venez de creer votre compte")

def valider_art(email_art,mdp_art):
    df = pd.read_csv('artiste.csv',sep = ',')
    a = 0
    i = 0
    
    b = df['email']
    c = df['mot de passe']
    
    for csv_email in b:       # vérifications de l'existance de l'adresse email
        i += 1
        print(i)
        if str(email_art.get()) == str(b[i]):
            if str(mdp_art.get()) == str(c[i]): # concordance entre email et mdp
                tk.messagebox.showinfo("Validation de votre compte", "§§§§§§§§§§§§§§§")
    
def valider_spect(email_spect,mdp_spect):
    df = pd.read_csv('spect.csv',sep = ',')
    a = 0
    i = 0
    
    b = df['email']
    c = df['mot de passe']
    
    for csv_email in b:       # vérifications de l'existance de l'adresse email
        i += 1
        print(i)
        if str(email_spect.get()) == str(b[i]):
            if str(mdp_spect.get()) == str(c[i]): # concordance entre email et mdp
                tk.messagebox.showinfo("Validation de votre compte", "§§§§§§§§§§§§§§§")
                
def formulaireEnvoye():
    tk.messagebox.showinfo("Statut de l'inscription", "Fomulaire envoyé")

def enregister_donnees_artiste(nom, prenom, numero_telephone, date, chair_position, prix_place):
    artiste = Artiste(nom.get(), prenom.get(), numero_telephone.get(), date.get(), chair_position.get(), prix_place.get())
    
    
class Artiste:
    '''
    création de la classe artiste
    '''
    def __init__(self, nom, prenom, number, date, chair_position, prix_place):
        '''
        création des attributs du artiste
        '''
        self.nom = nom
        self.prenom = prenom
        self.number = number
        self.date = date
        self.chair_position = chair_position
        self.prix_place = prix_place
    

class Spectateur:
    '''
    création de la classe spectateur 
    '''
    def __init___(self, email, mdp, prenom, nom):
        '''
        création des attributs de l'spectateur 
        '''
        
