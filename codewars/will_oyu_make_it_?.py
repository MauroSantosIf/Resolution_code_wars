def zero_fuel(distance_to_pump, mpg, fuel_left):
    #Happy Coding! ;
    distance_max = mpg * fuel_left
    return distance_max >= distance_to_pump

print(zero_fuel(50,25,2))