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

df=pd.read_csv('/Users/B.Suryanarayanan/Documents/Git/Ice_Stupa_Analysis/analysis/data/processed/merged.csv', sep='\t')
df['Date']=pd.to_datetime(df['Date'])
plt.scatter(df.index, df['Tm'])
plt.show()
