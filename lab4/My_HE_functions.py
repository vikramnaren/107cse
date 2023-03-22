# Import numpy
import numpy as np

def compute_histogram(image_pixels ):
    #get dimesnsions and setup vector for histogram
    rows, cols = image_pixels.shape
    hist = np.zeros(shape=(256))
    for i in range(0, rows):
        for j in range (0, cols):
            #assign pixel values and it should add up to 1
            hist[int(image_pixels[i][j])] += 1 
    hist=hist/(rows*cols)
    return hist



def equalize(image_pixels):
    rows, cols = image_pixels.shape
    #get dimnesions
    output=image_pixels
    #computer the histogram and assign it to value so that when using the formula from 3-15
    hist =compute_histogram(image_pixels)
    s = np.zeros(shape=(256))
    L=256
    #L constant from textbook
    #second nested for loop through the rows and columns to assign each pixel value in the out image to the transformed pixel
    for k in range(L):
        for i in range(k):
            s[k] += hist[i]
        s[k] = (L - 1) * s[k]
    for i in range(rows):
        for j in range(cols):
            output[i,j]=s[int(image_pixels[i][j])]    
    return output
        

    




def plot_histogram( hist ):
    # plot_histgram  Plots the length 256 numpy vector representing the normalized
    # histogram of a grayscale image.
    #
    # Syntax:
    #   plot_histogram( hist )
    #
    # Input:
    #   hist = The length 256 histogram vector..
    #
    # Output:
    #   none
    #
    # History:
    #   S. Newsam     10/23/2022   created

    # Import plotting functions from matplotlib.
    import matplotlib.pyplot as plt

    plt.bar( range(256), hist )

    plt.xlabel('intensity value');

    plt.ylabel('PMF'); 

    plt.show()
