import requests as req
from citipy import citipy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

# generate city name list
lati_bin=np.linspace(-90,90,45)
long_bin=np.linspace(-180,180,45)

city_list=[]
for i in lati_bin:
    for j in long_bin:
        city_list.append(str(citipy.nearest_city(i,j).city_name)+','
                          +str(citipy.nearest_city(i,j).country_code))
city_list=list(set(city_list))


# API request
api_key = "25bc90a1196e6f153eece0bc0b0fc9eb"
url = "http://api.openweathermap.org/data/2.5/weather?"

lat_list=[]
lng_list=[]
tem_list=[]
hum_list=[]
clo_list=[]
win_list=[]
log_list=[]
dat_list=[]
citycountry_list=[]
rec=1
error_count=0

for i in city_list:
    payload={'q':i,'units':'imperial','appid':api_key}
    resp=req.get(url, params=payload)
    response=resp.json()
    if response['cod']==200:
        lat_list.append(response['coord']['lat'])
        lng_list.append(response['coord']['lon'])
        dat_list.append(response['dt'])
        tem_list.append(response['main']['temp_max'])
        hum_list.append(response['main']['humidity'])
        clo_list.append(response['clouds']['all'])
        win_list.append(response['wind']['speed'])
        citycountry_list.append(i)
        text='Processing Record:'+str(rec)+' | '+i+'\n'
        log_list.append(text+resp.url+'\n')
        rec+=1
    else:
        error_count+=1
        
date=datetime.datetime.utcfromtimestamp(dat_list[0]).replace(tzinfo=datetime.timezone.utc)
date=str(date).split()[0].replace('-','/')


# Write to csv and log
data_dict={'Latitude':lat_list,
           'Longitude':lng_list,
           'Humidity (%)':hum_list,
           'Temperature (F)':tem_list,
           'Cloudiness (%)':clo_list,
           'WindSpeed (mph)':win_list,
           'Date':dat_list,
           'City,Country':citycountry_list}
data_df=pd.DataFrame(data_dict)
data_df.to_csv('data.csv')

with open('log.txt','w') as logfile:
    logfile.writelines(log_list)

# Make plots
plt.style.use('seaborn')
fig,ax=plt.subplots(2,2,figsize=(20, 10))

plot_list=['Temperature (F)','Humidity (%)','Cloudiness (%)','WindSpeed (mph)']
k=0

for m in range(2):
    for n in range(2):
        ax[m,n].scatter(data_df['Latitude'],data_df[plot_list[k]])
        ax[m,n].set_xbound(lower=-80,upper=100)
        ax[m,n].set_title('City Latitude vs. '+plot_list[k].split()[0]+' ('+date+')')
        ax[m,n].set_xlabel('Latitude')
        ax[m,n].set_ylabel(plot_list[k])
        ax[m,n].set_xticks(range(-80,101,20))
        k+=1

plt.tight_layout()
plt.show()


