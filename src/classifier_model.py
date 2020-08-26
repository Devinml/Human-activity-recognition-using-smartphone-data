from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import multilabel_confusion_matrix
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.linear_model import LogisticRegressionCV, LogisticRegression
import numpy as np


def read_data(spectrum):
    """
    This function returns a dataframe based off
    wich data set that I want to evaluate
    Parameters
    ----------
    method of data analysis that want to train a model on
    Boolean

    Returns
    -------
    Pandas DataFrame
    """
    if spectrum:
        fp = 'data/calculated_data_save.csv'
        return pd.read_csv(fp)
    elif spectrum is None:
        fp = 'data/joined_calc_data.csv'
        return pd.read_csv(fp)
    else:
        fp = 'data/stats_method.csv'
        return pd.read_csv(fp)


def prep_data(random_forest, spectrum):
    """
    Specify the model you want and the what data set
    you want to use and this function returns a data set
    that is prepped for that function
    Parmeters
    ---------
    random_forest = Boolean
    spectrum = Booolean
    Returns
    -------
    split data in DataFrames
    X_train, X_test, y_train, y_test
    """
    df = read_data(spectrum)
    df_test = df[(df['Participant'] == 1) |
                 (df['Participant'] == 6) |
                 (df['Participant'] == 13) |
                 (df['Participant'] == 9) |
                 (df['Participant'] == 29) |
                 (df['Participant'] == 27) |
                 (df['Participant'] == 14) |
                 (df['Participant'] == 11) |
                 (df['Participant'] == 17) |
                 (df['Participant'] == 23)]
    df_train = df[(df['Participant'] != 1) &
                  (df['Participant'] != 6) &
                  (df['Participant'] != 13) &
                  (df['Participant'] != 9) &
                  (df['Participant'] != 29) &
                  (df['Participant'] != 27) &
                  (df['Participant'] != 14) &
                  (df['Participant'] != 11) &
                  (df['Participant'] != 17) &
                  (df['Participant'] != 23)]
    X_train = df_train.drop(columns=['activitiy', 'Participant'], axis=1)
    X_test = df_test.drop(columns=['activitiy', 'Participant'], axis=1)
    if random_forest:
        y_train = df_train['activitiy']
        y_test = df_test['activitiy']
        y_train = pd.get_dummies(y_train)
        y_test = pd.get_dummies(y_test)
    else:
        y_train = df_train['activitiy']
        y_test = df_test['activitiy']
    return X_train, X_test, y_train, y_test


def split_data_standard(random_forest, spectrum):
    """
    Splits the data and scales the data
    Parameters
    ---------
    random_forest = Boolean
    spectrum = Booolean
    Returns
    -------
    scaled data
    X_train, X_test, y_train, y_test
    """
    X_train, X_test, y_train, y_test = prep_data(random_forest, spectrum)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    return X_train, X_test, y_train, y_test


def random_forest(random_forest, spectrum):
    """
    performs a random foresst classifier on the prpeed data
    Parameters
    ----------
    random_forest = Boolean
    spectrum = Boolean
    Returns
    -------
    predictions on test set, y_test, and model
    """
    clf = RandomForestClassifier(random_state=0)
    (X_train,
     X_test,
     y_train,
     y_test) = prep_data(random_forest, spectrum)
    clf.fit(X_train, y_train)
    prediction = clf.predict(X_test)
    return prediction, y_test, clf


def logclassifier(random_forest, spectrum):
    """
    performs a log classifier on the prpeed data
    Parameters
    ----------
    random_forest = Boolean
    spectrum = Boolean
    Returns
    -------
    predictions on test set, y_test, and model
    """
    clf = LogisticRegression(max_iter=1000)
    (X_train,
     X_test,
     y_train,
     y_test) = split_data_standard(random_forest, spectrum)
    clf.fit(X_train, y_train)
    prediction = clf.predict(X_test)
    return prediction, y_test, clf


if __name__ == '__main__':
    preds, y_test_rf, rf = random_forest(True, None)
    prediction, y_test_log, clf = logclassifier(False, None)
    print("Random Forest")
    print(classification_report(y_test_rf, preds))
    print('Log Classification')
    print(classification_report(y_test_log, prediction))
    print('Log Coef')
    print(clf.coef_.shape)
    print(clf.classes_)
    print(confusion_matrix(y_test_log, prediction))
    results = pd.DataFrame(classification_report(y_test_rf,
                                                 preds,
                                                 output_dict=True))
    print(results.T.to_markdown())
