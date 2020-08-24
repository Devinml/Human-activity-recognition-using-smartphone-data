from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def perform_split(X,y):
    X_train, X_test, y_train, y_test = train_test_split(X, 
                                                        y, 
                                                        test_size=0.33, 
                                                        random_state=42)
    return (X_train, X_test, y_train, y_test)

def scale_data():
    pass