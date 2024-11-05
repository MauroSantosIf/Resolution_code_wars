def are_you_playing_banjo(name):
    # Implement me!

    if name[0] in ('R','r'):
        return name + " plays banjo"
    
    return name + " does not play banjo"

print(are_you_playing_banjo('Mauro'))
