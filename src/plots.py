import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np


def x_y_z_gyros(df, activity):
    """
    Returns the activity accerometer values at a given
    activity label
    Parameters
    ----------
    DataFrame of data
    activity label
    Returns
    -------
    list of :
    x,y,z,gyrox,gyroy,gyroz
    """
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
    """
    Returns one accelerometer value for all activities
    Parameters
    ----------
    DataFrame of data
    Returns
    -------
    List of acceleration data
    """
    df_out = df.copy()
    x1 = x2 = x3 = x4 = x5 = x6 = 0
    list_of_xs = [x1, x2, x3, x4, x5, x6]
    for i in range(1, 7):
        mask = df_out['label'] == i
        list_of_xs[i-1] = df_out[mask][acc_metric]
    return list_of_xs


def boxplots(df, fig, ax, acc_metric):
    """
    This function plots all of my acceleration data for
    all activities
    Parameters
    ----------
    DataFrame of Data
    figure to plot on
    axis to plot on
    What acceleration metric you want to plot
    Returns
    -------
    Boxplot of activities
    """
    data = acc_at_activity(df, acc_metric)
    box = plt.boxplot(data,
                      showfliers=False,
                      patch_artist=True,
                      medianprops=dict(color='k'))
    colors = ['blue', 'red', 'green', 'c', 'violet', 'orange']
    for patch, color in zip(box['boxes'], colors):
        patch.set_facecolor(color)
    plt.xticks([i for i in range(1, 7)], ['Walking',
                                          'Walking up',
                                          'Walking down',
                                          'Sittting',
                                          'Standing',
                                          'Laying'])
    ax.set_title(acc_metric + ' acc at Activity')
    ax.set_ylabel('Acc(gs)')
    ax.set_xlabel('Activity')
    plt.xticks(rotation=45)


def barplot():
    fig_7, ax_7 = plt.subplots(figsize=(12, 8))
    labels = ['Walking', 'Walking Up', 'Walking Down',
              'Sitting', 'Standing', 'Laying']
    stats_f1 = [0.87, 0.86, 0.93, 0.91, 0.92, 0.99]
    spec_f1 = [0.91, 0.86, 0.85, 0.75, 0.74, 0.77]
    combined_f1 = [0.93, 0.89, 0.96, 0.91, 0.93, 0.99]
    x = np.arange(len(labels))
    width = 0.25
    rects1 = ax_7.bar(x - width,
                      spec_f1, width,
                      label='Spec F1',
                      color='darkseagreen')
    rects2 = ax_7.bar(x, stats_f1,
                      width,
                      label='Stats F1',
                      color='orchid')
    rects3 = ax_7.bar(x + width, combined_f1,
                      width,
                      label='Combined F1',
                      color='steelblue')

    def autolabel(rects):
        """
        Attach a text label above each bar in *rects*,
        displaying its height. In side this function because
        it is only used here"""
        for rect in rects:
            font = {'size': 12}
            plt.rc('font', **font)
            height = rect.get_height()
            ax_7.annotate('{}'.format(height),
                          xy=(rect.get_x() + rect.get_width() / 2, height),
                          xytext=(0, 3),  # 3 points vertical offset
                          textcoords="offset points",
                          ha='center', va='bottom')
    autolabel(rects1)
    autolabel(rects2)
    autolabel(rects3)
    font = {'size': 16}
    plt.rc('font', **font)
    ax_7.set_ylabel('F1 Scores')
    ax_7.set_title('Scores By Group and Dataset')
    ax_7.set_xticks(x)
    ax_7.set_xticklabels(labels, rotation=45)
    ax_7.legend(loc='lower right')
    bbox_inches = 'tight'
    plt.tight_layout()


def main():
    """
    This function runs all of the plots I want to keep
    my IFEM clean
    Parameters
    ----------
    None
    Returns
    -------
    Boxplot of activities at all accelerations
    """
    font = {'size': 16}
    plt.rc('font', **font)
    df = pd.read_csv('data/merged_data_save.csv')
    plt.style.use('ggplot')
    fig, ax = plt.subplots(figsize=(10, 9))
    boxplots(df=df, fig=fig, ax=ax, acc_metric='X')
    fig2, ax2 = plt.subplots(figsize=(10, 9))
    boxplots(df=df, fig=fig2, ax=ax2, acc_metric='Y')
    fig3, ax3 = plt.subplots(figsize=(10, 9))
    boxplots(df=df, fig=fig3, ax=ax3, acc_metric='Z')
    fig4, ax4 = plt.subplots(figsize=(10, 9))
    boxplots(df=df, fig=fig4, ax=ax4, acc_metric='gyroX')
    fig5, ax5 = plt.subplots(figsize=(10, 9))
    boxplots(df=df, fig=fig5, ax=ax5, acc_metric='gyroY')
    fig6, ax6 = plt.subplots(figsize=(10, 9))
    boxplots(df=df, fig=fig6, ax=ax6, acc_metric='gyroZ')
    barplot()
    plt.show()


if __name__ == '__main__':
    main()
