import sys

# Dicionário para armazenar os tamanhos de ciclo já calculados
memo = {}

# Função para calcular o tamanho do ciclo de um número n
def ciclo(n):
    if n in memo:
        return memo[n]  # Retorna o tamanho do ciclo armazenado

    original_n = n
    tamanho = 1
    while n != 1:
        if n in memo:
            tamanho += memo[n] - 1  # Adiciona o tamanho do ciclo já conhecido
            break
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        tamanho += 1

    memo[original_n] = tamanho  # Armazena o resultado para n
    return tamanho

# Lendo cada linha da entrada padrão até o EOF
for linha in sys.stdin:
    # Lendo os valores i e j
    i, j = map(int, linha.split())
    
    # Definindo o intervalo corretamente, independentemente da ordem de i e j
    inicio, fim = min(i, j), max(i, j)
    
    # Encontrando o maior tamanho de ciclo no intervalo [inicio, fim]
    max_ciclo = 0
    for num in range(inicio, fim + 1):
        max_ciclo = max(max_ciclo, ciclo(num))
    
    # Imprimindo o resultado no formato solicitado
    print(f"{i} {j} {max_ciclo}")
