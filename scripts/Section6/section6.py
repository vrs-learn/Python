##################### IMPORTANT #################
################# FILE HANDLING #################


#####################################################
######## Reading contents of a file , opening a file in Read Mode ##########
####################################################
file=open("example.txt",'r')
print(type(file))
#content=file.read()  # this is used to read the contents and it reads in String format.
#print(content)

newcontent=file.readlines() # this reads in a array.
file.seek(0)
print(newcontent)

#For Deleting \n from the contents use rstrip function

newcontent=[i.rstrip("\n") for i in newcontent]
print(newcontent)

file.close()  # A very important step is to close the file


######################################
###### Creating a File :
######################################
file=open("newexample.txt",'w')
file.write("Line 1\n")
file.write("Line 2") # This is writing line to newexample.txt file. But the issue is that it will always overwrite the files.
file.close

#For doing the operation in a loop :

file=open("newexample.txt",'w')
l=['Line1','Line2','Line3']
for item in l:
    file.write(item+"\n")
file.close


######################################
###### Appending to a File :
######################################

file=open("newexample.txt",'a')
file.write("Line4")
file.close()


###################################
######### With Statement ##########
###################################

# The benefit of with command is that we donot need to close the file after closing the function

with open("newexample.txt",'a+') as file :
    file.seek(0)
    content=file.read()
    file.write("\nLine6")
