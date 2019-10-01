import pandas as pd
import os

#CONCATENATING ALL THE DATAFRAMES
sector = ['materials', 'financials', 'consumer_disc',
 'energy', 'healthcare', 'utilities', 'telecom',
'consumer_staples', 'industrials', 'tech', 'real_estate']

csv_paths = [element+'.csv' for element in sector]
data_directory = '/Users/alessandrogambetti/Desktop/yield_curve_inversion/ETF_sectors'

dfs = []

for path, sec in zip(csv_paths, sector):
    path = os.path.join(data_directory,path)
    temp_df = pd.read_csv(path, index_col=0, sep = ';')
    columns = temp_df.columns
    for col in columns:
        temp_df[col+'_'+sec] = temp_df[col]
    temp_df.drop(list(columns), axis = 1, inplace = True)

    dfs.append(temp_df)

df = pd.concat(dfs, axis = 1)


#LOADING YIELD CURVE DATA
yield_curve_data = pd.read_csv('yield_curve_data.csv', sep = ';', index_col=0)
df = pd.concat([df, yield_curve_data], axis = 1)
df = df.loc['2000-01-31':]

#METHOD: CHECK IF THE YIELD CURVE IS INVERTED
def inverted(x):
    if x < 0:
        return 1 #yes, it is inverted
    return 0

df['Inverted'] = df['T10Y2Y'].apply(lambda x: inverted(x))

#SELECTING DATAFRAME WITH INVERTED DATAFRAME
rule = df['Inverted'] == 1
df_inv = df[rule]

#SELECTING DATAFRAMES OF 3 AND 4 YEARS PERFORMANCES - ARBITRRY MEASURE
df_2000_inversion = df.loc['2000-12-31':'2003-12-31 ']
df_2007_inversion = df.loc['2007-05-31':'2011-05-31 ']

#EXPORTING DATA IN CURRENT DIRECTORY
df_inv.to_csv('inverted.csv', sep = ';')
df_2000_inversion.to_csv('2000inversion.csv', sep = ';')
df_2007_inversion.to_csv('2007inversion.csv', sep = ';')
df.to_csv('data.csv', sep = ';')
