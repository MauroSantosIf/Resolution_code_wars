"""
This kata is about multiplying 
a given number by eight if it is an even number and by nine otherwise.

def simple_multiplication(number) :
    # Your code goes here
    if number % 2 == 0:
        return number * 8
    return number * 9
"""

# refatorando 
def simble_multiplication(number):
    return number * 9 if number % 2 else number * 8
print(simble_multiplication(3))