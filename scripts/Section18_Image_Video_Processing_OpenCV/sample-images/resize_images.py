#
# Exercise to Reimage all the Images in a Directory 
#

import os
import cv2

img_dir = "C:\Vaibhav\Learning\Python\scripts\Section18_Image_Video_Processing_OpenCV\sample-images"
type(os.listdir(img_dir))
list_of_files = os.listdir(img_dir)

for file in list_of_files:
	img = cv2.imread(file,0)
	resized_img = cv2.resize(img, (100,100))
	cv2.imwrite(file.split(sep=".")[0] + "_resized." + file.split(sep=".")[1] , resized_img)

	