from PIL import Image, ImageOps

# Import numpy
import numpy as np
from numpy import asarray

im = Image.open('Beginnings.jpg')

# Show the image.
im.show()

# Convert image to gray scale.
im_gray = ImageOps.grayscale(im)

# Show the grayscale image.
im_gray.show()

# Get access to the pixel values through the matrix im_gray_pixels.
im_gray_pixels = asarray(im_gray)

#get dimensions in rows and cols of gray image
rows, cols = im_gray_pixels.shape
print("Image size is: ", rows, "rows x", cols, "columns")
#copy pixel values from gray to new _arr
new_arr =np.zeros(shape=(rows, cols))
for i in range(rows):
    for j in range(cols):
        new_arr[i][j] = im_gray_pixels[i][j]
      

#loop to compute max pixel values
max = new_arr[0][0]
for i in range(rows):
    for j in range(cols):
        if(new_arr[i][j]>max):
            max = new_arr[i][j]
print(max)

# rotate 90 degrees counterclockwise
new_arr2 =np.zeros(shape=(cols, rows))
for j in range(cols):
    for i in range(rows):
        new_arr2[cols-j-1,i]=new_arr[i, j]
data=Image.fromarray(new_arr2)
data.show()
picture = Image.fromarray(np.uint8(data))

# rotate 90 degrees clockwise
for j in range(cols):
    for i in range(rows):
        new_arr2[j,rows-i-1]=new_arr[i, j]
data=Image.fromarray(new_arr2)
data.show()
picture = Image.fromarray(np.uint8(data))

#compute new max for rotated image
rows, cols = new_arr2.shape
print("Image size is: ", rows, "rows x", cols, "columns")
for i in range(rows):
    for j in range(cols):
        if(new_arr2[i][j]>max):
            max = new_arr[i][j]
print(max)