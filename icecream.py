import csv
import plotly.express as ps
import numpy as np

def datasource(datapath):
    icecream=[]
    Temperature=[]
    with open(datapath)as csv_file:
        df=csv.DictReader(csv_file)
        for row in df:
            icecream.append(float(row["Marks In Percentage"]))
            Temperature.append(float(row["Days Present"]))

    return{"x":Temperature,"y":icecream}
    
 
 def correlationfinder(ds):
    correlation=np.corrcoef(ds["x"],ds["y"])
    print(correlation[0,1])

def setup():
    datapath="correlation.csv"
    ds=datasource(datapath)
    correlationfinder(df)

setup()
