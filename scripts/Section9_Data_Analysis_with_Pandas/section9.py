###################
## PANDAS : Python Library which provides Data Structures & Data Analysis tools
## Jupyter NoteBooks : An opensource tool which is used for data
## It allows Data to be loaded from different sources to analyse the data and produce the result.
## And also the visualization.
###################
## Pandas is a high level library . It requires numpy
#### Installation of pandas :
## pip install pandas
##########
# IPython :
# Note: In the next lecture we're going to use an enhanced Python interactive shell called IPython. IPython is just like the normal shell you get when you run python , but it provides better printing of large output.
# This makes IPython suitable for data analysis as it prints data in a well structured format. You can install IPython with pip:
# pip install ipython , or
# pip3 install ipython , or
# python3 -m pip install ipython
#
# To login to ipython , just type "ipython" on command prompt :
# Installing geopy - a library for getting co-ordinates based on address and vice versa
#working with pandas on ipython

import pandas

# creating a data frame :
df1 = pandas.DataFrame([[2,4,6],[10,20,30]])

print(df1)
# Above command prints :
#    0   1   2
#0   2   4   6
#1  10  20  30

# To Add a Column name for the data frame :

df1 = pandas.DataFrame([[2,4,6],[10,20,30]],columns=["Price","Age","Value"])
print(df1)

# To Add a Index name :
df1 = pandas.DataFrame([[2,4,6],[10,20,30]],columns=["Price","Age","Value"],index=["First","second"])
print(df1)

#Another way of creating a Panda Data Frame :
# In this way we provide a dictionary to the list of data frame
df2 = pandas.DataFrame([{"Name":"John","Surname":"Zen"},{"Name":"Jack"}])
print(df2)

# All above are data structures.
# Actions can be performed on the above :

type(df1)
#In [5]: type(df1)
#Out[5]: pandas.core.frame.DataFrame

# MEthods attached to Pandas object :
dir(df1)

#TO Calculate the Mean of the df1
df1.mean()

#In [10]: type(df1.Price)
#Out[10]: pandas.core.series.Series

##########################################################################################33
############# JUPYTER #############
###################################
# Install JUPYTER
# pip install jupyter

# Jupyter notebook is actually a browser
# to enter into browser : type on command line :
# jupyter notebook

# Once selected the Python notebook inside the jupyter notebook.
# type Enter to enter multiple lines
# to run the command , press Ctrl + Enter
# to go to new command, press Alt + Enter
# to run the command and go to new command line again press Shift + Enter
# To delete a command , press Esc & type : dd
# if you press Esc ( the box turns into Grey or Blue box , i.e Command mode )
# if you are typing commands in box, its in type mode and the box is in Green Color


##########################################################################################
## WORKING WITH PANDAS on JUPYTER ############
## Importing XLSX, CSV files with Python #####
##############################################

# To Load XLSX files in Python, Pandas require xlrd library.
# to install : pip install xlrd

import pandas
# LOADING CSV
df1 = pandas.read_csv("pandas/supermarkets.csv") # for reading csv files.
print(df1)

# to set index to a specific column in csv file,
df1.set_index("ID") # here ID is the name of the column

df1.shape # this command tells the no of rows and columns in the df1 object

# LOADING JSON
df2 = pandas.read_json("pandas/supermarkets.json")
print(df2.set_index("ID"))


# LOADING XLSX File
df3 = pandas.read_excel("pandas/supermarkets.xlsx",sheetname=0)
print(df3.set_index("ID"))

# LOADING Text File with Comma as a seperator
df4=pandas.read_csv("pandas/supermarkets-commas.txt") # in case the seperator was not a comma, we would need to provide another parameter of seperator with the corresponding value
print(df4.set_index("ID"))

# LOADING Text file with Semi Colons :
df5=pandas.read_csv("pandas/supermarkets-semi-colons.txt",sep=";") # here we are explicitly mentioning the seperator as semi colon
print(df5.set_index("ID"))


########## PANDAS ALSO READS ONLINE FILES i.e with URL ################

df6=pandas.read_csv("http://pythonhow.com/supermarkets.csv")
print(df6)


##### Indexing and Slicing #####
# Accessing parts of the Data Frame
# loc method

df7=pandas.read_json("http://pythonhow.com/supermarkets.json")
df7=df7.set_index("Address")

# Extracting data using Label Based Indexing:
print(df7.loc[:,"Country"])
print(df7.loc["332 Hill St","Country"])

# Extracting data using Position based Indexing :
print(df7.iloc[1:3,1:3])

#### If you want to access data frame with a combination of both label based indexing & position based indexing.

print(df7.ix[3,"Name"])

print(df7.index)  # it prints only the Indexes of the data frame
print(df7.columns)  # It prints only the columns of the data frame.
#########################################
############### Deleting Columns ########
#########################################

print(df7.drop("332 Hill St", 0))

# If you want to delete based on indexig :

print(df7.drop(df7.index[0:3],0))

#############################################################
####### Updating and Adding New Columns in Data Frame #######
#############################################################

# Adding New Column :

df7["Continent"]=df7.shape[0]*["North America"]

#Modifying a Column can be :

df7["Continent"]=df7["Country"] + "," + "North America"
print(df7)

######### Adding a ROW to a Data Frame ###########
### THere is no easy way of adding a row to a Data Frame
### First Transpose the existing Data Frame and then add a column.
### And then again Transpose it.

df7_t = df7.T
print(df7_t) # this is the transposed Data Frame

# Lets add a column now :

df7_t["My Address"]=["My City","My Cuntry",10,7,"My Shop","My State","My Continent"]
print(df7_t)
df7=df7_t.T
print(df7)

##########################################################3
#### IMPORTING GEOPY ######################################

import geopy

# Process to convert Address to Latitude and Longitude is called Geo coding
# Process to conver Latitiude to Longitude to ADdress is called Reverse Geo coding

from geopy.geocoders import Nominatim
nom = Nominatim()

print(nom.geocode("3995 23rd St, San Francisco, CA 94114"))

n=nom.geocode("3995 23rd St, San Francisco, CA 94114")
print(" The latitude is : ", n.latitude)
print(" The longitude is : ", n.longitude)

## Below example we add a column with co-ordinates in the data frame
df7 = pandas.read_csv("pandas/supermarkets.csv")
df7["Address"] = df7["Address"] + ", " + df7["City"] + ", " + df7["State"]
df7["Coordinates"] = df7["Address"].apply(nom.geocode)  # apply is an inline function which can apply a function on the input

## Adding Latitude and Longitude in the Data Frame :

df7["Latitude"]=df7["Coordinates"].apply(lambda x: x.latitude if x != None else None)
df7["Longitude"]=df7["Coordinates"].apply(lambda x: x.longitude if x != None else None)
print(df7)
