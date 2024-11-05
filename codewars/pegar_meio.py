def get_middle(s):
    tamanho = len(s)
    meio = tamanho // 2

    return s[meio] if tamanho % 2 != 0 else s[meio-1:meio+1]
print(get_middle("testing"))
