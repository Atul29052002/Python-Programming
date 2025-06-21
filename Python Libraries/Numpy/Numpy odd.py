# Problem Statemnt: Given an integer array of size 10. Replace the odd number in numpy array with -1 ?
# Note: Generate the following array
# array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) Print the Numpy array.
# Output Format : firstElement secondElement  ... 


import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9,10])

odd = np.where(a % 2 != 0)

a[odd] = -1

print(*a)
