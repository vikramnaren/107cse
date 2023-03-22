# Import pillow

# Import numpy
import numpy as np

#take and image and get the dimensions and then change each pixel value accordingly based on given equation
#Takes in an array
#output_value=255-input_value
def myImageInverse(inImage):
    rows, cols = inImage.shape
    arr = np.zeros(shape=(rows, cols))
    for i in range(rows):
        for j in range(cols):
            arr[i, j] = 255 - inImage[i, j]
    return arr