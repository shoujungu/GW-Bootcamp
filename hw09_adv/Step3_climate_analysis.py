import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sqlalchemy as sa
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

Base = automap_base()

engine = sa.create_engine("sqlite:///hawaii.sqlite", echo=False)
Base.prepare(engine, reflect=True)


# Precipitation Analysis
Mea = Base.classes.measurement
session = Session(bind=engine)

prcp=[]
date_index=[]

for row in session.query(Mea.date, Mea.prcp).filter(Mea.date>'2016-12-31').all():
    date_index.append(row[0])
    prcp.append(row[1])

df_prcp=pd.DataFrame({'prcp':prcp},index=date_index)


plt.style.use('seaborn')
fig,ax=plt.subplots(figsize=(10,8))

ax.bar(df_prcp.index,df_prcp['prcp'],label='Precipitation')
ax.set_xlabel('date')
plt.xticks(rotation=45)
plt.legend()

plt.savefig('prcp.png')
plt.clf()

print(df_prcp.describe())


# Station Analysis
Sta=Base.classes.station
total_stations=session.query(sa.func.count(Sta.station)).all()[0][0]

most_active_station=session.query(Mea.station,sa.func.count(Mea.station)).\
                     group_by(Mea.station).\
                     order_by(sa.func.count(Mea.station).desc()).\
                     all()[0][0]

station=[]
date_index=[]
tobs=[]
for row in session.query(Mea.date, Mea.station, Mea.tobs).filter(Mea.date>'2016-12-31').all():
    date_index.append(row[0])
    station.append(row[1])
    tobs.append(row[2])

df_tob=pd.DataFrame({'station':station,'tobs':tobs},index=date_index)

hno=df_tob.groupby('station').agg({'tobs':'count'})['tobs'].idxmax()
df_tob=df_tob.loc[df_tob['station']==hno,:]

bins=np.linspace(55,95,13)

plt.style.use('seaborn')
fig,ax=plt.subplots(figsize=(10,8))

ax.hist(df_tob['tobs'],bins,label='tobs')
ax.set_xlabel('date')
ax.set_ylabel('Frequency')
plt.legend()

plt.savefig('tobs.png')
plt.clf()


# Temperature Analysis
def calc_temps(start,end):
    date_index=[]
    tobs=[]
    for row in session.query(Mea.date,Mea.tobs).filter((Mea.date>start) & (Mea.date<end)).all():
        date_index.append(row[0])
        tobs.append(row[1])
    df=pd.DataFrame({'tobs':tobs},index=date_index)
    _min=np.min(df['tobs'])
    _max=np.max(df['tobs'])
    avg=np.mean(df['tobs'])   
    return _min,_max,avg

_max,_min,avg=calc_temps('2017-01-01','2018-01-01')

plt.style.use('seaborn')
fig,ax=plt.subplots(figsize=(6,8))

ax.bar([1],avg)
ax.errorbar(1,avg,yerr=[[avg-_min],[_max-avg]],color='black')
ax.xaxis.set_ticklabels([])
ax.set_xlim(0,2)
ax.set_title('Trip Avg Temp')
ax.set_ylabel('Temp (F)')

plt.savefig('temp.png')
plt.clf()


# Optional Recommended Analysis

date_index=[]
station=[]
prcp=[]
tobs=[]

for row in session.query(Mea.date,Mea.station,Mea.prcp,Mea.tobs).all():
    date_index.append(row[0])
    station.append(row[1])
    prcp.append(row[2])
    tobs.append(row[3])

df_opt=pd.DataFrame({'station':station,'prcp':prcp,'tobs':tobs},index=date_index)

#Calcualte the rainfall per weather station using the previous year's matching dates.
def rainfall_per_weather_station(date):
    return df_opt.loc[df_opt.index.astype('str')==date,:]

#Calculate the daily normals
def daily_normals(date):
    df=df_opt.loc[df_opt.index.astype('str').str.contains(date),:]
    _min=np.min(df['tobs'])
    _max=np.max(df['tobs'])
    avg=np.mean(df['tobs'])
    return _min,_max,avg

dates=['01-01','01-02','01-03','01-04','01-05','01-06','01-07']
dates_labels=['min','max','avg']
dates_values=[[],[],[]]

for d in dates:
    nor=daily_normals(d)
    for i in range(3):
        dates_values[i].append(nor[i])

df_dates=pd.DataFrame({dates_labels[i]:dates_values[i] for i in range(3)},index=dates)

plt.style.use('seaborn')
ax = df_dates.plot(kind='area', stacked=False, figsize=(10,10),
                   alpha=0.5)

ax.set_xlabel('date')
ax.legend(loc=3,frameon=True)
ax.set_xticks(np.arange(7))
ax.xaxis.set_ticklabels(['2018-'+i for i in dates])
plt.xticks(rotation=45)

plt.savefig('normals.png')
plt.clf()



