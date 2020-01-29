import requests
import pandas as pd
import csv

with open('For code.csv', newline='') as myfile:
    reader = csv.reader(myfile)
    for row in reader:
        rowarray = ', '.join(row)
        ALLLink = rowarray.split(", ")
        try:
            url = ALLLink[0]
            html = requests.get(url).content
            df_list = pd.read_html(html)
            df = df_list[-1]
            print(df)
            df.to_csv('my data' +ALLLink[1]+ '.csv')
        except:
            pass
