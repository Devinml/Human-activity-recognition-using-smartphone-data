import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def x_y_z_gyros(df, activity):
    df_out = df.copy()
    df_out = df_out[df_out['label'] == activity]
    x = df_out['X']
    y = df_out['Y']
    z = df_out['Z']
    gyrox = df_out['gyroX']
    gyroy = df_out['gyroY']
    gyroz = df_out['gyroZ']
    return [x, y, z, gyrox, gyroy, gyroz]


def acc_at_activity(df, acc_metric):
    df_out = df.copy()
    x1 = x2 = x3 = x4 = x5 = x6 = 0
    list_of_xs = [x1, x2, x3, x4, x5, x6]
    for i in range(1, 7):
        mask = df_out['label'] == i
        list_of_xs[i-1] = df_out[mask][acc_metric]
    return list_of_xs


def boxplots(df, fig, ax, acc_metric):
    data = acc_at_activity(df, acc_metric)
    ax.boxplot(data, showfliers=False)
    plt.xticks([i for i in range(1, 7)], ['Walking',
                                          'Walking up',
                                          'Walking down',
                                          'Sittting',
                                          'Standing',
                                          'Laying'])
    ax.set_title(acc_metric + ' acc at each activity')
    ax.set_ylabel('Acc(gs)')
    ax.set_xlabel('Activity')
    plt.xticks(rotation=45)


if __name__ == '__main__':
    df = pd.read_csv('data/merged_data_save.csv')
    plt.style.use('ggplot')
    fig, ax = plt.subplots(figsize=(12, 8))
    boxplots(df=df, fig=fig, ax=ax, acc_metric='X')
    fig2, ax2 = plt.subplots(figsize=(12, 8))
    boxplots(df=df, fig=fig2, ax=ax2, acc_metric='Y')
    fig3, ax3 = plt.subplots(figsize=(12, 8))
    boxplots(df=df, fig=fig3, ax=ax3, acc_metric='Z')
    plt.show()
