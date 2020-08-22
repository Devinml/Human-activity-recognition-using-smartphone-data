import pandas as pd
import numpy as np
from scipy.signal import welch
from scipy.integrate import simps


class IntensityBands(object):
    """
    Calculates the integral of the power spectrum for the
    accelerometer data, given a spectrum of the dataframe
    there are 3 spectrums chosen.
    Parameters
    ----------
    subsample of accelerometer data
    Returns
    -------
    integral of spectrum evaluated a the 3 spectrums defined above
    """
    def __init__(self, df):
        self.df = df

    def _compute_power(self):
        """
        Computes the power spectrum for each accelerometer measurment
        Parameters
        ----------
        self

        Returns
        -------
        None
        """
        self.f, self.x_power = welch(self.df['X'], fs=50)
        _, self.y_power = welch(self.df['Y'], fs=50)
        _, self.z_power = welch(self.df['Z'], fs=50)
        _, self.gyro_x = welch(self.df['gyroX'], fs=50)
        _, self.gyro_y = welch(self.df['gyroY'], fs=50)
        _, self.gyro_z = welch(self.df['gyroZ'], fs=50)

    def intensity_bands(self):
        """
        Calculates the integral of the power spectrum for
        the accelerometer data, there are 3 spectrums chosen.
        1. 0 : 1.17 Hz
        2. 1.17 : 2.34 Hz
        3. 2.34 : 4.1 Hz

        Parameters
        ----------
        Power spectrums for each accelerometer

        Returns
        -------
        integral of spectrum evaluated a the 3 spectrums defined above
        (x1, x2, x3,
         y1, y2, y3,
         z1, z2, z3,
         gyro_x1, gyro_x2, gyro_x3,
         gyro_y1, gyro_y2, gyro_y3,
         gyro_z1, gyro_z2, gyro_z3) = intensity_bands()
        """
        x1 = 0
        x2 = 0
        x3 = 0
        y1 = 0
        y2 = 0
        y3 = 0
        z1 = 0
        z2 = 0
        z3 = 0
        gyro_x1 = 0
        gyro_x2 = 0
        gyro_x3 = 0
        gyro_y1 = 0
        gyro_y2 = 0
        gyro_y3 = 0
        gyro_z1 = 0
        gyro_z2 = 0
        gyro_z3 = 0
        integraters = [x1,
                       x2,
                       x3,
                       y1,
                       y2,
                       y3,
                       z1,
                       z2,
                       z3,
                       gyro_x1,
                       gyro_x2,
                       gyro_x3,
                       gyro_y1,
                       gyro_y2,
                       gyro_y3,
                       gyro_z1,
                       gyro_z3,
                       gyro_z2]
        x = [[0, 7], [6, 13], [12, 21]]
        power_spectrums = [self.x_power,
                           self.y_power,
                           self.z_power,
                           self.gyro_x,
                           self.gyro_y,
                           self.gyro_z]
        indexer = 0
        for i in range(len(power_spectrums)):
            for j in range(len(x)):
                start = x[j][0]
                stop = x[j][1]
                integraters[indexer] = simps(power_spectrums[i][start:stop],
                                             x=self.f[start:stop])
                indexer += 1
        return tuple(integraters)


if __name__ == "__main__":
    df = pd.read_csv('data/merged_data.csv')
    df_up = df[df['label'] == 2]
    spec = IntensityBands(df_up)
    spec._compute_power()
    (x1, x2, x3,
     y1, y2, y3,
     z1, z2, z3,
     gyro_x1, gyro_x2, gyro_x3,
     gyro_y1, gyro_y2, gyro_y3,
     gyro_z1, gyro_z2, gyro_z3) = spec.intensity_bands()
    print(spec.intensity_bands())
