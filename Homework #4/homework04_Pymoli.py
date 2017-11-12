
# coding: utf-8

# In[99]:


import pandas as pd

input_file=r'/home/shoujun/Desktop/bootcamp/GW-Bootcamp/Homework #4/purchase_data.json'
df=pd.read_json(input_file)


# In[100]:


#Player Count

player_number=df[['Age', 'Gender', 'SN']].drop_duplicates().shape[0]
df_PC=pd.DataFrame({'Total Players':[player_number]})
df_PC


# In[101]:


#Purchasing Analysis (Total)

df_item=df[['Item ID', 'Item Name',  'Price']].copy()

uniq_items=df_item.drop_duplicates().shape[0]

avg_price=df['Price'].mean()
avg_price='${:.2f}'.format(avg_price)

total_purchase=df.shape[0]

total_rev=df['Price'].sum()
total_rev='${:.2f}'.format(total_rev)

df_PAT=pd.DataFrame({'Number of Unique Items':[uniq_items],
                     'Average Price': [avg_price],
                     'Number of Purchases': [total_purchase],
                     'Total Revenue': [total_rev]})

df_PAT=df_PAT[['Number of Unique Items','Average Price',
               'Number of Purchases','Total Revenue']]

df_PAT


# In[102]:


#Gender Demographics

df_GD=df[['Age', 'Gender', 'SN']].drop_duplicates().groupby('Gender').count()
df_GD['Total Count']=df_GD['SN']
df_GD['Percentage of Players']=(df_GD['SN']/player_number*100).round(2)
df_GD=df_GD.reset_index()
df_GD=df_GD[['Gender','Percentage of Players', 'Total Count']].set_index('Gender')

df_GD


# In[103]:


#Purchasing Analysis (Gender)

df_PAG=df[['Gender','SN','Price']].copy()
df_PAG['Purchase Count']=df_PAG['SN']
df_PAG['Average Purchase Price']=df_PAG['Price']
df_PAG['Total Purchase Value']=df_PAG['Price']

df_PAG=df_PAG.groupby('Gender').agg({'Purchase Count':'count',
                                     'Average Purchase Price':'mean',
                                     'Total Purchase Value':'sum'})
df_PAG['Normalized Totals']=df_PAG['Total Purchase Value']/df_PAG['Purchase Count']

df_PAG['Average Purchase Price']='$'+df_PAG['Average Purchase Price'].                                  round(2).astype(str)
df_PAG['Total Purchase Value']='$'+df_PAG['Total Purchase Value'].                                  round(2).astype(str)
df_PAG['Normalized Totals']='$'+df_PAG['Normalized Totals'].                                  round(2).astype(str)
df_PAG=df_PAG[['Purchase Count','Average Purchase Price',
               'Total Purchase Value','Normalized Totals']]

df_PAG


# In[104]:


#Age Demographics

bins = [0,9,14,19,24,29,34,39,100]
labels=['0<10', '10-14','15-19','20-24','25-29','30-34','35-39','40+']

df_AD=df[['Age', 'Gender', 'SN']].copy().drop_duplicates()
df_AD['Age Group']=pd.cut(df_AD['Age'], bins, labels=labels)
df_AD['Total Count']=df_AD['SN']
df_AD=df_AD.groupby('Age Group').agg({'Total Count':'count'})
df_AD['Percentage of Players']=(df_AD['Total Count']/player_number*100).round(2)
df_AD=df_AD[['Percentage of Players','Total Count']]
del df_AD.index.name

df_AD


# In[105]:


#Purchasing Analysis (Age)

df_PAA=df[['Age', 'Price']].copy()
df_PAA['Age Group']=pd.cut(df_PAA['Age'], bins, labels=labels)

df_PAA['Purchase Count']=df_PAA['Age']
df_PAA['Average Purchase Price']=df_PAA['Price']
df_PAA['Total Purchase Value']=df_PAA['Price']

df_PAA=df_PAA.groupby('Age Group').agg({'Purchase Count':'count',
                                      'Average Purchase Price':'mean',
                                      'Total Purchase Value':'sum'})
df_PAA['Normalized Totals']=df_PAA['Total Purchase Value']/df_PAA['Purchase Count']

df_PAA['Average Purchase Price']='$'+df_PAA['Average Purchase Price'].round(2).astype(str)
df_PAA['Total Purchase Value']='$'+df_PAA['Total Purchase Value'].round(2).astype(str)
df_PAA['Normalized Totals']='$'+df_PAA['Normalized Totals'].round(2).astype(str)
df_PAA=df_PAA[['Purchase Count','Average Purchase Price',
               'Total Purchase Value','Normalized Totals']]
del df_PAA.index.name

df_PAA


# In[106]:


#Top Spenders

df_TS=df[['Age','Gender','SN','Price']].copy()
    
df_TS['player']=df_TS['Age'].astype(str)+df_TS['Gender']+'-'+df_TS['SN']
df_TS['Purchase Count']=df_TS['SN']
df_TS['Average Purchase Price']=df_TS['Price']
df_TS['Total Purchase Price']=df_TS['Price']

df_TS=df_TS.groupby('player').agg({'Purchase Count': 'count',
                                   'Average Purchase Price':'mean',
                                    'Total Purchase Price':'sum'})
df_TS=df_TS.sort_values('Total Purchase Price', ascending=False).head(5)
df_TS['SN']=df_TS.index.str.split('-').str[1]
df_TS['Average Purchase Price']='$'+df_TS['Average Purchase Price'].round(2).astype(str)
df_TS['Total Purchase Price']='$'+df_TS['Total Purchase Price'].round(2).astype(str)
df_TS=df_TS.reset_index()[['SN','Purchase Count','Average Purchase Price',
                           'Total Purchase Price']].set_index('SN')

df_TS


# In[107]:


#Most Popular Items

_df_MPI=df[['Item ID', 'Item Name',  'Price']].copy()
_df_MPI['Item']=_df_MPI['Item ID'].astype(str)+'-'+                      _df_MPI['Item Name']+'-'+                      _df_MPI['Price'].astype(str)

_df_MPI['Purchase Count']=_df_MPI['Price']
_df_MPI['Total Purchase Value']=_df_MPI['Price']
       
_df_MPI=_df_MPI.groupby('Item').agg({'Purchase Count': 'count',
                                   'Total Purchase Value':'sum'})

_df_MPI.reset_index(inplace=True)
_df_MPI['Item ID']=_df_MPI['Item'].str.split('-').str[0]
_df_MPI['Item Name']=_df_MPI['Item'].str.split('-').str[1]
_df_MPI['Item Price']='$'+_df_MPI['Item'].str.split('-').str[2]
_df_MPI.set_index(['Item ID', 'Item Name'], inplace=True)
_df_MPI=_df_MPI[['Purchase Count','Item Price','Total Purchase Value']]

df_MPI=_df_MPI.sort_values('Purchase Count', ascending=False).head(5)
df_MPI['Total Purchase Value']='$'+df_MPI['Total Purchase Value'].round(2).astype(str)

df_MPI


# In[108]:


#Most Profitable Items

df_MProI=_df_MPI.sort_values('Total Purchase Value', ascending=False).head(5)
df_MProI['Total Purchase Value']='$'+df_MProI['Total Purchase Value'].round(2).astype(str)

df_MProI

