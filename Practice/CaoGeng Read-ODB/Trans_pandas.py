import pandas as pd
import sys


folder = sys.argv[0].split('\\')[-2]
file = 'RF_RM_temp.csv'
file_out = folder+'.csv'
file_create = open(file_out,'w')             
file_create.close()

df = pd.read_csv(file,header=None)
df.values
data = df.as_matrix()
data = list(map(list,zip(*data)))
data = pd.DataFrame(data)
data.to_csv(file_out,header=0,index=0)
