"""linear_regression
This module is designed to encapsulate common functionality used
by data scientist in the context of machine learning with Linear Regression Algorithms
"""
import numpy as np
import matplotlib.pyplot as plot
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
from statsmodels.formula.api import ols

def split_data(x, y, test_size = 0.30, random_state = 50):
    """split_dataset
    This function splits the dataset into training and test data.
    Returns:
        x_train: array(), 
        x_test: array(),
        y_train: array(),
        y_test: array()
    """
    #
    # Break data up into training and test data:
    #
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size, random_state=random_state)
   
    return x_train, x_test, y_train, y_test
   
def residual_plot(xlabel, ylabel, data):
    """residual_plot
    This function returns a residual plot summary.
    Returns:
        model: object
    """
    #
    #
    #
    model = ols("{xlabel} ~ {ylabel}".format(xlabel=xlabel, ylabel=ylabel), data=data).fit()
    return model

def mean_abs_err(y, _pred):
    """mean_abs_err
    This function returns the mean_absolute_error.
    Returns:
        model: object
    """
    mae = mean_absolute_error(y, _pred)

    return mae