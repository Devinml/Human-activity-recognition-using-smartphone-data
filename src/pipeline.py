import logging
import pandas as pd
import numpy as np
from intensity_bands import IntensityBands, DataStats
import csv


def write_processed_data(log, df, method):
    """
    This function loops through all of my raw data and calculates the
    intensity bands that are going to be used in my clasifier.
    This is the Engineering approach
    Parameters
    ----------
    log to log errors raised for debugging
    DataFrame of meged data
    Returns
    -------
    None
    Saves calculated data into directory
    """
    data_file = input("Specifiy name and location     ")
    with open(data_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        if method == 'spectrum':
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
        elif method == 'stats':
            writer.writerow(['Participant',
                             'activitiy',
                             'x_mean',
                             'y_mean',
                             'z_mean',
                             'gyrox_mean',
                             'gyroy_mean',
                             'gyroz_mean',
                             'x_std',
                             'y_std',
                             'z_std',
                             'gyrox_std',
                             'gyroy_std',
                             'gyroz_std'])
        elif method == 'joined':
            writer.writerow(['Participant',
                             'activitiy',
                             'x_mean',
                             'y_mean',
                             'z_mean',
                             'gyrox_mean',
                             'gyroy_mean',
                             'gyroz_mean',
                             'x_std',
                             'y_std',
                             'z_std',
                             'gyrox_std',
                             'gyroy_std',
                             'gyroz_std',
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
                x = df[(df['label'] == activity) &
                       (df['user'] == user)]
                while stop < len(x):
                    try:
                        data = x.iloc[start:stop]
                        if method == 'spectrum':
                            print(i, j, 'inloop')
                            spectrum_method(data,
                                            writer,
                                            i,
                                            j,
                                            participants,
                                            activities)
                        elif method == 'stats':
                            stats_method(data,
                                         writer,
                                         i,
                                         j,
                                         participants,
                                         activities)
                        elif method == 'joined':
                            joined_method(data,
                                          writer,
                                          i,
                                          j,
                                          participants,
                                          activities)
                        start += 120
                        stop += 120
                    except Exception as e:
                        log.error(e)
                        raise
                        break


def spectrum_method(data, writer, i, j, participants, activities):
    """
    This Function gets data from the intensty class and writes them
    to a CSV file
    Parmaeters
    ----------
    data = Dataframe of the subseted data
    writer = the writing object for writing to a csc
    i = the participant indexer
    j = the activity indexer
    participants = list of participants
    activiites = list of activities
    Returns
    --------
    None
    """
    intense = IntensityBands(data)
    (x1, x2, x3,
     y1, y2, y3,
     z1, z2, z3,
     gyro_x1, gyro_x2, gyro_x3,
     gyro_y1, gyro_y2, gyro_y3,
     gyro_z1, gyro_z2, gyro_z3) = intense.intensity_bands()
    writer.writerow([participants[i],
                     activities[j],
                     x1, x2, x3,
                     y1, y2, y3,
                     z1, z2, z3,
                     gyro_x1, gyro_x2, gyro_x3,
                     gyro_y1, gyro_y2, gyro_y3,
                     gyro_z1, gyro_z2, gyro_z3])


def stats_method(data, writer, i, j, participants, activities):
    """
    This Function gets data from the stats class and writes them
    to a CSV file
    Parmaeters
    ----------
    data = Dataframe of the subseted data
    writer = the writing object for writing to a csc
    i = the participant indexer
    j = the activity indexer
    participants = list of participants
    activiites = list of activities
    Returns
    --------
    None
    """
    stat = DataStats(data)
    (x_mean,
     y_mean,
     z_mean,
     gyrox_mean,
     gyroy_mean,
     gyroz_mean,
     x_std,
     y_std,
     z_std,
     gyrox_std,
     gyroy_std,
     gyroz_std) = stat.get_stats()
    writer.writerow([participants[i],
                     activities[j],
                     x_mean,
                     y_mean,
                     z_mean,
                     gyrox_mean,
                     gyroy_mean,
                     gyroz_mean,
                     x_std,
                     y_std,
                     z_std,
                     gyrox_std,
                     gyroy_std,
                     gyroz_std])


def joined_method(data, writer, i, j, participants, activities):
    stat = DataStats(data)
    (x_mean,
     y_mean,
     z_mean,
     gyrox_mean,
     gyroy_mean,
     gyroz_mean,
     x_std,
     y_std,
     z_std,
     gyrox_std,
     gyroy_std,
     gyroz_std) = stat.get_stats()
    intense = IntensityBands(data)
    (x1, x2, x3,
     y1, y2, y3,
     z1, z2, z3,
     gyro_x1, gyro_x2, gyro_x3,
     gyro_y1, gyro_y2, gyro_y3,
     gyro_z1, gyro_z2, gyro_z3) = intense.intensity_bands()
    writer.writerow([participants[i],
                     activities[j],
                     x_mean,
                     y_mean,
                     z_mean,
                     gyrox_mean,
                     gyroy_mean,
                     gyroz_mean,
                     x_std,
                     y_std,
                     z_std,
                     gyrox_std,
                     gyroy_std,
                     gyroz_std,
                     x1, x2, x3,
                     y1, y2, y3,
                     z1, z2, z3,
                     gyro_x1, gyro_x2, gyro_x3,
                     gyro_y1, gyro_y2, gyro_y3,
                     gyro_z1, gyro_z2, gyro_z3])


if __name__ == '__main__':
    participants = [i for i in range(1, 31)]
    activities = [i for i in range(1, 7)]
    df = pd.read_csv('data/merged_data_save.csv')

    # print(df.head())
    logging.basicConfig(filename='erros/log_errors.Log', level=logging.DEBUG)
    log = logging.getLogger()
    write_processed_data(log, df, 'joined')
