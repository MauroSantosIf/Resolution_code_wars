def abbrev_name(name):
    name = name.split()
    return f"{name[0][0].upper()}.{name[1][0].upper()}"

print(abbrev_name('Sam Harris'))


"""
def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()

"""