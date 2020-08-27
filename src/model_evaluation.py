from classifier_model import read_data, prep_data
import pickle
import time
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt


def select_model(data_set_bool):
    """
    Loads the model that coresponds to the correct
    training data
    Parameters
    ----------
    data_set_bool -> Boolean
    True False or None
    Returns
    -------
    Model trained on specific data
    """
    if data_set_bool:
        file_name = 'models/spectral_trained_model.sav'
        infile = open(file_name, 'rb')
        model = pickle.load(infile)
        return model
    elif data_set_bool is None:
        file_name = 'models/combined_training_sets.sav'
        infile = open(file_name, 'rb')
        model = pickle.load(infile)
        return model
    else:
        file_name = 'models/stats_trained_model.sav'
        infile = open(file_name, 'rb')
        model = pickle.load(infile)
        return model


def evaluate_model(data_set_bool):
    """
    Evaluates the pickled model on the holdout dataset
    Parameters
    ----------
    data_set_bool -> Boolean
    True False or None
    Returns
    -------
    results of model perfomance
    """
    (_, X_test, _, y_test) = prep_data(True, data_set_bool)
    model = select_model(data_set_bool)
    result = model.score(X_test, y_test)
    return result


def get_avg_runtime(data_set_bool):
    """
    Evaluates the average runtime of a model
    ----------
    data_set_bool -> Boolean
    True False or None
    Returns
    -------
    list of times it that it took the model
    """
    list_of_times = []
    for i in range(15):
        start = time.time()
        evaluate_model(data_set_bool)
        end = time.time()
        list_of_times.append(end-start)
    start = end = 0
    return list_of_times


def main():
    list_of_stat_times = get_avg_runtime(False)
    list_of_spec_times = get_avg_runtime(True)
    list_of_combined = get_avg_runtime(None)
    return (np.mean(list_of_stat_times),
            np.mean(list_of_spec_times),
            np.mean(list_of_combined))


if __name__ == '__main__':
    print(main())
