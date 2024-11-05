def fake_bin(x):
    # x é o array
    if x == "":
        return 0

    lista_resultante = []

    for y in x:
        if int(y) >= 5:
            lista_resultante.append('1')
        else:
            lista_resultante.append('0')
    return ''.join(lista_resultante)

print(fake_bin([1,2,3,7,8,9]))

"""
Refatorando: 

def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)
"""