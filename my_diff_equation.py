## JAMES GALANTE
## JOSH WEINICK

import numpy as np
def my_diffequation(x, alpha, N):

############################################################################
# A function to generate the output signal y of the system described by a
# diffence equation
############################################################################

# INPUT PARAMETERS---------------------------------------------------------
# x: input signal
# alpha: decreasing amplitude
# N: delay between consecutive echoes

############################################################################
# Data processing (TO BE COMPLETED BY STUDENTS)
############################################################################
# OUTPUT PARAMETERS--------------------------------------------------------
# y: output signal

    L=len(x)
    # Write the code including comments to explain what you are doing

    #initialize y
    y = []

    #print statements for testing to make sure everything is working correctly
    print("x: ", x)
    print("a: ", alpha)
    print("N: ", N)
    print("L: ", L)
    

    #create a numpy array of zeros length L
    temp = np.zeros(L)

    #reverebation as a for loop
    for i in range(0,L):
        if (i > N):     #make sure its in range
            temp[i] = x[i] + alpha*temp[i-N]   #reverberation equation
                                               #modified for a loop


    #set y to temp
    y = temp    

    return y
