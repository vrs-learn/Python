"""
This is the part where the documentation of the module goes.
This script creates an empty file.
"""
###############################
##### More Functionalities :
##### What is a Module
##### OS Module ,documentation
##### Working with Date and Time
###############################

# OS Module :
# To use the OS module, import the module :
import os
print(os.listdir())
print(type(os.listdir()))
print(dir(os.listdir()))

############ Importing Libraries is the same as Modules . Libraries are a bunch of modules collected and stored together.
#### All folders inside the lib folder of the installation are the libraries.

#How to Install a third party module or library , type below command on the command prompt
#pip install glob2
#here glob2 is a library.

# How to use the __doc__ part of any function
# all the text written within """ """ , is printed when __doc__ is called.



def create_file():
    """ this function will create a file """
    with open("sample.txt",'w') as file :
        file.write("")


##### Working with Date and Times :

import datetime

print(datetime.datetime.now()) # this prints the current time

now=datetime.datetime.now() # stores the value of now in variable now

yesterday=datetime.datetime(2016,5,13,11,0,0,0) # sets the time of 13th May 2016 11:00:00 in the variable yesterday

delta=now-yesterday # gets the difference of the two dates

print("the diff between now and yesterday :" , delta.days) # prints the days of difference between the two dates
print("The diff of secs between the two dates is : ", delta.total_seconds()) # total seconds of difference between the two dates

#####################
# Converting a time into string :
##################

print("the time in string is : ", now.strftime("%Y-%m-%d-%H-%M-%S-%f"))  # for reference check site : www.strftime.org


############ Adding some days in a date ###########
after=now+datetime.timedelta(days=2)
print(after)

############## Using time function ##############
# To sleep for few seconds, use time(5) , this will sleep for 5 seconds
import time


lst=[]
for i in range(5):
    lst.append(datetime.datetime.now())
    time.sleep(1)


for i in lst:
    print(i)
