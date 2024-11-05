def get_count(sentence):
    vowels = "aeiouAEIOU"
    count = 0
    for i in sentence:
        if i in vowels:
            count += 1
    return count

print(get_count('AEIOU'))

"""
Refatorando 

def getCount(sentence)

    return sum(1 for let in sequence if let in 'aeiouAEIOU')
"""