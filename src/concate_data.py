import os
import numpy as np
import pandas as pd
directory = '/home/devin/Documents/Galvanize/repos/Human-activity-recognition-using-smartphone-data/data/RawData'

out_arr = np.empty([0,3])

filepath = directory+'/labels.txt'
out_df = pd.DataFrame(columns=['X', 'Y', 'Z','label'])
label_df = pd.read_csv(filepath, header=None, delim_whitespace=True)
exp_num = 1
acc_list = sorted(os.listdir(directory+'/acc'))
gyro_list = sorted(os.listdir(directory+'/gyro'))
for i in range(len(acc_list)):
    dir_ = directory+ '/acc/'+ acc_list[i]
    b = pd.read_csv(dir_,header=None,delim_whitespace=True)
    dir_gyro = directory + '/gyro/' + gyro_list[i]
    gyro = pd.read_csv(dir_gyro, header=None, delim_whitespace=True)
    b = pd.concat([b,gyro],axis=1)
    b.columns = ['X', 'Y', 'Z','gyroX', 'gyroY','gyroZ']
    b['label'] = 0
    b['user'] = 0
    empty = np.zeros(b.shape)
    for label in label_df.iterrows():
        if label[1][0] == int(acc_list[i][7:9]):
            b.loc[label[1][3]-2: label[1][4]-2, 'label'] = label[1][2]
            b.loc[label[1][3]-2: label[1][4]-2, 'user'] = label[1][1]
    out_df = pd.concat([out_df,b])

out_df.to_csv('/home/devin/Documents/Galvanize/repos/Human-activity-recognition-using-smartphone-data/data/merged_data.csv')



