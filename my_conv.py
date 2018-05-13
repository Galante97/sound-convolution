## JAMES GALANTE
## JOSH WEINICK

import numpy as np
import math


def  myconv(x,h):
 
 
############################################################################
# A function to generate the output signal y as convolution of input signal
# x and impulse response signal h
############################################################################

# INPUT PARAMETERS---------------------------------------------------------
# x: input signal
# h: impulse response
    len_x = len(x) # length of x
    len_h = len(h) # length of h
############################################################################
# Data processing: convolution (TO BE COMPLETED BY STUDENTS)
############################################################################
# OUTPUT PARAMETERS--------------------------------------------------------
# y: output signal as convolution of input signal x and impulse response h

# Write the code including comments to explain what you are doing

    #flip x and h if h is bigger
    if (len(x)<len(h)):
        x, h = h, x

    len_x = len(x) # length of x
    len_h = len(h) # length of h




    ###########################    

    #add x amount of zeros to h
    numXZeros = 0
    for a in range(0, len_h):
        numXZeros = numXZeros + 1
    
    temp = np.zeros(len_x+numXZeros)
    for b in range(len_h, len_x+numXZeros):
        temp[b] = x[b-numXZeros]

    len_x = len(x)
    temp3 = np.zeros(len_x+numXZeros)
    for e in range(0, len_x):
        temp3[e] = x[e]
    

    x = temp3 


    ###########################

    #add h amount of zeros to x
    numHZeros = 0
    for c in range(0, len_x):
        numHZeros = numHZeros + 1

    temp2 = np.zeros(len_h+numHZeros)
    for d in range(0, len_h):
        temp2[d] = h[d]
        
    h = temp2 


    ############################

    #re-initalize the lengths of x and h with the added zeros
    len_x = len(x) 
    len_h = len(h)

    #create an empty list to work of of before adding values to why
    tempY = []

    #print statements for testing to make sure everything is working correctly
    print("x: ", x)
    print("h: ", h)
    print("y: ", tempY)
    print()
    print("x-len: ", len_x)
    print("h-len: ", len_h)
    print()


    #dummy variable to measure how many loops the convultion goes through
    count = 0;
    

    print("processing... (can takes several minutes)")

    #Convolution double for loop
    for i in range(0, len_x):
        tempY.insert(i,0)          #add a dummy zero before completing the Convolution
        for j in range(0, len_x):
            if (i-j+1 > 0):
                tempY[i] = tempY[i]+x[j]*h[i-j-1] #Convolution eqution modified to work with loops
                count = count + 1                 #increase count for every loop
                if (count % 10000000 == 0):     
                    print("count:", count)          #show an output every 10000000 ticks
                                                    #as a visual to know your code is working
            else:
                break


    tempY.pop(0)        #convo. for loop creates an unnessiary zero at y[0], this removes it
    y = np.array(tempY) #set y equal to a numpy array
    
    print("Convolution complete, processing sound file...")
    
    
    return y



#myconv([1,2,3],[1,4,5])
