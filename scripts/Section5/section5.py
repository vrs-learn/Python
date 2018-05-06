########### LOOPS #################

#### Two Kind of Loops #####
#### FOR LOOP ###########

emails=['me@gmail.com','you@hotmail.com','they@gmail.com']

for item in emails:
    if 'gmail' in item:   # This is for finding a string in the variable #grep
        print(item)

#########################################
##### For Loop with multiple Lists :
##########################################


names=['james','john','smith']
email_domains=['gmail','hotmail','yahoo']

for i,j in zip(names,email_domains): # use zip function to use two lists in a single for loop
    print(i,j)


#### WHILE LOOP #########

password = ""
while password != 'python123' :
    password = input("Enter Password : ")
    if password == 'python123' :
        print("You are logged in:!")
    else:
        print("Sorry, Try Again!")
