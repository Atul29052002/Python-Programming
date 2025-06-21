# Problem statement Given an integer array of size 10. Print the index of elements which are multiple of 3.
# Note: Generate the following array
# array([ 1,  3,  5,  7,  9, 11, 13, 15, 17, 19]) Print the index of elements.
# Output Format : index1 index2 index3 ... 


import numpy as np

a = np.array([1,  3,  5,  7,  9, 11, 13, 15, 17, 19])

index = np.where((a%3 == 0))[0]

print(*index)
