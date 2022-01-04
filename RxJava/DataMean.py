###
### Step 4 Progetto Evoluzione del Software
###
### Calcolo delle medie delle metriche per ogni commit
### Rimozione duplicati
### Creazione dataset con medie metriche per commit
###

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame
from operator import itemgetter

df1=pd.read_csv("MetricsDataset1.csv", sep = ';', parse_dates = [0], infer_datetime_format = True, header = 0)
print(df1)
df2=pd.read_csv("MetricsDataset2.csv", sep = ';', parse_dates = [0], infer_datetime_format = True, header = 0)
print(df2)
df3=pd.read_csv("MetricsDataset3.csv", sep = ';', parse_dates = [0], infer_datetime_format = True, header = 0)
print(df3)
df4=pd.read_csv("MetricsDataset4.csv", sep = ';', parse_dates = [0], infer_datetime_format = True, header = 0)
print(df4)
df1.drop_duplicates(subset=['fileid','commit_hash', 'modified', 'file'],keep=False,inplace=True)
df2.drop_duplicates(subset=['fileid','commit_hash', 'modified', 'file'],keep=False,inplace=True)
df3.drop_duplicates(subset=['fileid','commit_hash', 'modified', 'file'],keep=False,inplace=True)
df4.drop_duplicates(subset=['fileid','commit_hash', 'modified', 'file'],keep=False,inplace=True)

df = pd.DataFrame()

df = pd.concat([df1, df2, df3, df4])

commit_frame=pd.DataFrame()



massimi=list()

for a in range(0, 870):
    temp=pd.DataFrame()
    df_t = df.loc[df["fileid"]==str(a)]
    temp.insert(0, "fileid", [a])
    temp.insert(1, "commit_hash", [df_t["commit_hash"].values[0]])
    m=df_t["modified"].values
    tot_m=0
    tot_file_modified=0
    for i in m:
        tot_m+=i
        if(i>0):
            tot_file_modified+=1
    massimi.append([df_t["commit_hash"].values[0], tot_m])
    temp.insert(2, "modified", [tot_m])
    temp.insert(3, "file_modified", [tot_file_modified])
    temp.insert(4, 'CBO', [df_t["cbo"].mean()])
    temp.insert(5, 'WMC', [df_t["wmc"].mean()])
    temp.insert(6, 'DIT', [df_t["dit"].mean()])
    temp.insert(7, 'NOC', [df_t["noc"].mean()])
    temp.insert(8, 'RFC', [df_t["rfc"].mean()])
    temp.insert(9, 'LCOM', [df_t["lcom"].mean()]) 
    temp.insert(10, 'LOC', [df_t["loc"].sum()])
    
    commit_frame = pd.concat([commit_frame, temp])


commit_frame.to_csv("DataMean.csv",index=False)


