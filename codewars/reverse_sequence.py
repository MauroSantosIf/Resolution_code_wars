def reverse_seq(n):
    inverse = []
    if n > 0:
        for x in range(n,0,-1):
            inverse.append(x)
    else:
        return False
    return inverse
print(reverse_seq(5))

# usando lambda
reverse_seq = lambda n:list(range(n,0,-1))
