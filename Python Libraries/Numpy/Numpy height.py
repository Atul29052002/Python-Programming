# Given age and height of 20 students in two different numpy arrays with name age and height (in cms). Print the age of those students whose height is above 155 cm.
# Print the Numpy array. Output Format :
# age1 height1 
# age2 height2 
# ... 

import numpy as np 

age=np.array([15,17,19,20,14,21,16,19,13,20,22,23,21,16,18,19,20,15,17,18])
height=np.array([156,144,180,162,152,157,154,155,151,150,158,179,126,182,183,154,159,160,172,149])

index = np.where(height  > 155)

for a , b in zip(age[index],height[index]):
    print(a,b)
