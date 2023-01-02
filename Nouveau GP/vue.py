# Interface
import tkinter as tk
import csv
import modele as md
import pandas as pd
import smtplib

class Interface_Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Olympia")
        self.config(bg='red')
        self.geometry("750x250")
        
        self.email_art = tk.StringVar()
        self.email_spect = tk.StringVar()
        
        label = tk.Label(self, text="Salle de l'Olympia",font=("arial italic", 15))
        label.config(bg="red")
        label.grid(column=5, row=1)
        
        T1= tk.Label(self, text="Si vous êtes un artiste c'est par ici:", highlightbackground="red", fg="yellow" )
        T1.config(bg='red')
        T1.grid(column=2, row=4)
        T2= tk.Label(self, text="Si vous êtes un spectateur c'est par ici:",highlightbackground="red", fg="yellow")
        T2.grid(column=9, row=4)
        T2.config(bg='red')
        T3= tk.Label(self, text="email: ", highlightbackground="blue", fg="yellow" )
        T3.grid(column=1, row=5)
        T3.config(bg='red')
        T4= tk.Label(self, text="email: ",highlightbackground="blue", fg="yellow")
        T4.grid(column=8, row=5)
        T4.config(bg='red')
        
        inutile1 = tk.Label(self, text="")
        inutile1.config(bg="red")
        inutile1.grid(column=1, row = 2)
        
        inutile2 = tk.Label(self, text="")
        inutile2.config(bg="red")
        inutile2.grid(column=1, row = 3)
        
        Entree1 = tk.Entry(self, width=15, textvariable= self.email_art)
        Entree1.config(bg='red')
        Entree1.grid(column=2, row=5)
        Entree2 = tk.Entry(self, width=15, textvariable= self.email_spect)
        Entree2.grid(column=9, row=5)
        Entree2.config(bg='red')
        
        def save_email():
            with open('mail.txt', 'w') as f:
                pass
            f = open('mail.txt', 'w')
            f.write(self.email_spect.get())
            f.close()
        
        bouton1 = tk.Button(self, text = 'Valider', command = Interface_Artiste)
        bouton1.grid(column=3, row=5)
        bouton2 = tk.Button(self, text = 'Valider', command = md.two_funcs(save_email,Interface_Spectateur))
        bouton2.grid(column=10, row=5)
        
        self.mainloop()      


class Interface_Artiste(tk.Tk):
    
    
    
    def __init__(self):
        super().__init__()
        self.title("Artiste")

        tk.Label(self, text="Nom").grid(row=0, column=0)
        tk.Label(self, text="Prénom").grid(row=1, column=0)
        tk.Label(self, text="Numéro de téléphone").grid(row=2, column=0)
        tk.Label(self, text="Date de réservation").grid(row=3, column=0)
        tk.Label(self, text="dispostion de la salle").grid(row=4, column=0)
        tk.Label(self, text="Prix de la place").grid(row=5, column=0)
        
        
        def show_info_place():
            tk.messagebox.showinfo("Disposition de la salle", "1. 200 places en carré d'or, 600 en orchestre et 500 en mezzanine\n2. 300 places en carré d'or, 400 en orchestre et 500 en mezzanine\n3. 1000 en fosses et 500 en mezzanine")

        def show_info_prix():
            tk.messagebox.showinfo("Prix des places","Vous choisissez le prix de l'orchestre ou le prix en fosses. Le prix du carré d'or sera 50 euros plus cher et le prix de la mezzanine 20 euros plus cher")

        self.nom_entry = tk.Entry(self)
        self.prenom_entry = tk.Entry(self)
        self.tel_entry = tk.Entry(self)
        self.date_entry = tk.Entry(self)
        self.nombre_entry = tk.Spinbox(self, from_=1, to=3)
        self.prix_entry = tk.Entry(self)

        self.nom_entry.grid(row=0, column=1)
        self.prenom_entry.grid(row=1, column=1)
        self.tel_entry.grid(row=2, column=1)
        self.date_entry.grid(row=3, column=1)
        self.nombre_entry.grid(row=4, column=1)
        self.prix_entry.grid(row=5, column=1)
        button1 = tk.Button(self, text="Plus d'informations sur la disposition de la salle", command=show_info_place).grid(column = 3, row = 4)
        button2 = tk.Button(self, text="Enregistrer", command=self.save_data).grid(row=6, column=0, columnspan=2, pady=10)
        button3 = tk.Button(self, text="Plus d'informations sur les prix", command=show_info_prix).grid(column = 3, row = 5)

    def save_data(self):
        nom = self.nom_entry.get()
        prenom = self.prenom_entry.get()
        tel = self.tel_entry.get()
        date = self.date_entry.get()
        nombre = self.nombre_entry.get()
        prix = self.prix_entry.get()

        with open("artiste.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([nom, prenom, tel, date, nombre, prix])

class Interface_Spectateur(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.geometry("750x250")
        self.title("Spectateur")
        tk.Label(self, text="Choisissez un artiste:").grid(row = 1, column = 0)
        
        self.artiste_var = tk.StringVar(self)
        self.artiste_var.set("")  # initial value

        # Charge les artistes depuis le fichier CSV
        self.artistes = self.load_artistes()

        self.artiste_menu = tk.OptionMenu(self, self.artiste_var, *self.artistes)
        self.artiste_menu.grid(row=1,column = 1)
        
        
        def affichage_de_artiste():
            data = pd.read_csv('artiste.csv')
            nom = md.get_first_word(self.artiste_var.get())
            for i in range(len(data)):
                if data['nom'][i] == nom:
                    break
                
            
            nom_prenom = self.artiste_var.get()
            date = data['date'][i]
            dispo = data['dispo'][i]
            prix = data['prix'][i]
            
            tk.Label(self, text=f"Le concert de {nom_prenom} aura lieu le {date}.").grid(row=2, column=3)
            if dispo == 1 or dispo == 2:
                _or = prix + 50
                _mez = prix + 20
                value = tk.StringVar() 
                bouton1 = tk.Radiobutton(self, text=f"Carré d'or à {_or} euros ", variable=value, value=3).grid(row=3, column=3)
                bouton2 = tk.Radiobutton(self, text=f"Orchestre à {prix} euros", variable=value, value=1).grid(row=4, column=3)
                bouton3 = tk.Radiobutton(self, text=f"Mezzanine à {_mez} euros", variable=value, value=2).grid(row=5, column=3)
            elif dispo == 3:
                _mez = prix + 20
                value = tk.StringVar() 
                bouton1 = tk.Radiobutton(self, text=f"Fosse à {prix} euros", variable=value, value=1).grid(row=3, column=3)
                bouton2 = tk.Radiobutton(self, text=f"Orchestre à {_mez} euros", variable=value, value=2).grid(row=4, column=3)
             
            def confirmation_achat():
                f = open('mail.txt', 'r')
                contenue = f.readlines()
                f.close()
                
                if value == 1:
                    cout = prix
                elif value == 2:
                    cout = prix + 20
                else:
                    cout = prix + 50
                tk.messagebox.showinfo("Confirmation de votre Achat", f"Votre achat va vous coûter {cout} euros vous allez bientot recevoir un email")
                message = "Votre achat d'une place de concert de ",nom_prenom," pour le ",date," est confirmé !"
                md.send_email(contenue,'Confirmation', message )
    
            tk.Button(self, text="Confirmer votre achat", command=confirmation_achat).grid(column = 4, row = 6)
                

        tk.Button(self, text="Choisir cet artiste", command=affichage_de_artiste).grid(column = 1, row = 2)
                
    def load_artistes(self):
        artistes = []
        data = pd.read_csv('artiste.csv')
        for i in range(len(data)):
            nom = data['nom'][i]
            prenom = data['prenom'][i]
            artistes.append(f"{nom} {prenom}")
        return artistes
    
    
   
     
    