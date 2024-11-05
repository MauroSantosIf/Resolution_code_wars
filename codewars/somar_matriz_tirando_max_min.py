def sum_array(arr):
    #your code here
    if arr is None or len(arr) <=1:
        return 0

    max_arr = max(arr)
    min_arr = min(arr)
    
    """
    Tentei de outra forma, com lista comprehesion, só que estava tirando todos os valores repetidos
    e só precisava tirar apenas o maior e o menor
    """

    arr_copy = arr.copy()
    arr_copy.remove(max_arr)
    arr_copy.remove(min_arr)
    soma = sum(arr_copy)
    return soma

print(sum_array([1,1,1,2,8,9,9,9]))


"""
Refatorando o código
def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)

"""