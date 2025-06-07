# Problem statement You are given a rope of length 5m. Cut the rope into 9 parts such that each part is of equal length.
# Note:Array elements are the points where cut is to be made and round upto 2 decimal place.
# Print the array element. Output Format :
# element1 
# element2 
# element3
# .
# .

import numpy as np

a = np.linspace(0,5,10)[1:-1]
a = np.round(a,2)

for val in a:
  print(val)


