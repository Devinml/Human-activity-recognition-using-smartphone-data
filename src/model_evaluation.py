from classifier_model import read_data, prep_data
import pickle
import time
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def select_model(data_set_bool):
    if data_set_bool:
        file_name = 'models/spectral_trained_model.sav'
        infile = open(file_name,'rb')
        model = pickle.load(infile)
        return model
    elif data_set_bool is None:
        file_name = 'models/combined_training_sets.sav'
        infile = open(file_name,'rb')
        model = pickle.load(infile)
        return model
    else:
        file_name = 'models/stats_trained_model.sav'
        infile = open(file_name,'rb')
        model = pickle.load(infile)
        return model


def evaluate_model(data_set_bool):
    (_, X_test, _, y_test) = prep_data(True, data_set_bool)
    model = select_model(data_set_bool)
    result = model.score(X_test, y_test)
    return result


def get_avg_runtime(data_set_bool):
    list_of_times = []
    for i in range(100):
        start = time.time()
        evaluate_model(data_set_bool)
        end = time.time()
        list_of_times.append(end-start)
    return list_of_times


def get_normal_of_time(list_of_times):
    mean = np.mean(list_of_times)
    sqrt_n = np.sqrt(len(list_of_times))
    std = np.std(list_of_times) / sqrt_n
    return stats.norm(loc=mean, scale=std)


def main():
    list_of_stat_times = get_avg_runtime(False)
    list_of_spec_times = get_avg_runtime(True)
    list_of_combined = get_avg_runtime(None)
    # Get the normal distributions of the times using CLT
    stat_times_norm = get_normal_of_time(list_of_stat_times)
    spec_times_norm = get_normal_of_time(list_of_spec_times)
    comb_times_norm = get_normal_of_time(list_of_combined)
    plt.style.use('ggplot')
    font = {'size'   : 16}
    plt.rc('font', **font)
    fig, ax = plt.subplots(figsize=(12, 5))
    x = np.linspace(.1,.16,1000)
    ax.plot(x,stat_times_norm.pdf(x),
            label='Stats Dataset',
            color='olivedrab')
    ax.plot(x,spec_times_norm.pdf(x),
            label='Spec Dataset',
            color='teal')
    ax.plot(x,comb_times_norm.pdf(x),
            label='Combined Dataset',
            color='sienna')
    ax.set_xlim(.11,.155)
    ax.legend()
    plt.title('Distribution of Mean Execution Time')
    plt.xlabel('Mean(execution time)')
    plt.ylabel('Probabilty(execution time)')
    plt.tight_layout()
    plt.savefig('exectution_times.png', dpi=500)

if __name__ == '__main__':
    main()