import numpy as np
import pandas as pd
import os.path
import subprocess
import math
import datetime
import matplotlib
import os.path
from copy import copy, deepcopy
from matplotlib import pyplot as plt
from datetime import datetime, timedelta

df=pd.read_csv('/Users/B.Suryanarayanan/Documents/Git/Ice_Stupa_Analysis/analysis/data/raw/Ice_Stupa_Base.csv',encoding='latin-1', sep=',')
del df['Relative_Humidity']
df['Timestamp']=pd.to_datetime(df['Timestamp'], dayfirst=True)
df['Time'],df['Date']= df['Timestamp'].apply(lambda x:x.time()), df['Timestamp'].apply(lambda x:x.date())
dfs=pd.DataFrame({'Type' : []})
dfs['Date']=pd.to_datetime(df['Date'])
df.index = df['Timestamp']
del df['Timestamp']
dfs=dfs.drop_duplicates(subset=['Date'], keep='first')
dfs=dfs.reset_index()
dfs=dfs.drop({'Type','index'}, axis=1)
for i in range(0,dfs.shape[0]):
    dfs.loc[i,'Tm']=df[str(dfs.loc[i,'Date'].date())]['Temperature_Celsius'].mean()
dfs.to_csv('/Users/B.Suryanarayanan/Documents/Git/Ice_Stupa_Analysis/analysis/data/processed/data_2.csv', sep='\t')
plt.scatter(dfs.index, dfs['Tm'])
plt.show()
