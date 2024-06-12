import secrets
import string
import hashlib

class TokenGen:
    def __init__(self):
        pass
      
    def generarKey(self):
        longitud=14
        caracteres = string.ascii_letters + string.digits + string.punctuation
        contrasena = ''.join(secrets.choice(caracteres) for _ in range(longitud))
        secretKeyB = contrasena.encode('utf-8')
        keyHash = hashlib.sha256(secretKeyB).hexdigest()
        keySting= str(keyHash)
        return keySting


# uso
#generador = GeneradorToken()
#hash_resultante = generador.generarKey()
#print(hash_resultante)




