############# Loading JSON files in Python ###########
############# Making a Program Case Insesnsitive ########

import json
data = json.load(open("data.json"))
print(type(data))

userinput = input("Enter the keyword in small letter :").lower() # the lower converts the string into lower case.

try:
    result = data[userinput]
    for i in result:
        print(i)
except KeyError:
    print("No such word found in the dictionary.")

###############################################
####### Another way of doing this is :
###############################################

def translate(w):
    if w in data:
        return data[w]
    else:
        return "The word does not exists."

word = input("Enter a word again :").lower() # the lower converts the string into lower case.

print(translate(word))

################################################
## CALCULATING SIMILARITY RATIO : #############
################################################

import difflib # this is a library
from difflib import SequenceMatcher
print(SequenceMatcher(None,"rainn","rain").ratio()) # this prints the ratio of the match between the two values.

############## Finding the best match of a word out of a list
############## USING get_close_matches function from difflib

from difflib import get_close_matches

get_close_matches("rainn",data.keys())      # this will print 3 closest values of the matches ( default no of matches is 3 .) . Note the values that are returned are in the sorted order.
get_close_matches("rainn",data.keys())[0]  # this will return the first element of the matches that were found .
