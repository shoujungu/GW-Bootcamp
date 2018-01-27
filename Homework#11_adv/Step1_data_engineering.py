import pandas as pd

#read data to df
df_m=pd.read_csv('hawaii_measurements.csv')
df_s=pd.read_csv('hawaii_stations.csv')

#check null value
dfs=[df_m,df_s]
for df in dfs:
    print(pd.isnull(df).sum())
    print('\n')

#clean the data
output_label=['clean_hawaii_measurements.csv','clean_hawaii_stations.csv']
for i in range(2):
    dfs[i].fillna(0).to_csv(output_label[i],index=False)


    




