import pandas as pd
import random
import numpy as np

df_user = pd.read_excel("Experience.xlsx")
df_list = pd.read_excel("emmy.xlsx")

df_user = df_user.iloc[:, [4]]
df_list = df_list.iloc[:, [0]]

mat_user = df_user.as_matrix()
mat_list = df_list.as_matrix()

#print(mat_list)

a = []

for x in range(len(mat_user)):
	#number of amenities for each listing
	y = random.sample(range(1,6),1) 
	#tuple of y elements from range of list
	b = random.sample(range(0,len(mat_list)), y[0])
	for z in range(len(b)):
		a.append((mat_user[x], mat_list[b[z]]))
		
		
a = np.array(a)
a = np.matrix(a)
a = pd.DataFrame(a)

filename = "Amenities_Provided_dummy.xlsx"
a.to_excel(filename, index=False)

