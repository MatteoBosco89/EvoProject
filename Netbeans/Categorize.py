###
### Step 5 Progetto Evoluzione del Software
###
### Categorizzazione tipologia di errore in base alle righe di codice modificate
### Normalizzazione in base al massimo e minimo numero di righe modificate
### Scala su 5 fasce
### Creazione dataset finale
###

import pandas as pd
from pandas.core.frame import DataFrame
import openpyxl
from openpyxl import load_workbook
import pprint



df=pd.read_csv("DataMean.csv", sep = ';', parse_dates = [0], infer_datetime_format = False, header = 0)
massimo=df["modified"].max()
aliquota=massimo/5
dfc=pd.DataFrame()
res=pd.DataFrame()

dfc.insert(0, "Type1", 0)
dfc.insert(1, "Type2", 0)
dfc.insert(2, "Type3", 0)
dfc.insert(3, "Type4", 0)
dfc.insert(4, "Type5", 0)
dfc.insert(5, "Type", "")
res=pd.concat([df,dfc])
res["Type1"]=0
res["Type2"]=0
res["Type3"]=0
res["Type4"]=0
res["Type5"]=0
res["Type"]=""
print(res)
for i,e in res.iterrows():
    l=int(e["modified"])
    if(l >= 0):
        if(l <= aliquota): 
            res.at[i, 'Type1'] = 1
            res.at[i, 'Type'] = "Type1"
        elif(l <= aliquota*2): 
            res.at[i, 'Type2'] = 1
            res.at[i, 'Type'] = "Type2"
        elif(l <= aliquota*3): 
            res.at[i, 'Type3'] = 1
            res.at[i, 'Type'] = "Type3"
        elif(l <= aliquota*4): 
            res.at[i, 'Type4'] = 1
            res.at[i, 'Type'] = "Type4"
        elif(l <= aliquota*5): 
            res.at[i, 'Type5'] = 1
            res.at[i, 'Type'] = "Type5"
res.to_csv("DataCategorized.csv", index=False)