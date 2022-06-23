from application import app
from flask import render_template, request
import pandas as pd
import json
import plotly
import plotly.express as px
import seaborn as sns
from sklearn import preprocessing


@app.route('/')
def index():
    return render_template('index1.html')


@app.route('/table')
def table():
    
    # converting csv to html
    data = pd.read_csv('preprocessed.csv')
    data.to_html()
   
    #return render_template('display.html', tables=[data.to_html()], titles=[''])
    return render_template('display.html', tables=[data.iloc[0:42,1:9].to_html()], titles=[''])
    #return render_template('display.html', tables=[data[:1]], titles=[''])

@app.route('/chart1')
def chart1():

    df = pd.read_csv("preprocessed.csv")
    fig1 = px.histogram(df, x=df["Project Domain"], title="Project Domain")
    graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)


    # Graph 2
    
    df = pd.read_csv("preprocessed.csv")
    
    label_encoder = preprocessing.LabelEncoder()
    df['Name of the Project Guide']= label_encoder.fit_transform(df['Name of the Project Guide'])
    labels= 'prof. prashant gadakh', 'prof. bailappa bhovi','prof. ashwini jarali', 'dr. sashikala mishra','prof. ramkrushna m', 'prof. ajitkumar shitole','prof. sandeep patil', 'prof. deptii c.'
    fig2 = px.pie(values=df["Name of the Project Guide"].value_counts(),  names=labels,
            color_discrete_sequence=px.colors.sequential.RdBu,title="Faculty Distribution")
    graph2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph 3
    df = pd.read_csv("preprocessed.csv")
    
    fig3 = px.bar(df, x=df["Project Domain"], y=df["Name of the Project Guide"],title="Project Domain Vs Faculty")
    graph3JSON = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)
 
 
    # Graph 4
    df = pd.read_csv("preprocessed.csv")
    fig4 = px.scatter_3d(df, x=df["Project Domain"], y=df["Name of the Project Guide"],
              z=df["pub_status"],  color=df["year"].astype("int64"),title="3D Visualization")
    graph4JSON = json.dumps(fig4, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph 5
    
    df = pd.read_csv("preprocessed.csv")
    fig5 = px.histogram(df, x=df["pub_status"], title="Publication Status")
    graph5JSON = json.dumps(fig5, cls=plotly.utils.PlotlyJSONEncoder)
    

    # Graph 6
    
    df = pd.read_csv("preprocessed.csv")
    fig6 = px.histogram(df, x=df["Project Domain"],color = df["pub_status"], title="Publication vs Domain")
    graph6JSON = json.dumps(fig6, cls=plotly.utils.PlotlyJSONEncoder)

    
    # Graph 7
    
    df = pd.read_csv("preprocessed.csv")
    fig7 = px.histogram(df, x=df["Name of the Project Guide"],color = df["pub_status"], title="Publication vs Faculty")
    graph7JSON = json.dumps(fig7, cls=plotly.utils.PlotlyJSONEncoder)

  

    return render_template('index.html', graph1JSON=graph1JSON,  graph2JSON=graph2JSON, graph3JSON=graph3JSON, 
    graph4JSON=graph4JSON, graph5JSON=graph5JSON, graph6JSON=graph6JSON, graph7JSON=graph7JSON)



@app.route('/search')
def search():
    
    return render_template('search.html')
    #return render_template('display.html', tables=[data[:1]], titles=[''])

@app.route('/search/iot')
def iot():
    data=pd.read_csv("preprocessed.csv")
    rslt_df = data[data['Project Domain'] == "iot"]
    rslt_df.drop("Project Domain",axis=1,inplace=True)
    return render_template('iot.html',tables=[rslt_df.to_html()], titles=[''])


@app.route('/search/deeplearning')
def deeplearning():
    data=pd.read_csv("preprocessed.csv")
    rslt_df = data[data['Project Domain'] == "deep learning"]
    rslt_df.drop("Project Domain",axis=1,inplace=True)
    return render_template('deeplearning.html',tables=[rslt_df.to_html()], titles=[''])



@app.route('/search/gis')
def gis():
    data=pd.read_csv("preprocessed.csv")
    rslt_df = data[data['Project Domain'] == "gis"]
    rslt_df.drop("Project Domain",axis=1,inplace=True)
    return render_template('gis.html',tables=[rslt_df.to_html()], titles=[''])

@app.route('/search/blockchain')
def blockchain():
    data=pd.read_csv("preprocessed.csv")
    rslt_df = data[data['Project Domain'] == "block chain"]
    rslt_df.drop("Project Domain",axis=1,inplace=True)
    return render_template('blockchain.html',tables=[rslt_df.to_html()], titles=[''])

@app.route('/search/cybersecurity')
def cybersecurity():
    data=pd.read_csv("preprocessed.csv")
    rslt_df = data[data['Project Domain'] == "cyber security"]
    rslt_df.drop("Project Domain",axis=1,inplace=True)
    return render_template('cybersecurity.html',tables=[rslt_df.to_html()], titles=[''])

@app.route('/search/datamining')
def dataminingain():
    data=pd.read_csv("preprocessed.csv")
    rslt_df = data[data['Project Domain'] == "data mining"]
    rslt_df.drop("Project Domain",axis=1,inplace=True)
    return render_template('dataminingain.html',tables=[rslt_df.to_html()], titles=[''])

@app.route('/search/artificialintelligence')
def artificialintelligence():
    data=pd.read_csv("preprocessed.csv")
    rslt_df = data[data['Project Domain'] == "artificial intelligence"]
    rslt_df.drop("Project Domain",axis=1,inplace=True)
    return render_template('artificialintelligence.html',tables=[rslt_df.to_html()], titles=[''])

@app.route('/search/machinelearning')
def machinelearning():
    data=pd.read_csv("preprocessed.csv")
    rslt_df = data[data['Project Domain'] == "machine learning"]
    rslt_df.drop("Project Domain",axis=1,inplace=True)
    return render_template('machinelearning.html',tables=[rslt_df.to_html()], titles=[''])

@app.route('/search/datascience')
def datascience():
    data=pd.read_csv("preprocessed.csv")
    rslt_df = data[data['Project Domain'] == "data science"]
    rslt_df.drop("Project Domain",axis=1,inplace=True)
    return render_template('datascience.html',tables=[rslt_df.to_html()], titles=[''])

@app.route('/search/geofencing')
def geofencing():
    data=pd.read_csv("preprocessed.csv")
    rslt_df = data[data['Project Domain'] == "geo-fencing"]
    rslt_df.drop("Project Domain",axis=1,inplace=True)
    return render_template('geofencing.html',tables=[rslt_df.to_html()], titles=[''])

@app.route('/search/fintech')
def fintech():
    data=pd.read_csv("preprocessed.csv")
    rslt_df = data[data['Project Domain'] == "fintech"]
    rslt_df.drop("Project Domain",axis=1,inplace=True)
    return render_template('fintech.html',tables=[rslt_df.to_html()], titles=[''])

@app.route('/search/webscrapping')
def webscrapping():
    data=pd.read_csv("preprocessed.csv")
    rslt_df = data[data['Project Domain'] == "web scrapping/crawling"]
    rslt_df.drop("Project Domain",axis=1,inplace=True)
    return render_template('webscrapping.html',tables=[rslt_df.to_html()], titles=[''])


@app.route('/search/prashant')
def prashant():
    data=pd.read_csv("preprocessed.csv")
    rslt_df = data[data['Name of the Project Guide'] == "prof. prashant gadakh"]
    rslt_df.drop("Name of the Project Guide",axis=1,inplace=True)
    return render_template('prashant.html',tables=[rslt_df.to_html()], titles=[''])





@app.route('/search/bailappa')
def bailappa():
    data=pd.read_csv("preprocessed.csv")
    rslt_df = data[data['Name of the Project Guide'] == "prof. bailappa bhovi"]
    rslt_df.drop("Name of the Project Guide",axis=1,inplace=True)
    return render_template('bailappa.html',tables=[rslt_df.to_html()], titles=[''])




@app.route('/search/ashwini')
def ashwini():
    data=pd.read_csv("preprocessed.csv")
    rslt_df = data[data['Name of the Project Guide'] == "prof. ashwini jarali"]
    rslt_df.drop("Name of the Project Guide",axis=1,inplace=True)
    return render_template('ashwini.html',tables=[rslt_df.to_html()], titles=[''])

@app.route('/search/sashikala')
def sashikala():
    data=pd.read_csv("preprocessed.csv")
    rslt_df = data[data['Name of the Project Guide'] == "dr. sashikala mishra"]
    rslt_df.drop("Name of the Project Guide",axis=1,inplace=True)
    return render_template('sashikala.html',tables=[rslt_df.to_html()], titles=[''])

@app.route('/search/ramkrushna')
def ramkrushna():
    data=pd.read_csv("preprocessed.csv")
    rslt_df = data[data['Name of the Project Guide'] == "prof. ramkrushna m"]
    rslt_df.drop("Name of the Project Guide",axis=1,inplace=True)
    return render_template('ramkrushna.html',tables=[rslt_df.to_html()], titles=[''])

@app.route('/search/ajitkumar')
def ajitkumar():
    data=pd.read_csv("preprocessed.csv")
    rslt_df = data[data['Name of the Project Guide'] == "prof. ajitkumar shitole"]
    rslt_df.drop("Name of the Project Guide",axis=1,inplace=True)
    return render_template('ajitkumar.html',tables=[rslt_df.to_html()], titles=[''])

@app.route('/search/sandeep')
def sandeep():
    data=pd.read_csv("preprocessed.csv")
    rslt_df = data[data['Name of the Project Guide'] == "prof. sandeep patil"]
    rslt_df.drop("Name of the Project Guide",axis=1,inplace=True)
    return render_template('sandeep.html',tables=[rslt_df.to_html()], titles=[''])

@app.route('/search/deptii')
def deptii():
    data=pd.read_csv("preprocessed.csv")
    rslt_df = data[data['Name of the Project Guide'] == "prof. deptii c."]
    rslt_df.drop("Name of the Project Guide",axis=1,inplace=True)
    return render_template('deptii.html',tables=[rslt_df.to_html()], titles=[''])

@app.route('/abstract')
def abstract():
    return render_template('abstract.html')

@app.route('/abstract1', methods=['GET', 'POST'])
def abstract1():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       index = request.form.get("index")
       # getting input with name = lname in HTML form 
       data=pd.read_csv("abstract.csv", encoding= 'unicode_escape')
       #rslt_df = data[data['Index'].loc[0]]
       rslt_df = data[data['Index'] == int(index)]
       #rslt_df = data[data['Index'] == int(index)]
       # rslt_df['Abstract']
       title = rslt_df['Index']
       abs1 = rslt_df['Abstract']
       return abs1[int(index)]
    return render_template('abstract1.html')
