# Problem Statement : Find total number of people killed from USA? Note: Some columns of killed are empty so replace them by 0. Print count of Killed as integer value.
# Output Format : TotalKilled

import numpy as np 
import csv

file_obj = open("terrorismData.csv")
data = csv.DictReader(file_obj, skipinitialspace = True)

killed = []
country = []
for row in data:
    killed.append(row['Killed'])
    country.append(row['Country'])


np_killed = np.array(killed)
np_killed[np_killed == ''] = '0.0'

np_killed = np.array(np_killed, dtype = float)
np_country = np.array(country)

bool_arr = np_country == 'United States'
us_killed = np_killed[bool_arr]

print(int(np.sum(us_killed)))
