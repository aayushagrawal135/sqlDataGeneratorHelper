#does excel related jobs
import pandas as pd

#excel related stuff
import xlrd as xl

import dbsupport

#Load data
#tr = pd.read_csv('sample.csv')   ## path name
tr = pd.read_excel("Listing.xlsx")
data = tr.as_matrix()

r = len(data)
c = len(data[0])



#-----------------------------------------------------------------------
# k <= r : number of random rows you want 
k = 70
#column indices to be selected
cols = [0] 

dbsupport.func(r, c, k, cols, data)

#------------------------------------------------------------------------

