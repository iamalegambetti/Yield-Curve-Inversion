import pandas as pd
import numpy as np
import os

project_path = 'Yield_curve_data'

#LOAD DATA
fed_funds = pd.read_csv(os.path.join(project_path ,'Monthly.csv'), index_col=0) #this is Monthly
spread_10y_2y = pd.read_csv(os.path.join(project_path, 'Daily.csv'), index_col=0) #this is Daily

# CONVERT INDEX INTO DATETIME INDEX TO PERFORM DATETIME OPERATIONS
dfs = [fed_funds, spread_10y_2y]
for df in dfs:
    df.index = pd.DatetimeIndex(df.index)

#METHOD: Convert first object to numbers
def convert_to_float(x):
    if x == '.':
        x = np.nan
    if not isinstance(x, int):
        x = float(x)
    return x

#CONVERT
spread_10y_2y['T10Y2Y'] = spread_10y_2y['T10Y2Y'].apply(lambda x: convert_to_float(x))
fed_funds['FEDFUNDS'] = fed_funds['FEDFUNDS'].apply(lambda x: convert_to_float(x))

#RESAMPLE TO MONTHLY DATA 
spread_10y_2y = spread_10y_2y.resample('M').mean()
fed_funds = fed_funds.resample('M').mean()


#FINAL DF -> Export to CSV
df = pd.concat([spread_10y_2y, fed_funds], axis = 1)
df.to_csv('yield_curve_data.csv', sep = ';')
