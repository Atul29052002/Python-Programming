# Problem statement  Find the casualty in the Red Corridor States ? Mainly Red corridor states include Jharkhand, Odisha, Andhra Pradesh, and Chhattisgarh.
# Note: Casualty=Killed +Wounded

# Print count of Casualty as integer value. Output Format : Count

import numpy as np 
import csv

file_obj = open("terrorismData.csv")
data = csv.DictReader(file_obj, skipinitialspace = True)

killed = []
wounded = []
state = []

for row in data:
    killed.append(row['Killed'])
    wounded.append(row['Wounded'])
    state.append(row['State'])

np_killed = np.array(killed)
np_killed[np_killed == ''] = '0.0'

np_wounded = np.array(wounded)
np_wounded[np_wounded == ''] = '0.0'

np_state = np.array(state)

np_killed = np.array(np_killed, dtype = float)
np_wounded = np.array(np_wounded, dtype = float)
np_state = np.array(state, dtype=str)


bool_arr =((np_state == 'Jharkhand') | (np_state == 'Odisha') | (np_state == 'Andhra Pradesh') | (np_state == 'Chhattisgarh') )

Casualty = np_killed[bool_arr] + np_wounded[bool_arr]


print(int(np.sum(Casualty)))
