from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP, AES
from variable import *
import os

def decrypt(fileToDecrypt, privateKeyFile):
    """
    USE EAX mode to allow detection of unauthorized modifications
    """
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
    os.remove(fileToDecrypt)


