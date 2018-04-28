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

df=pd.read_csv('/Users/B.Suryanarayanan/Documents/Git/Ice_Stupa_Analysis/analysis/data/processed/data_2.csv',encoding='latin-1', sep='\t')
dfs=pd.read_csv('/Users/B.Suryanarayanan/Documents/Git/Ice_Stupa_Analysis/analysis/data/processed/data_1.csv',encoding='latin-1', sep='\t')
df['Date'],dfs['Date']=pd.to_datetime(df['Date']),pd.to_datetime(dfs['Date'])
df.index,dfs.index = df['Date'], dfs['Date']
del df['Date'],dfs['Date']
dfo=pd.concat([df, dfs], axis=0)
dfo=dfo.drop_duplicates(subset=['Tm'], keep='first')
del dfo['Unnamed: 0']
dfo=dfo.sort_index()
dfo.to_csv('/Users/B.Suryanarayanan/Documents/Git/Ice_Stupa_Analysis/analysis/data/processed/merged.csv',sep='\t')
