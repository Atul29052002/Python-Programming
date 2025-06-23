# Problem statement   Find the number of attack held between day 10 and day 20?(ignoring the year and month)(including both day)
# Print count of NumberOFAttack as integer value.
# Output Format : count

import numpy as np 
import csv

file_obj = open("terrorismData.csv")
data = csv.DictReader(file_obj, skipinitialspace = True)

day = []
for row in data:
    day.append(row['Day'])


np_day = np.array(day)
np_day[np_day == ''] = '0.0'

np_day = np.array(np_day, dtype = float)

bool_arr = (np_day >= 10) & (np_day <=20 )
Number_of_attack = np.sum(bool_arr)

print(int(Number_of_attack))
