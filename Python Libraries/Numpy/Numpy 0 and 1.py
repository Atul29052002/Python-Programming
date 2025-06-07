# Create an integer array of size 10, where all the values should be 0 but the fifth value should be 1. Print the elements of array.
# Output Format : element1 element2 element3 ... 

import numpy as np

a = np.zeros(10,dtype=int)
a[4]=1
print(*a)

