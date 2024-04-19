import numpy as np

# root mean squared logarithmic error 
def rmsle(y:np.ndarray, y_pred:np.ndarray)->float:
    '''
    Root Mean Squared Logarithmic Error
    return -> this function return the root mean squared logarithmic error
    param -> y:np.ndarray actual value of the labels
             y_pred:np.ndarray predicted value of labels
    '''
    return np.sqrt(np.mean(np.power(np.log1p(y_pred) - np.log1p(y), 2)))