#does excel related jobs
import pandas as pd

#does random number related job
import random

#does array related stuff
import numpy as np

#Load data
tr = pd.read_csv('sample.csv')   ## path name
data = tr.as_matrix()

r = len(data)
c = len(data[0])

# k <= r : generates k random numbers within a range 1,r 
k = 5
#column indices to be selected
cols = [0, 2, 4] 

setOfRandomRowNum = random.sample(range(1, r), k)

#this will keep all columns of seected rows    - (1)
up_data = [];

for x in range(len(setOfRandomRowNum)):
	up_data.append(data[setOfRandomRowNum[x],:])

up_data = np.array(up_data)

#this will select columns from (1)
upp_data = []

for x in range(len(cols)):
	upp_data.append(up_data[:,cols[x]])

upp_data = np.array(upp_data)
upp_data = np.transpose(upp_data)

#store this somewhere

## convert your array into a dataframe
df = pd.DataFrame(upp_data)
# save to xlsx file, if file doesnt exist, it will be created, then copied
filepath = "samplex.xlsx"
df.to_excel(filepath, index=False)


