import pandas as pd
import os
import pickle

# LOGIC =
# iterate through keys
# iterate through values
# create a temporary dataframe
# convert index to datetime -> method above
# drop unnecessary columns ['Open', 'High', 'Low', 'Adj Close', 'Volume']
# resample by month .resample('M').mean()
# concatenate dataaframes of etfs for each sector
# export it as sector_i.csv

#FIND CSV FILES IN THE DIRECTORY
directory = 'macro_report/ETFs'
sectored_etfs = {}

for _, filenames in enumerate(os.walk(directory)):
    name = filenames[0].split('/ETFs/')
    if len(name) == 2:
        name = name[1]
        etfs = filenames[2]

        sectored_etfs[name] = etfs


cols_to_drop = ['Open', 'High', 'Low', 'Adj Close', 'Volume']
csv_names = []

#CREATE A DATAFRAME FOR EACH SECTOR
for key in sectored_etfs.keys():
    dfs = []
    for val in sectored_etfs[key]:
        temp_df = pd.read_csv(directory + '/' + key + '/' + val, index_col = 0)
        temp_df.index = pd.DatetimeIndex(temp_df.index) #convert to datetime
        temp_df = temp_df.drop(cols_to_drop, axis=1).resample('M').mean() #resample monthly
        temp_df[val.split('.')[0].strip()] = temp_df['Close']
        temp_df = temp_df.drop('Close', axis = 1)
        dfs.append(temp_df)
    df = pd.concat(dfs, axis = 1)

    print('Dataframe for industry', key, 'is:')
    print(df.head())
    print('\n')
    print('Converting to csv:')
    csv_name = key + '.csv'
    csv_names.append(csv_name)
    df.to_csv('macro_report/ETF_sectors/'+csv_name, sep = ';')

#PICKLE SAVE THE NAME OF THE SECTORS. IT MIGHT BE USEFIL LATER
pickle_out = open("csv_etfs_list.pickle","wb")
pickle.dump(csv_names, pickle_out)
