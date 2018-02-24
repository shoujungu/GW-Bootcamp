from flask import Flask
from flask import jsonify
from flask import render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def homepage():
     return render_template('index.html')

@app.route('/names')
def names():
    #list of sample names
    filename="belly_button_biodiversity_samples.csv"
    df=pd.read_csv(filename)
    cols=df.columns.values.tolist()[1:]
    #cols=json.dumps(cols)
    return jsonify(cols)

@app.route('/otu')
def otu():
    #List of OTU descriptions
    filename="belly_button_biodiversity_otu_id.csv"
    df=pd.read_csv(filename)
    otu=df['lowest_taxonomic_unit_found'].values.tolist()
    #otu=json.dumps(otu)
    return jsonify(otu)

@app.route('/metadata/<sample>')
def metadata(sample):
    #MetaData for a given sample
    id=int(sample.split('_')[-1])
    filename="Belly_Button_Biodiversity_Metadata.csv"
    df=pd.read_csv(filename)
    data=df.loc[df['SAMPLEID']==id,:].stack()
    data.index=data.index.droplevel()
    #data=json.dumps(data.to_dict())
    return jsonify(data)

@app.route('/wfreq/<sample>')
def wfreq(sample):
    #Weekly Washing Frequency as a number
    id=int(sample.split('_')[-1])
    filename="Belly_Button_Biodiversity_Metadata.csv"
    df=pd.read_csv(filename)
    data=df.loc[df['SAMPLEID']==id,'WFREQ'][0]
    return data

@app.route('/samples/<sample>')
def samples(sample):
    #OTU IDs and Sample Values for a given sample
    filename="belly_button_biodiversity_samples.csv"
    filename2="belly_button_biodiversity_otu_id.csv"
    df=pd.read_csv(filename).dropna().loc[:,['otu_id',sample]]
    df2=pd.read_csv(filename2).dropna()
    df=df.merge(df2, how='inner').loc[:,['otu_id',sample,'lowest_taxonomic_unit_found']]
    df=df.sort_values(sample, ascending=False)
    data=[{'otu_ids':df['otu_id'].values.tolist(), 'sample_values':df[sample].values.astype(str).tolist(),
    'description':df['lowest_taxonomic_unit_found'].values.astype(str).tolist()}]
    #data=json.dumps(data)
    return jsonify(data)

if __name__=='__main__':
    app.run()
