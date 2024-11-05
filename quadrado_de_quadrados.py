# verificando se n é um quadrado perfeito
def is_square(n):    
    if n < 0:
        return False
    raiz = int(n**0.5)
    return raiz * raiz == n

print(is_square(3))

'''
refatorando 

def is_square(n):    
    return n >= 0 and (n**0.5) % 1 == 0
'''