def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])

print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))

"""
Refatorando
sum_two_smallest_numbers = lambda numbers: sum(sorted(numbers)[:2]) if len(numbers) >= 4 else 0
"""