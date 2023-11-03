import numpy as np
import pandas as pd

df_csv = pd.read_csv("T1.csv")
print(df_csv)
#print(df_csv.head(3))
#print(df_csv.tail(3))

#_________________________________________________________________________

df2 = df_csv.head()
#print(df2)
df3 = df2.replace({"pm2":{12031.25:np.nan}})
print(df3)
df4 = df3.dropna()
print(df4)