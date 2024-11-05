import sys

indice = 0

entrada = sys.stdin.read().strip().split()

while True:

    first_entry = int(entrada[indice])
    indice += 1
    
    if first_entry == -1:
        break

    numbers = [first_entry]
    
    for _ in range(999):
        numbers.append(int(entrada[indice]))
        indice += 1
    
    N = int(entrada[indice])
    indice += 1
    
    K = numbers.count(N)

    print(f"{N} appeared {K} times")
