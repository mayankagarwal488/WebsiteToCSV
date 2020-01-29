import os
from glob import glob
import pandas as pd


interesting_files = glob("[Folder Address]\\*.csv") # it grabs all the csv files from the directory you mention here

df_list = []
for filename in sorted(interesting_files):
    df_list.append(pd.read_csv(filename))
    full_df = pd.concat(df_list, sort=False)

# save the final file in same/different directory:

full_df.to_csv("Combined File.csv", index=False)
