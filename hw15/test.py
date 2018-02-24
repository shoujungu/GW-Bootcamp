import pandas as pd

sample='BB_941'

filename="belly_button_biodiversity_samples.csv"
df=pd.read_csv(filename)
cols=df.columns.values.tolist()[1:]






print(len(cols))
#print(id)
