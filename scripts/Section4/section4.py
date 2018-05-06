######################################
###### CONDITIONALS ##################
######################################

#### FUNCTIONS #######################


###### Creating Funtions with User Inputs : ###########
def age_foo(age):
    new_age = float(age) + 50
    return new_age

age = input("Enter your age : ")
print(age_foo(age))


############## Conditionals ##########
##### Usage of IF ELSE ###############

a = 5
if a < 5 :
    print("Less than 5")
else:
    print("Equal to or greater than 5")

########## Multiple Else IF : ###########

a = 5
if a < 5 :
    print("Less than 5")
elif a == 5:
    print("Equal to 5")
else:
    print("Greater than 5")

############ Conditionals Advanced ##############
