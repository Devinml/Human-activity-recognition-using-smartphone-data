import logging
import pandas as pd
import numpy as np
from intensity_bands import IntensityBands
import csv

def write_processed_data(log,df):
    with open('calculated_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['Participant',
                         'activitiy',
                         'x_0_1.17',
                         'x_1.17_2.34',
                         'x_2.34_4.1',
                         'y_0_1.17',
                         'y_1.17_2.34',
                         'y_2.34_4.1',
                         'z_0_1.17',
                         'z_1.17_2.34',
                         'z_2.34_4.1',
                         'gyrox_0_1.17',
                         'gyrox_1.17_2.34',
                         'gyrox_2.34_4.1',
                         'gyroy_0_1.17',
                         'gyroy_1.17_2.34',
                         'gyroy_2.34_4.1',
                         'gyroz_0_1.17',
                         'gyroz_1.17_2.34',
                         'gyroz_2.34_4.1'])  
        for i in range(len(participants)):
            for j in range(len(activities)):
                print(f'participant : {i}  ' + ('='*j) + '>')
                user = participants[i]
                activity = activities[j]
                stop = 120
                start = 0
                x = df[(df['label'] == activities[j]) & (df['user'] == participants[i])]
                while stop<len(df):
                    try:
                        data = x.iloc[start:stop]
                        intensities = IntensityBands(data)
                        intensities._compute_power()
                        (x1, x2, x3,
                         y1, y2, y3,
                         z1, z2, z3,
                         gyro_x1, gyro_x2, gyro_x3,
                         gyro_y1, gyro_y2, gyro_y3,
                         gyro_z1, gyro_z2, gyro_z3) = intensities.intensity_bands()
                        writer.writerow([participants[i],
                                         activities[j],
                                         x1, x2, x3,
                                         y1, y2, y3,
                                         z1, z2, z3,
                                         gyro_x1, gyro_x2, gyro_x3,
                                         gyro_y1, gyro_y2, gyro_y3,
                                         gyro_z1, gyro_z2, gyro_z3])
                        start += 120
                        stop += 120
                    except Exception as e:
                        log.error(e)
                        # raise
                        break
                


if __name__ == '__main__':
    participants = [i for i in range(1,31)]
    activities = [i for i in range(1,7)]
    df = pd.read_csv('data/merged_data_save.csv') 
    logging.basicConfig(filename='erros/log_errors.Log',level=logging.DEBUG)
    log = logging.getLogger()
    write_processed_data(log,df)
