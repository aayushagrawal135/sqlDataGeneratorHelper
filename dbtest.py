#does excel related jobs
import pandas as pd

import dbsupport

#Load data
tr = pd.read_csv('sample.csv')   ## path name
data = tr.as_matrix()

r = len(data)
c = len(data[0])

#-----------------------------------------------------------------------
# k <= r : number of random rows you want 
k = 10
#column indices to be selected
cols = [0, 2, 4] 

dbsupport.func(r, c, k, cols, data)

#------------------------------------------------------------------------

