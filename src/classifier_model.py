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
    X = df.drop(columns=['activitiy','Participant'],axis=1)
    y = df['activitiy']
    if random_forest:
        y = pd.get_dummies(y)
    return X,y
    
def split_data_standard(random_forest=True):
    X,y = prep_data(random_forest)
    (X_train, 
     X_test, 
     y_train, 
     y_test) = train_test_split(X, y, test_size=0.33, random_state=42)
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
