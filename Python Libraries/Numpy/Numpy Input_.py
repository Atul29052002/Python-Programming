# Problem statement Given a 2D integer array size (4, 5) with name input_?
# Output Format :
#element1 element2 element3 . . .
#element1 element2 element3 . . .
#element1 element2 element3 . . .
#element1 element2 element3 . . .


import numpy as np
input_=np.arange(1,21,1)
input_=input_.reshape(4,5)

print(*input_[2,0:3])
print(*input_[1:4,3])
print(*input_[2:4,0:5].flatten())
print(*input_[1:3,1:3].flatten())
