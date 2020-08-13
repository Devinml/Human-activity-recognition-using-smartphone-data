import os
import numpy as np
import pandas as pd
directory = '/home/devin/Documents/Galvanize/repos/Human-activity-recognition-using-smartphone-data/data/RawData'

out_arr = np.empty([0,3])

filepath = directory+'/labels.txt'
out_df = pd.DataFrame(columns=['X', 'Y', 'Z','label'])
label_df = pd.read_csv(filepath, header=None, delim_whitespace=True)
exp_num = 1
for entry in sorted(os.listdir(directory+'/acc')):
    if (entry != 'labels.txt')and ('gyro' not in entry):
        dir_ = directory+ '/acc/'+ entry
        b = pd.read_csv(dir_,header=None,delim_whitespace=True)
        b.columns = ['X', 'Y', 'Z']
        b['label'] = 0
        empty = np.zeros(b.shape)
        for label in label_df.iterrows():
            if label[1][0] == int(entry[7:9]):
                b.loc[label[1][3]-2: label[1][4]-2, 'label'] = label[1][2]
        out_df = pd.concat([out_df,b])

out_df.to_csv('/home/devin/Documents/Galvanize/repos/Human-activity-recognition-using-smartphone-data/data/merged_data.csv')



