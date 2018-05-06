# OpenCV - Image and Video processing Python library
#
# To install OpenCV
# pip install opencv-python
#

import cv2

img = cv2.imread("galaxy.jpg",0) # 1 - RBG , 0 - Black&White , -1 - adds an alpha panel ( used for transparency )

print(type(img))    # prints that its a Numpy array
print(img)          # This prints the Numpy Array
print(img.shape)    # Prints the resolution of the Image
print(img.ndim)     # Prints the Dimension of the Picture. If the Image is read with option 1, it would show the Dimensions as 3


resized_image = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("Galaxy", resized_image)    # Displays a window with the image. "Galaxy is the name of the window"
cv2.imwrite("Galaxy_resized.jpg",resized_image)
cv2.waitKey(0)           # the window remains open for 2000 ms. If you set it to 0 , the user can close the window.
cv2.destroyAllWindows()
