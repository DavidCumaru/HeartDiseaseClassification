from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from datetime import datetime
from loguru import logger

"""
Implementing a decorator called 'train_time' that can be applied to a function to measure the execution time of the decorated function. The decorator is used to measure the training time of a machine learning model.

Measuring the training time of machine learning models is essential in the field of data to optimize resources, compare models and configurations, plan resources, optimize performance, and ensure the transparency and reproducibility of results. This helps improve the efficiency and quality of data modeling processes.
"""

def train_time(f):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        print()
        clf, best_params = f(model=kwargs["model"], param_grid=kwargs["param_grid"], x_train=kwargs["x_train"], y_train=kwargs["y_train"])
        return datetime.now() - start, clf, best_params

    return wrapper

@train_time
def train_model(model, param_grid, x_train, y_train):
    grid_search = GridSearchCV(model, param_grid, cv=5, n_jobs=-1)
    grid_search.fit(x_train, y_train)
    best_params = grid_search.best_params_
    return grid_search.best_estimator_, best_params


def calculate_accuracy(model, y_test, x_test):
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy