Problem Statement :

As we knew the Kargil ( in Jammu and Kashmir) War that took place between May 1999 and July 1999 (3 Months) ,so there was a huge conflict in Kashmir Valley during this period.

In this dataset, there is no information regarding the war between the two countries to find out the casualty during the war.

So find out the attack in this period in which maximum casualties happened.

Print the count of casualties (as integer), city in which that attack happened and name of attack group.

Note : Casualty = Killed + Wounded.Fill the empty value in killed or wounded feature to 0.
Output Format :

Casualty City TerroristGroup


## Open and read data file as specified in the question
## Print the required output in given format
import numpy as np 
import csv

file_obj = open("terrorismData.csv")
data = csv.DictReader(file_obj, skipinitialspace = True)

month = []
year = []
killed = []
wounded = []
city = []
group = []
state = []

for row in data:
    month.append(row['Month'])
    year.append(row['Year'])
    killed.append(row['Killed'])
    wounded.append(row['Wounded'])
    city.append(row['City'])
    group.append(row['Group'])
    state.append(row['State'])


np_month = np.array(month)
np_month[np_month == ''] = '0.0'
np_year = np.array(year)
np_year[np_year == ''] = '0.0'
np_killed = np.array(killed)
np_killed[np_killed == ''] = '0.0'
np_wounded = np.array(wounded)
np_wounded[np_wounded == ''] = '0.0'
np_city = np.array(city)
np_group = np.array(group)
np_state = np.array(state)

np_month = np.array(np_month, dtype = float)
np_year = np.array(np_year, dtype = float)
np_killed = np.array(np_killed, dtype = float)
np_wounded = np.array(np_wounded, dtype = float)
np_state = np.array(state, dtype=str)


bool_arr = (((np_month >= 5 ) & (np_month <= 7)) & ((np_year == 1999)) & (np_state == 'Jammu and Kashmir'))

Casualty = np_killed + np_wounded

filtered_casualty = Casualty[bool_arr]
filtered_city = np_city[bool_arr]
filtered_group = np_group[bool_arr]

max_index = np.argmax(filtered_casualty)

print(f"{int(filtered_casualty[max_index])} {filtered_city[max_index]} {filtered_group[max_index]}")
