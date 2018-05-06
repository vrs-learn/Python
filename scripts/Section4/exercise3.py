def cel_to_fah(deg_in_cel):
    deg_in_fah = deg_in_cel*9/5+32
    return deg_in_fah

deg = float(input("Please input deg in Celcius :"))

if deg < -273.15:
    print("Temperature cannot be lower than -273.15")
else:
    print(cel_to_fah(deg))
