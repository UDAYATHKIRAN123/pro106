import csv
import plotly.express as ps
with open("mark.csv")as csv_file:
    df=csv.DictReader(csv_file)
    fig=ps.scatter(df,x="Marks In Percentage",y="Days Present")
    fig.show()