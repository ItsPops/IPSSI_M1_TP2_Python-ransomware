from Cryptodome.PublicKey import RSA
from variable import *

def generate_pair():
    print("Generating new key pairs...")
    key = RSA.generate(2046)
    openedPrivateKey = key.export_key()
    openedPublicKey = key.publickey().export_key()

    file = open(publicKey,"wb")
    file.write(openedPublicKey)
    file.close
    file = open(privateKey,"wb")
    file.write(openedPrivateKey)
    file.close