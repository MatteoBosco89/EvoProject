import pandas as pd
import os

folderName = input("Insert folder name: ")
result = pd.DataFrame()
data_dir= os.listdir(folderName)

data_dir=sorted(data_dir,key=lambda f: os.stat(folderName+"/"+f).st_birthtime)


for filename in os.listdir(folderName):
    print(filename)
    file_df = pd.read_csv(folderName+"/"+filename, sep = ',', parse_dates = [0], infer_datetime_format = True, header = 0)
    file_df['commit_hash'] = filename.strip(".csv")
    temp_col = file_df['commit_hash']
    file_df.drop(labels=['commit_hash'], axis=1,inplace = True)
    file_df.insert(0, 'commit_hash', temp_col)
    result = pd.concat([result, file_df])
result.to_csv("MetricsDataset.csv", index = False)