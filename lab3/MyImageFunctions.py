from PIL import Image, ImageOps

# Import numpy
import math
#for sqrt
import numpy as np
from numpy import asarray

def myImageResize(inputArr, numRows, numCols, method):
    #get cols and rows from input matrix
    rows, cols = inputArr.shape
    #created empty matrix making sure it can take in floats

    resizeArr = np.zeros((numRows, numCols), dtype=np.float32)   

    for i in range(numRows):
        for j in range (numCols):
            #from hw1 to check and not cause bounds error
            m_inter = (((i-0.5)/numRows) * rows) + 0.5  
            n_inter = (((j-0.5)/numCols) * cols) + 0.5
    
            if method == 'nearest':
                m_inter = round(m_inter)
                n_inter= round(n_inter)
                resizeArr[i-1, j-1]=inputArr[m_inter-1,n_inter-1]
            #check conditions for whether integer is greater or less than
            elif method == 'bilinear':

                #check if integer value
                if m_inter == int(m_inter):
                    m1=m_inter
                    m2=m_inter
                else:
                    #check if greater
                    if m_inter<1:
                        m1=1
                        m2=2
                    #check if less than
                    elif m_inter>rows:
                        m1 =rows-1
                        m2 =rows
                    else:
                        m1 = math.floor(m_inter)
                        m2 = math.ceil(m_inter)
                if n_inter == int(n_inter):
                    n1=n_inter
                    n2=n_inter
                else:
                    #check if greater

                    if n_inter<1:
                        n1=1
                        n2=2
                    #check if less than
                    elif m_inter>cols:
                        n1 =cols-1
                        n2 =cols
                    else:
                        n1 = math.floor(n_inter)
                        n2 = math.ceil(n_inter)
                m1 -= 1; m2 -=1; n1-=1; n2-=1
                #assign p valules based on points gathered
                p1 = inputArr[m1, n1]
                p2 = inputArr[m1, n2]
                p3 = inputArr[m2, n1]
                p4 = inputArr[m2, n2]
                #pass values to bilinear and make it return value to p5 so that we are able use it for asgining value to scaled matrix
                p5 = mybilinear(m1, n1, p1, m1, n2, p2, m2, n1, p3, m2, n2, p4, (m_inter-1), (n_inter-1))

                resizeArr[i-1, j-1]=p5
    return resizeArr
       




def mybilinear(x1, y1, p1, x2, y2, p2, x3, y3, p3, x4, y4, p4, x5, y5):
    #use the formula from the lecture slides
    r1=(p3-p1)*((x5-x1)/(x3-x1))+p1
    r2=(p4-p2)*((x5-x2)/(x4-x2))+p2

    p5=(r2-r1)*((y5-y1)/(y2-y1))+r1

    return p5


def myRMSE(num1Matrix, num2Matrix):
    #get dimensions for both matrices, but we onl use row1 and col2
    row1, col1 = num1Matrix.shape
    row2, col2 = num2Matrix.shape


    RMSE=0    
    for i in range(1,row1):
        for j in range(1, col2):
            #for assurance that there was no round off error before squaring, we use float
            RMSE += (float(num1Matrix[i][j])-float(num2Matrix[i][j]))**2

    RMSE = RMSE / ( row1*col2)
    return math.sqrt(RMSE)
