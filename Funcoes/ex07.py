import random
import string

def gera_senha(tamanho = 8):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))

    return senha

senha = gera_senha(10)
print("A senha é: ", senha  )