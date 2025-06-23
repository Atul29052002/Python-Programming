# Problem statement Given file "terrorismData.csv"
# It is an open-source database including information on terrorist attacks around the world from 1970 through 2017. This dataset includes systematic data on domestic as well as international terrorist incidents that have occurred during this time period
# Problem Statement : Find value of killed column only where country == ‘United States’? Print 0 in place of missing values. Print count of Killed as integer value.
# Output Format :

# Killed1
# Killed2
# Killed3
# Killed4
# . . .


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

for kills in us_killed:
    print(int(kills))
