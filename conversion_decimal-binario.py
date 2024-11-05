def for_binario(n):
    if isinstance(n, int):
        return bin(n)[2:]
    
    raise ValueError("Argumento inválido")

def for_decimal(b):
    if isinstance(b, str) and all(bit in '01' for bit in b):
        return int(b,2)
    return ValueError("Argumento inválido")

print(for_binario(33))
print(for_decimal('10111101'))