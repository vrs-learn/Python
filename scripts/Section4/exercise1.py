def cel_to_fah(deg_in_cel):
    deg_in_fah = deg_in_cel*9/5+32
    return deg_in_fah

deg = input("Please input deg in Celcius :")
print(cel_to_fah(float(deg)))
