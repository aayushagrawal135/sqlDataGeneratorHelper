import pandas as pd
import random 
import numpy as np 

#Avails will be made in samplex
df = pd.read_excel("samplex.xlsx")
data = df.as_matrix()
data = data[:, 1]

df_home = pd.read_excel("Home.xlsx")
df_home = df_home.iloc[:,[6,5]]
mat_home = df_home.as_matrix()

df_exp = pd.read_excel("Experience.xlsx")
df_exp = df_exp.iloc[:,[4,2]]
mat_exp = df_exp.as_matrix()

mat = np.concatenate((mat_home, mat_exp))

a = []

for x in range(len(data)):
	y = data[x]
	for z in range(len(mat)):
		if mat[z][0] == y : 
			a.append(mat[z][1])
			break

a = np.array(a)
a = pd.DataFrame(a)

filename = "kuch.xlsx"
a.to_excel(filename, index=False)	

'''
#host_ids = df.columns['Host_ID']
data = (df.loc[:,""]).as_matrix()
random.sample(range(1,))
'''

'''
a = []
for x in range(200):
	y = random.choice(data)
	a.append(y)

a = np.array(a) 
a = np.transpose(a)
df1 = pd.DataFrame(a)
fil = "samplex1.xlsx"
df1.to_excel(fil, index=False)

print(a)
'''
