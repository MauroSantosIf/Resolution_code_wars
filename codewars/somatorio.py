'''
Forma de fazer um somatório simples
'''


def summation(num):
    termos = [str(i) for i in range(1, num + 1 )]
    soma = sum(range(1, num + 1))
    print(f"{num} -> {soma} ({' + '.join(termos)})")
    return soma

resultado = summation(8)
print(resultado)

'''
Refactoring of question
def summation(num):
    return sum(range(1,num+1))


'''