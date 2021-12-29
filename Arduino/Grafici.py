###
### Step 6 Progetto Evoluzione del Software
###
### Creazione grafici per analisi a partire dal dataset finale
### 
###

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame
from operator import itemgetter
import seaborn as sb


df=pd.read_csv("DataCategorized.csv", sep = ';', parse_dates = [0], infer_datetime_format = True, header = 0)
massimi = list()
max = pd.DataFrame()
cbo_type1 = list()

for i, d in df.iterrows():
    massimi.append([d["commit_hash"], d["modified"], d["CBO"]])
    if(int(d["Type1"]) == 1):
        cbo_type1.append([i, d["CBO"]])

massimi=sorted(massimi, reverse=True, key=lambda f: int(f[1])) 
m = list()
c = list()
cbo_boxplot = list()
for x in range(0,10):
    m.append(massimi[x][1])
    c.append(massimi[x][0])
    cbo_boxplot.append([massimi[x][2], 0])

max.insert(0, "Max", m)
max.insert(1, "commit", c)

max.plot(x="commit", y="Max", kind="bar",figsize=(9,8))
plt.show()

fig = plt.figure(figsize=[10, 7])

### CREAZIONE BOX PLOT

sb.boxplot(x="Type", y="CBO", data=df)
plt.title("CBO")
plt.show()
sb.boxplot(x="Type", y="WMC", data=df)
plt.title("WMC")
plt.show()
sb.boxplot(x="Type", y="DIT", data=df)
plt.title("DIT")
plt.show()
sb.boxplot(x="Type", y="NOC", data=df)
plt.title("NOC")
plt.show()
sb.boxplot(x="Type", y="RFC", data=df)
plt.title("RFC")
plt.show()
sb.boxplot(x="Type", y="LCOM", data=df)
plt.title("LCOM")
plt.show()
sb.boxplot(x="Type", y="LOC", data=df)
plt.title("LOC")
plt.show()

### CREAZIONE GRAFICI PER ANALISI TEMPORALE

### ANALISI FILE E LINEE MODIFICATE

df.plot(x="commit_hash", y="file_modified",kind="bar",figsize=(9,8))
plt.title("File modificati dai commit")
plt.show()

df.plot(x="commit_hash", y="modified",kind="bar",figsize=(9,8))
plt.title("Linee modificate dai commit")
plt.show()


### ANALISI TEMPORALE METRICHE

df.plot(x="commit_hash", y=["CBO"])
plt.axhline(2,color="red")
plt.show()


df.plot(x="commit_hash", y=["WMC"])
plt.axhline(14,color="red")
plt.show()


df.plot(x="commit_hash", y=["DIT"])
plt.axhline(7,color="red")
plt.show()


df.plot(x="commit_hash", y=["RFC"])
plt.show()


df.plot(x="commit_hash", y=["LCOM"])
plt.show()


df.plot(x="commit_hash", y=["NOC"])
plt.show()


df.plot(x="commit_hash", y=["LOC"])
plt.show()

