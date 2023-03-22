from PIL import Image, ImageOps

# Import numpy
import numpy as np
from numpy import asarray


#set rows and cols to desired dimensions
rows = 100
cols = 256
 
#create image with assigned rows and cols
img  = Image.new( mode = "RGB", size = (cols, rows))
pixelArray = asarray(img)

# ensure the dimensions are set by using resize, so that we dont get a value error
pArray= np.resize(pixelArray, (rows, cols))

#print array
# for i in range(rows):
#     for j in range(cols):
#        print(pArray[i][j])

rows, cols = pArray.shape #get dimensions of array in order

#print("Image size is: ", rows, "rows x", cols, "columns")
#assign to each value in the array the respective col number since cols go from 0-255
im_gray_pixels = np.zeros(shape=(rows, cols))
for i in range(rows):
    for j in range(cols):
        im_gray_pixels[i, j] = j

#convert from array to image, display and save as a .tif
data=Image.fromarray(np.uint8(im_gray_pixels))
data.show()
data.save('task3.tif')

#calculate average pixel value
sum = 0
for i in range(rows):
    for j in range(cols):
        sum+=im_gray_pixels[i,j]
print(sum/(cols*rows))