import pandas as pd
import random
import numpy as np

a = random.sample(range(1,201), 200)
a = np.array(a)

b = a[0:100]
c = a[100:201]

b = pd.DataFrame(b)
c = pd.DataFrame(c)

filename = "kuch.xlsx"
b.to_excel(filename, index = False)

c.to_excel("kuch1.xlsx", index=False)

#filename = "kuch.xlsx"
#a.to_excel(filename, index= False)

