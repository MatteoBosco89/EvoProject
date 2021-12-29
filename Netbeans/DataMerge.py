###
### Step 3 Progetto Evoluzione del Software
###
### Merge per creazione dataset con metriche per ogni commit e righe modificate
###

import pandas as pd
import os


folderName = input("Insert folder name: ")
result = pd.DataFrame()
data_dir= os.listdir(folderName)

data_dir=sorted(data_dir,reverse=False,key=lambda f: int(f.split("_")[0])) 
#data_dir.reverse()
#print(data_dir)
print("+++++++++++++++++++++ INIZIO MERGE +++++++++++++++++++++++")

diff_df = pd.read_csv('DiffDataset.csv', parse_dates = [0], infer_datetime_format = True, header = 0)

for filename in data_dir:
    print(filename)
    file_df = pd.read_csv(folderName+"/"+filename, sep = ',', parse_dates = [0], infer_datetime_format = True, header = 0)
    file_df['commit_hash'] = filename.split("_")[1].strip(".csv")
    fileid = filename.split("_")[0]
    temp_col = file_df['commit_hash']
    id_col = pd.DataFrame()
    modif = pd.DataFrame()
    id_col["fileid"] = fileid
    modif["modified"] = 0
    file_df.drop(labels=['commit_hash'], axis=1,inplace = True)
    file_df.insert(0, 'fileid', id_col)
    file_df.insert(1, 'commit_hash', temp_col)
    file_df.insert(2, 'modified', modif)
    file_df['fileid'] = fileid
    file_df['modified'] = 0
    tempframe = diff_df.loc[(diff_df['hash'] == filename.split("_")[1].strip(".csv"))]
    l = tempframe["file"]
    for a in l:
        v = tempframe.loc[(tempframe['file'] == a)]['modlines'].values
        t1 = file_df.loc[(file_df['file'] == a.replace("/", "/"))]["modified"] 
        for i in t1.index:
            file_df.iloc[i,2] = int(v[0])
    result = pd.concat([result, file_df])
    
result.to_csv("MetricsDataset.csv", index = False)