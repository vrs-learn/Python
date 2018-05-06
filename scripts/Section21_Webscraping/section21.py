#
#   WebScraping with BeautifulSoup
# To install BeautifulSoup , use below :
# pip install bs4

# To get the html page for any file , we need requests.
# pip install requests

import requests
from bs4 import BeautifulSoup

r=requests.get("https://pythonhow.com/example.html")
c=r.content

# print(c) # prints the content of the c i.e the example.html page

soup=BeautifulSoup(c,"html.parser") # html.parser is the parser for the content in the variable c

#print(soup.prettify()) # prints the html in a better format.

all=soup.find_all("div",{"class":"cities"})
#print(all)   # the variable all is a list. to get only the first element. we can use all[0]
#print(all[0])

# To print
print(all[0].find_all("h2")[0].text) # This prints the first h2 element of the first section of the element.

#to print the content in a loop. use below

for item in all:    # all is a list. so we can perform a loop on that list
    print(item.find_all("p")[0].text)
