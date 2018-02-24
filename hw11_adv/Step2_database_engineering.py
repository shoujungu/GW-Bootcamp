import pandas as pd
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import Session

Base = declarative_base()

#read data to df
df_m=pd.read_csv('clean_hawaii_measurements.csv')
df_s=pd.read_csv('clean_hawaii_stations.csv')
df_m['date'] = pd.to_datetime(df_m['date'],format='%Y-%m-%d')

#create db
class Measurement(Base):
    __tablename__ = 'measurement'
    id = Column(Integer, primary_key=True)
    station = Column(String(15))
    date = Column(Date)
    prcp = Column(Float)
    tobs = Column(Integer)

class Station(Base):
    __tablename__ = 'station'
    id = Column(Integer, primary_key=True)
    station = Column(String(15))
    name = Column(String(250))
    latitude = Column(Float)
    longitude = Column(Float)
    elevation = Column(Float)

engine = sa.create_engine("sqlite:///hawaii.sqlite", echo=False)
conn = engine.connect()
Base.metadata.create_all(conn)
session = Session(bind=engine)

for index, row in df_m.iterrows():
    mea=Measurement(id=index, station=row['station'],date=row['date'],
                    prcp=row['prcp'],tobs=row['tobs'])
    session.add(mea)
session.commit()

for index, row in df_s.iterrows():
    sta=Station(id=index, station=row['station'],name=row['name'],
                latitude=row['latitude'],longitude=row['longitude'],
                elevation=row['elevation'])
    session.add(sta)
session.commit()
