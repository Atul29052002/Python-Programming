# Problem Statemnt: In a given 1D array, convert all elements that fall between 3 and 8 (both inclusive) to negative numbers.
# Note: Generate the following array
# array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) Print the Numpy array.
# Output Format :
    #firstElement 
    #secondElement  
    # ... 

import numpy as np 

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

a[(a>=3) & (a<=8)] *= -1

for i in a:
    print(i)
