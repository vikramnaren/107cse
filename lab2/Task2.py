# Import pillow
from PIL import Image, ImageOps

# Import numpy
import numpy as np
from numpy import asarray

from MyImageFunctions import *

# Read the image from file.
im = Image.open('Watertower.tif')
im.show()
arr = asarray(im)

new_arr = myImageInverse(arr)

#print max pixel value
# rows, cols = new_arr.shape
# max = new_arr[0][0]
# for i in range(rows):
#     for j in range(cols):
#         if(new_arr[i][j]>max):
#             max = new_arr[i][j]
# print(max)

#covert array to image and display it. Finally save it as a .tif
picture = Image.fromarray(np.uint8(new_arr))
picture.show()
picture.save("new_watertower.tif")