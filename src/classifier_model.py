from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import multilabel_confusion_matrix
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegressionCV, LogisticRegression


def read_data(fp='data/calculated_data.csv'):
    return pd.read_csv(fp)


def prep_data(random_forest=True):
    df = read_data()
    df_test= df[(df['Participant'] == 1)|
                (df['Participant'] == 6)|
                (df['Participant'] == 13)|
                (df['Participant'] == 9)|
                (df['Participant'] == 29)|
                (df['Participant'] == 27)|
                (df['Participant'] == 14)|
                (df['Participant'] == 11)|
                (df['Participant'] == 17)|
                (df['Participant'] == 23)]
    df_train = df[(df['Participant'] != 1)&
                  (df['Participant'] != 6)&
                  (df['Participant'] != 13)&
                  (df['Participant'] != 9)&
                  (df['Participant'] != 29)&
                  (df['Participant'] != 27)&
                  (df['Participant'] != 14)&
                  (df['Participant'] != 11)&
                  (df['Participant'] != 17)&
                  (df['Participant'] != 23)]
    X_train = df_train.drop(columns=['activitiy','Participant'],axis=1)
    X_test = df_test.drop(columns=['activitiy','Participant'],axis=1)
    
    if random_forest:
        y_train = df_train['activitiy']
        y_test = df_test['activitiy']
        y_train = pd.get_dummies(y_train)
        y_test = pd.get_dummies(y_test)
    else:
        y_train = df_train['activitiy']
        y_test = df_test['activitiy']
    return X_train, X_test, y_train, y_test


def split_data_standard(random_forest=True):
    X_train, X_test, y_train, y_test = prep_data(random_forest=True)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    return X_train, X_test, y_train, y_test


def random_forest():
    clf = RandomForestClassifier(random_state=0)
    (X_train,
     X_test,
     y_train,
     y_test) = split_data_standard()
    clf.fit(X_train,y_train)
    prediction = clf.predict(X_test)
    # print(multilabel_confusion_matrix(y_test, prediction))
    print(classification_report(y_test,prediction))


def logclassifier():
    clf = LogisticRegression()
    (X_train,
     X_test,
     y_train,
     y_test) = split_data_standard(random_forest=False)
    clf.fit(X_train, y_train)
    prediction = clf.predict(X_test)
    print(classification_report(y_test,prediction))


if __name__ == '__main__':
    random_forest()
    logclassifier()
