from flask import Flask
import pandas as pd
import numpy as np
import sqlalchemy as sa
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import json
import datetime

now = datetime.datetime.now().strftime("%Y-%m-%d")

Base = automap_base()

engine = sa.create_engine("sqlite:///hawaii.sqlite", echo=False)
Base.prepare(engine, reflect=True)

Mea = Base.classes.measurement
Sta = Base.classes.station
session = Session(bind=engine)

app = Flask(__name__)

@app.route("/api/v1.0/precipitation")
def prcp():
    prc=[]
    date_index=[]
    for row in session.query(Mea.date, Mea.prcp).filter(Mea.date>'2016-12-31').all():
        date_index.append(row[0])
        prc.append(row[1])
    dic={str(date_index[i]):prc[i] for i in range(len(prc))}
    dic = json.dumps(dic)
    return dic

@app.route("/api/v1.0/stations")
def stations():
    sta=[]
    for row in session.query(Sta.station).all():
        sta.append(row[0])
    sta=json.dumps(sta)
    return sta
    
@app.route("/api/v1.0/tobs")
def tobs():
    tobs=[]
    date_index=[]
    for row in session.query(Mea.date, Mea.tobs).filter(Mea.date>'2016-12-31').all():
        date_index.append(row[0])
        tobs.append(row[1])
    dic={str(date_index[i]):tobs[i] for i in range(len(tobs))}
    dic = json.dumps(dic)
    return dic

@app.route("/api/v1.0/<start>")
def start(start):
    date_index=[]
    tobs=[]
    for row in session.query(Mea.date,Mea.tobs).filter((Mea.date>=start) & (Mea.date<=now)).all():
        date_index.append(row[0])
        tobs.append(row[1])
    df=pd.DataFrame({'tobs':tobs},index=date_index)
    _min=np.min(df['tobs'])
    _max=np.max(df['tobs'])
    avg=np.mean(df['tobs'])
    r='TMIN: {}, TMAX: {}, TAVG: {}'.format(_min,_max,avg) 
    return r

@app.route("/api/v1.0/<start>/<end>")
def start_end(start,end):
    date_index=[]
    tobs=[]
    for row in session.query(Mea.date,Mea.tobs).filter((Mea.date>=start) & (Mea.date<=end)).all():
        date_index.append(row[0])
        tobs.append(row[1])
    df=pd.DataFrame({'tobs':tobs},index=date_index)
    _min=np.min(df['tobs'])
    _max=np.max(df['tobs'])
    avg=np.mean(df['tobs'])
    r='TMIN: {}, TMAX: {}, TAVG: {}'.format(_min,_max,avg) 
    return r
    
