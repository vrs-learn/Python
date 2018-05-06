
def cel_to_fah(deg_in_cel):
    deg_in_fah = deg_in_cel*9/5+32
    return deg_in_fah

temperatures=[10,-20,-289,100]

file=open("celcius_deg.txt",'w')
for deg in temperatures:
    if deg > -273.15:
        file.write(str(cel_to_fah(int(deg)))+"\n")

file.close
