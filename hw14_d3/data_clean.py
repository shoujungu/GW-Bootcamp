import pandas as pd

acs='ACS_14_1YR_B02001_with_ann.csv'
brfss='BRFSS_2014_Overall.csv'

#clean acs
df_acs=pd.read_csv(acs,header=0).loc[:,['GEO.display-label','HD01_VD01','HD01_VD02','HD01_VD05']]
df_acs['white_alone_ratio']=df_acs['HD01_VD02']/df_acs['HD01_VD01']
df_acs['asian_alone_ratio']=df_acs['HD01_VD05']/df_acs['HD01_VD01']

df_brf=pd.read_csv(brfss).loc[:,['Locationabbr','Locationdesc','Topic','Question','Response','Data_value']]
df_brf_dep=df_brf.loc[(df_brf['Topic']=='Depression')&(df_brf['Response']=='Yes'),['Locationabbr','Locationdesc','Response','Data_value']]

df=df_acs.merge(df_brf_dep, how='inner', left_on='GEO.display-label', right_on='Locationdesc')
df=df.loc[:,['Locationabbr','GEO.display-label','asian_alone_ratio','white_alone_ratio','Data_value']]
df.rename(columns={'Locationabbr':'abbr','GEO.display-label':'state','asian_alone_ratio':'asian_ratio','white_alone_ratio':'white_ratio','Data_value':'depression'}, inplace=True)
df['asian_ratio']=round(df['asian_ratio']*100,2)
df['white_ratio']=round(df['white_ratio']*100,2)

#add more data
def add_data(df,str):
    df_brf_dia=df_brf.loc[(df_brf['Topic']==str)&(df_brf['Response']=='Yes'),['Locationabbr','Data_value']]\
    .rename(columns={'Locationabbr':'abbr','Data_value':str.lower()})
    df=df.merge(df_brf_dia, how='inner', on='abbr')
    return df

df=add_data(df,'Diabetes')
df=add_data(df,'Arthritis')


df.to_csv('data.csv', index=False)

#print(df)
