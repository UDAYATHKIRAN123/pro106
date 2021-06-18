import csv
import plotly.express as ps
with open("tv.csv")as csv_file:
    df=csv.DictReader(csv_file)
    fig=ps.scatter(df,x="Size of TV",y="Average")
    fig.show()