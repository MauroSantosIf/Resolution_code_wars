def disemvowel(string_):
    vowels = "aeiouAEIOU"
    return "".join([char for char in string_ if char not in vowels])

print(disemvowel("This website is for losers LOL!"))