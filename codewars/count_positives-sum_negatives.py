def count_positives_sum_negatives(arr):
    positive =[]
    negative =[]
    final = []

    if arr == [] or arr == [0]:
        return []

    for x in arr:
        if x > 0:
            positive.append(x)
        else:
            negative.append(x)

    count_positives = len(positive)
    sum_negatives = sum(negative)
    
    final.append(count_positives)
    final.append(sum_negatives)
    return final

print(count_positives_sum_negatives([0]))

"""
Refatorando
def count_positives_sum_negatives(arr):
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg] if len(arr) else []

"""