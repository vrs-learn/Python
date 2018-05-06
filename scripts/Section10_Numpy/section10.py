##
# Numpy is a Python library that provides a multidimensional Array
##

import numpy
n=numpy.arange(27)

print(n)
#([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,       17, 18, 19, 20, 21, 22, 23, 24, 25, 26])
print(type(n))

# To convert a normal numpy array into two dimesnsional
n.reshape(3,9)
n.reshape(3,3,3)

# To convert a list into a numpy arrary :

m=numpy.asarray([[123,231,2312],[],[]])
print(m)
# output of above cmd : numpy.ndarray

#############################################################
#### Reading Image using OpenCV into Numpy Array ############

import cv2

im_g=cv2.imread("smallgray.png",0) # Here 0 means GrayScale & 1 means in BGR i.e Blue Green & Red
# The values in this array shows the intensity of the the gray scale. 0 being black and 255 being white

print(type(im_g))

## TO create an image :
cv2.imwrite("newsmallgray.png",im_g)

#####################################################
##### INDEXING , SLICING & ITERATING the NUMPY Arrays
#####################################################

# First working with the 2 dimesnsional array
# Using the above im_g array :
print("Printing the first two columns of the 2 dimesnsional array")
print(im_g[0:2]) # This will just print the first two rows
print(im_g[0:2,2:4]) # this will print the first two rows and the 2nd & 3rd column ( remember in the series like 2:4 , the last number is not inclusive )

# To get the no of rows and columns of the numpy array , type :
im_g.shape


# Iteration :
# For iteration , each time the loop reads a row

for i in im_g:
    print(i)

# For Transposing an array, use .T

for i in im_g.T:
    print(i)

# for accessing the numpy array one by one use flat.

for i in im_g.flat:
    print(i)

#################
## concatenating two Numpy arrays :
################

# Using the method hstack ( Horizontal stack ) or vstack ( Vertical Stack )

imh=numpy.hstack((im_g,im_g))

#or you can use vstack for virtual Stack
imv=numpy.vstack((im_g,im_g))


################
## Splitting the arrays
################

# Splitting can be done in two ways : Horizontal or vertical
# During splitting the new array should be equally dividable

lst=numpy.vsplit(imh,5) # the variable lst is a list of Numpy arrays 
