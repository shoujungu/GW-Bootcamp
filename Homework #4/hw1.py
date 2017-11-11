import pandas as pd

input_1='/home/shoujun/Desktop/purchase_data.json'
#input_2='/home/shoujun/Desktop/purchase_data2.json'

df=pd.read_json(input_1)
#df2=pd.read_json(input_2)
#df=pd.concat([df1,df2])

#Player Count

df_player=df[['Age', 'Gender', 'SN']].drop_duplicates()
player_number=df_player.shape[0]

#Purchasing Analysis (Total)

uniq_items=len(df['Item Name'].unique())

avg_price=df['Price'].mean()

total_purchase=df.shape[0]

total_rev=df['Price'].sum()

#Gender Demographics

df_gender=df_player.groupby('Gender').count()

male_count=df_gender.loc['Male','SN']
male_percent=male_count/player_number

female_count=df_gender.loc['Female','SN']
female_percent=female_count/player_number

other_count=df_gender.loc['Other / Non-Disclosed','SN']
other_percent=other_count/player_number

#Purchasing Analysis (Gender)

df_g_analysis=df[['Gender', 'SN', 'Price']].copy()
df_g_analysis['Average Purchase Price']=df_g_analysis['Price']
df_g_purchase=df_g_analysis.groupby('Gender').agg({'SN': 'count', 'Price': 'sum',
                                                 'Average Purchase Price': 'mean'})                    
df_g_purchase['Normalized Totals']=df_g_purchase['Price']/total_rev
df_g_purchase.reset_index().set_index('Gender')

df_g_purchase['Purchase Count']=df_g_purchase['SN']
df_g_purchase['Total Purchase Value']=df_g_purchase['Price']
df_g_purchase=df_g_purchase[['Purchase Count', 'Average Purchase Price',
                         'Total Purchase Value', 'Normalized Totals']]

#Age Demographics

df_a_analysis=df[['Age', 'Price']].copy()
max_age=df_a_analysis['Age'].max()
bins = [0]+list(range(9, max_age+4))[::5]
df_a_analysis['Age Group'] = pd.cut(df_a_analysis['Age'], bins)

df_a_analysis['Average Purchase Price']=df_a_analysis['Price']

df_a_purchase=df_a_analysis.groupby('Age Group').agg({'Age': 'count', 'Price': 'sum',
                                                 'Average Purchase Price': 'mean'})                    
df_a_purchase['Normalized Totals']=df_a_purchase['Price']/total_rev
df_a_purchase.reset_index().set_index('Age Group')

df_a_purchase['Purchase Count']=df_a_purchase['Age']
df_a_purchase['Total Purchase Value']=df_a_purchase['Price']

df_a_purchase=df_a_purchase[['Purchase Count', 'Average Purchase Price',
                         'Total Purchase Value', 'Normalized Totals']]

#Top Spenders

df_spender=df[['Age','Gender','SN','Price']].copy()
    
df_spender['player']=df_spender['Age'].astype(str)+df['Gender']+'-'+df['SN']

df_spender['Average Purchase Price']=df_spender['Price']

df_spender=df_spender.groupby('player').agg({'Age': 'count','Average Purchase Price':'mean',
                                             'Price':'sum'})

df_spender['Purchase Count']=df_spender['Age']
df_spender['Total Purchase Value']=df_spender['Price']
df_spender.reset_index().set_index('player')
df_spender=df_spender[['Purchase Count','Average Purchase Price','Total Purchase Value']].\
            sort_values('Total Purchase Value', ascending=False)

df_spender['SN']=df_spender.index.str.split('-').str[1]

df_spender_top5=df_spender.head(5)

#Most Popular Items

df_item=df[['Item ID', 'Item Name',  'Price', 'SN']].copy()
df_item['Item']=df_item['Item ID'].astype(str)+'-'+\
                      df_item['Item Name']+'-'+\
                      df_item['Price'].astype(str)

df_item=df_item.groupby('Item').agg({'SN': 'count', 'Price':'sum'})

df_pop_item=df_item.sort_values('SN', ascending=False).reset_index()

df_pop_item['Total Purchase Value']=df_pop_item['Price']
df_pop_item['Purchase Count']=df_pop_item['SN']
df_pop_item['Item ID']=df_pop_item['Item'].str.split('-').str[0]
df_pop_item['Item Name']=df_pop_item['Item'].str.split('-').str[1]
df_pop_item['Item Price']=df_pop_item['Item'].str.split('-').str[2]

df_pop_item=df_pop_item[['Item ID', 'Item Name', 'Purchase Count', 'Item Price',
                 'Total Purchase Value']].head(5)

#Most Profitable Items

df_pro_item=df_pop_item.sort_values('Total Purchase Value',ascending=False).head(5)

print(df_pro_item)
