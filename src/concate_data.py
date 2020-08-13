import os
import numpy as np
import pandas as pd
directory = '/home/devin/Documents/Galvanize/repos/Human-activity-recognition-using-smartphone-data/data/RawData'

out_arr = np.empty([0,3])

filepath = directory+'/labels.txt'
df = pd.read_csv(filepath, header=None, delim_whitespace=True)
exp_num = 1
for entry in sorted(os.listdir(directory)):
    if (entry != 'labels.txt')and ('gyro' not in entry):
        dir_ = directory+ '/'+ entry
        b = pd.read_csv(dir_,header=None,delim_whitespace=True)
        empty = np.zeros(b.shape)
        for label in np.nditer(labels):
            pass
            # labels[]
        
        out_arr = np.concatenate((out_arr,b))
print(out_arr.shape)


