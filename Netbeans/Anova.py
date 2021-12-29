###
### Step 7 Progetto Evoluzione del Software
###
### Test ANOVA sul dataset finale
### 
###

import pandas as pd
from pandas.core.frame import DataFrame
from scipy import stats

def calc_mean(source, n):
    target = pd.DataFrame()
    t = source.loc[df["Type"+str(n)]==1]
    mean = []
    mean.append(t["CBO"].mean())
    mean.append(t["WMC"].mean())
    mean.append(t["DIT"].mean())
    mean.append(t["NOC"].mean())
    mean.append(t["RFC"].mean())
    mean.append(t["LCOM"].mean())
    mean.append(t["LOC"].mean())
    target.insert(0, "Type"+str(n), mean)
    return target["Type"+str(n)]

df=pd.read_csv("DataCategorized.csv", sep = ';', parse_dates = [0], infer_datetime_format = False, header = 0)

dff = pd.DataFrame()

for i in range(0,5):
    dff.insert(i, "Type"+str(i+1), calc_mean(df, i+1))

dff.to_csv("MetricOnTypeDataset.csv", index=False)

anova = pd.DataFrame()

Fcbo, pcbo = stats.f_oneway(df.loc[df["Type1"]==1]["CBO"], df.loc[df["Type2"]==1]["CBO"], df.loc[df["Type3"]==1]["CBO"], df.loc[df["Type4"]==1]["CBO"], df.loc[df["Type5"]==1]["CBO"])
Fwmc, pwmc = stats.f_oneway(df.loc[df["Type1"]==1]["WMC"], df.loc[df["Type2"]==1]["WMC"], df.loc[df["Type3"]==1]["WMC"], df.loc[df["Type4"]==1]["WMC"], df.loc[df["Type5"]==1]["WMC"])
Fdit, pdit = stats.f_oneway(df.loc[df["Type1"]==1]["DIT"], df.loc[df["Type2"]==1]["DIT"], df.loc[df["Type3"]==1]["DIT"], df.loc[df["Type4"]==1]["DIT"], df.loc[df["Type5"]==1]["DIT"])
Fnoc, pnoc = stats.f_oneway(df.loc[df["Type1"]==1]["NOC"], df.loc[df["Type2"]==1]["NOC"], df.loc[df["Type3"]==1]["NOC"], df.loc[df["Type4"]==1]["NOC"], df.loc[df["Type5"]==1]["NOC"])
Frfc, prfc = stats.f_oneway(df.loc[df["Type1"]==1]["RFC"], df.loc[df["Type2"]==1]["RFC"], df.loc[df["Type3"]==1]["RFC"], df.loc[df["Type4"]==1]["RFC"], df.loc[df["Type5"]==1]["RFC"])
Flcom, plcom = stats.f_oneway(df.loc[df["Type1"]==1]["LCOM"], df.loc[df["Type2"]==1]["LCOM"], df.loc[df["Type3"]==1]["LCOM"], df.loc[df["Type4"]==1]["LCOM"], df.loc[df["Type5"]==1]["LCOM"])
Floc, ploc = stats.f_oneway(df.loc[df["Type1"]==1]["LOC"], df.loc[df["Type2"]==1]["LOC"], df.loc[df["Type3"]==1]["LOC"], df.loc[df["Type4"]==1]["LOC"], df.loc[df["Type5"]==1]["LOC"])



print(Fcbo, pcbo)
print(Fwmc, pwmc)
print(Fdit, pdit)
print(Fnoc, pnoc)
print(Frfc, prfc)
print(Flcom, plcom)
print(Floc, ploc)

anova.insert(0, "Metric", ["CBO", "WMC", "DIT", "NOC", "RFC", "LCOM", "LOC"])
anova.insert(1, "F-Value", [Fcbo, Fwmc, Fdit, Fnoc, Frfc, Flcom, Floc])
anova.insert(2, "P-Value", [pcbo, pwmc, pdit, pnoc, prfc, plcom, ploc])

anova.to_csv("AnovaResults.csv", index=False)

for i in ["Type1", "Type2", "Type3", "Type4", "Type5"]:
    ant = pd.DataFrame()
    Pres = []
    Fres = []
    Fcbo, pcbo = stats.f_oneway(df.loc[df[i]==1]["CBO"], df["CBO"])
    Fwmc, pwmc = stats.f_oneway(df.loc[df[i]==1]["WMC"], df["WMC"])
    Fdit, pdit = stats.f_oneway(df.loc[df[i]==1]["DIT"], df["DIT"])
    Fnoc, pnoc = stats.f_oneway(df.loc[df[i]==1]["NOC"], df["NOC"])
    Frfc, prfc = stats.f_oneway(df.loc[df[i]==1]["RFC"], df["RFC"])
    Flcom, plcom = stats.f_oneway(df.loc[df[i]==1]["LCOM"], df["LCOM"])
    Floc, ploc = stats.f_oneway(df.loc[df[i]==1]["LOC"], df["LOC"])
    ant.insert(0, "Metric", ["CBO", "WMC", "DIT", "NOC", "RFC", "LCOM", "LOC"])
    ant.insert(1, "F-Value", [Fcbo, Fwmc, Fdit, Fnoc, Frfc, Flcom, Floc])
    ant.insert(2, "P-Value", [pcbo, pwmc, pdit, pnoc, prfc, plcom, ploc])
    ant.to_csv("AnovaResults"+i+".csv", index=False)



