
# To take input from user use as below :
age = input("Write your age :")

#Converting a text into Integer or float
# int(variable)
new_age = int(age) + 50
print("Your New age is : " , new_age)

#To concatenate two strings :
var1 = "this is the new "
var2 = "Program for Python"
print (var1 + var2)

#How to know the type of the variable :
#type(variable)
print(type(new_age))

############### NUMBERS AND OPERATORS #############
#Order of execution of OPERATORS
# the ** respresnts POWER of . In below ex its 3 to the power of 2
# first precedence : brackets
# Second precedence : power
# third precedence : division and multiplication ( in the below exp, since 10 / 5 comes first, so it will be executed first. & then the multiplication will be exected )
# fourth precedence : Addition and subtraction are done after that.
print ( 20 - 10 / 5 * 3 ** 2)
# first operation : ( 20 - 10 / 5 * 9 )
# second operation : ( 20 - 2 * 9 )
# third operation : ( 20 - 18 )
# Fourth operation : 2

##################################################
############### STRING MANUPULATIONS #############
# To check all the methods available for any variable :
var1 = "Some Text"

#To convert a variable into string , user str():
print(str("123"))

#Lists all the functions available for variable var1
print(dir(var1))
#Some methods for the strings :
print(var1.replace("e","i"))
print(var1.upper())

#To know more about the methods, use help function :
#This prints, how to use the function replace.
help("".replace)

##################################################
########### Sring Indexing #################
#Every String is stored in an indexed fashion. So if String is a = "Hello There!" ,then a[0] would retrieve H, and a[11] would retrieve !
a = "Hello There!"
print("The second character of the string a is : ", a[1])
type(a[1])

#Another method of indexing is in reverse order .
#To print the value from last , use a[-1] which prints the last character.
print("Second last character of a is : ", a[-2])

## Another way of parts of string is as below :
#The below substring will return from 1st character till 2nd ( but its exclusive ). So the below string only prints the character at first position.
print("String from 1st to 2nd ( but 2nd is exclusive ) : ", a[1:2])

#Same way the substring can also be calculated in reverse order : as below :
print("Last and second last character of a is : ", a[-2:])


##################################################
############ LISTS ###############################

#To create a list , use square brackets :
#and you can save different data types
c = ["H",2,"Hello"]

#To print all the functions available for a list are :
dir(list)
type(c[1]) # this prints the data type of the 2nd value in the list
type(c[:2]) # this prints the data type as list as it contains first two values of the list.

##################################################
############# TUPLES #############################

#Tuples is same as List, but the difference is that you cannot change it.

print("The functions available for list are : ")
print(dir(list))

print("The functions available for Tuple are : ")
print(dir(tuple))

d = ("hello" , 2 , 5.6)
print(d)
##################################################
######## DICTIONARIES ###########################
#DICTIONARIES are pair of Key and value

d = {"Name":"John" , "Surname":"Smith"}
print(d)

# We can also add a tuple in the Value of the DICTIONARIES :
d = {"Name":"John" , "Surname":"Smith", "Cities":("Rio-de-Jenaio" , "NewYork", "Guiena")}
print(d["Name"])
print(d["Cities"][1])

print(d.keys()) # prints all the keys of the dictionary d 

#####################################
######## FUNCTIONS ##################

#to define a function :

def function_name(input_value):
    #do some operation
    add_value = input_value + 100
    return add_value

print("the sum of 50 and 100 is : ", function_name(50))
