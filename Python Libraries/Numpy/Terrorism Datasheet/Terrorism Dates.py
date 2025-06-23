# Problem Statement : Find the number of attack held between 1 Jan 2010 and 31 Jan 2010?(including both date).
# Note Ignore the case where day is 0
# Print count of NumberOFAttack as integer value. Output Format : count

import numpy as np 
import csv

file_obj = open("terrorismData.csv")
data = csv.DictReader(file_obj, skipinitialspace = True)

day = []
month = []
year = []

for row in data:
    day.append(row['Day'])
    month.append(row['Month'])
    year.append(row['Year'])


np_day = np.array(day)
np_day[np_day == ''] = '0.0'
np_month = np.array(month)
np_month[np_month == ''] = '0.0'
np_year = np.array(year)
np_year[np_year == ''] = '0.0'

np_day = np.array(np_day, dtype = float)
np_month = np.array(np_month, dtype = float)
np_year = np.array(np_year, dtype = float)

bool_arr = ((np_day >= 1) & (np_day <=31 )) & ((np_month ==1)) & ((np_year == 2010))
Number_of_attack = np.sum(bool_arr)

print(int(Number_of_attack))
