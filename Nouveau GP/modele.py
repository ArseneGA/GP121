"""
fichier fonction
"""

import smtplib
import pandas as pd
import tkinter as tk
from vue import *
 

def write_art_to_csv(self):
    with open('ariste.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(self.nom,self.prenom,self.number,self.date,self.chair_position,self.prix_place)


def get_first_word(sentence):
  # split the sentence into a list of words
  words = sentence.split()
  # return the first word
  return words[0]


def two_funcs(*funcs):
    def two_funcs(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return two_funcs

    

        
def send_email(to, subject, message):
    # Spécifiez le serveur de messagerie et les paramètres de connexion
    server = smtplib.SMTP('smtp.gmail.com', 465)
    server.login('olympiaipsa@gmail.com', 'Ipsa123!')
    
    # Construisez le message
    msg = f"Subject: {subject}\n\n{message}"
    
    # Envoyez le message
    server.sendmail('olympiaipsa@gmail.com', to, msg)
    
    # Déconnectez-vous du serveur
    server.quit()