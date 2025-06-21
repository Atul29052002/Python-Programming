# Problem statement Find indices of non-zero elements from the array [1,2,0,0,4,0] ? Print the index of non-zero elements.
# Output Format : index1 index2 index3 ... 


import numpy as np

a = np.array([1, 2, 0, 0, 4, 0])

indices = np.where(a != 0)[0]

# Print indices without brackets

print(*indices)
