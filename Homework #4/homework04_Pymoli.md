## **Heroes Of Pymoli Data Analysis**
* OBSERVED TREND 1  
  The majority players are male (81.15%).

* OBSERVED TREND 2  
  The majority players are within 20-24 years old (45.2%).

* OBSERVED TREND 3  
  The average purchase counts in male and female are very close.


```python
import pandas as pd

input_file=r'/home/shoujun/Desktop/bootcamp/GW-Bootcamp/Homework #4/purchase_data.json'
df=pd.read_json(input_file)
```


```python
#Player Count

player_number=df[['Age', 'Gender', 'SN']].drop_duplicates().shape[0]
df_PC=pd.DataFrame({'Total Players':[player_number]})
df_PC
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>573</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Number of Unique Items</th>
      <th>Average Price</th>
      <th>Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>183</td>
      <td>$2.93</td>
      <td>780</td>
      <td>$2286.33</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Gender Demographics

df_GD=df[['Age', 'Gender', 'SN']].drop_duplicates().groupby('Gender').count()
df_GD['Total Count']=df_GD['SN']
df_GD['Percentage of Players']=(df_GD['SN']/player_number*100).round(2)
df_GD=df_GD.reset_index()
df_GD=df_GD[['Gender','Percentage of Players', 'Total Count']].set_index('Gender')

df_GD
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>17.45</td>
      <td>100</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>81.15</td>
      <td>465</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>1.40</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Purchasing Analysis (Gender)

df_PAG=df[['Gender','SN','Price']].copy()
df_PAG['Purchase Count']=df_PAG['SN']
df_PAG['Average Purchase Price']=df_PAG['Price']
df_PAG['Total Purchase Value']=df_PAG['Price']

df_PAG=df_PAG.groupby('Gender').agg({'Purchase Count':'count',
                                     'Average Purchase Price':'mean',
                                     'Total Purchase Value':'sum'})
df_PAG['Normalized Totals']=df_PAG['Total Purchase Value']/df_PAG['Purchase Count']

df_PAG['Average Purchase Price']='$'+df_PAG['Average Purchase Price'].\
                                  round(2).astype(str)
df_PAG['Total Purchase Value']='$'+df_PAG['Total Purchase Value'].\
                                  round(2).astype(str)
df_PAG['Normalized Totals']='$'+df_PAG['Normalized Totals'].\
                                  round(2).astype(str)
df_PAG=df_PAG[['Purchase Count','Average Purchase Price',
               'Total Purchase Value','Normalized Totals']]

df_PAG
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>136</td>
      <td>$2.82</td>
      <td>$382.91</td>
      <td>$2.82</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>633</td>
      <td>$2.95</td>
      <td>$1867.68</td>
      <td>$2.95</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
      <td>$3.25</td>
      <td>$35.74</td>
      <td>$3.25</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0&lt;10</th>
      <td>3.32</td>
      <td>19</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>4.01</td>
      <td>23</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>17.45</td>
      <td>100</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>45.20</td>
      <td>259</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>15.18</td>
      <td>87</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>8.20</td>
      <td>47</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>4.71</td>
      <td>27</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>1.92</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0&lt;10</th>
      <td>28</td>
      <td>$2.98</td>
      <td>$83.46</td>
      <td>$2.98</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>35</td>
      <td>$2.77</td>
      <td>$96.95</td>
      <td>$2.77</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>133</td>
      <td>$2.91</td>
      <td>$386.42</td>
      <td>$2.91</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>336</td>
      <td>$2.91</td>
      <td>$978.77</td>
      <td>$2.91</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>125</td>
      <td>$2.96</td>
      <td>$370.33</td>
      <td>$2.96</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>64</td>
      <td>$3.08</td>
      <td>$197.25</td>
      <td>$3.08</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>42</td>
      <td>$2.84</td>
      <td>$119.4</td>
      <td>$2.84</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>17</td>
      <td>$3.16</td>
      <td>$53.75</td>
      <td>$3.16</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Price</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>5</td>
      <td>$3.41</td>
      <td>$17.06</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>4</td>
      <td>$3.39</td>
      <td>$13.56</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>4</td>
      <td>$3.18</td>
      <td>$12.74</td>
    </tr>
    <tr>
      <th>Haellysu29</th>
      <td>3</td>
      <td>$4.24</td>
      <td>$12.73</td>
    </tr>
    <tr>
      <th>Eoda93</th>
      <td>3</td>
      <td>$3.86</td>
      <td>$11.58</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Most Popular Items

_df_MPI=df[['Item ID', 'Item Name',  'Price']].copy()
_df_MPI['Item']=_df_MPI['Item ID'].astype(str)+'-'+\
                      _df_MPI['Item Name']+'-'+\
                      _df_MPI['Price'].astype(str)

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
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <th>Betrayal, Whisper of Grieving Widows</th>
      <td>11</td>
      <td>$2.35</td>
      <td>$25.85</td>
    </tr>
    <tr>
      <th>84</th>
      <th>Arcane Gem</th>
      <td>11</td>
      <td>$2.23</td>
      <td>$24.53</td>
    </tr>
    <tr>
      <th>13</th>
      <th>Serenity</th>
      <td>9</td>
      <td>$1.49</td>
      <td>$13.41</td>
    </tr>
    <tr>
      <th>31</th>
      <th>Trickster</th>
      <td>9</td>
      <td>$2.07</td>
      <td>$18.63</td>
    </tr>
    <tr>
      <th>34</th>
      <th>Retribution Axe</th>
      <td>9</td>
      <td>$4.14</td>
      <td>$37.26</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Most Profitable Items

df_MProI=_df_MPI.sort_values('Total Purchase Value', ascending=False).head(5)
df_MProI['Total Purchase Value']='$'+df_MProI['Total Purchase Value'].round(2).astype(str)

df_MProI
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <th>Retribution Axe</th>
      <td>9</td>
      <td>$4.14</td>
      <td>$37.26</td>
    </tr>
    <tr>
      <th>115</th>
      <th>Spectral Diamond Doomblade</th>
      <td>7</td>
      <td>$4.25</td>
      <td>$29.75</td>
    </tr>
    <tr>
      <th>32</th>
      <th>Orenmir</th>
      <td>6</td>
      <td>$4.95</td>
      <td>$29.7</td>
    </tr>
    <tr>
      <th>103</th>
      <th>Singed Scalpel</th>
      <td>6</td>
      <td>$4.87</td>
      <td>$29.22</td>
    </tr>
    <tr>
      <th>107</th>
      <th>Splitter, Foe Of Subtlety</th>
      <td>8</td>
      <td>$3.61</td>
      <td>$28.88</td>
    </tr>
  </tbody>
</table>
</div>
