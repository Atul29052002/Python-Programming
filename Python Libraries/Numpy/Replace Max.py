# Problem Statemnt: Given an integer array of size 9 and replace the first occurrence of maximum value by 0?
# Note: Generate the following array
# array([11, 2, 13, 4, 15, 6, 27, 8, 19]) Print the Numpy array.
# Output Format :
              # firstElement
              # secondElement   
              # ... 


import numpy as np 

a = np.array([11, 2, 13, 4, 15, 6, 27, 8, 19])

a[a.argmax()] = 0

for i in a:
    print(i)
