def is_isogram(string):
    string = string.replace(" ","").lower()
    return len(string) == len(set(string))


print(is_isogram('maurosantos'))


"""
Refatorando 

def is_isogram(string):
    return len(string) == len(set(string.lower()))

Com expressão lambda:

is_isogram = lambda s: len(set(s.lower())) == len(s)
"""
