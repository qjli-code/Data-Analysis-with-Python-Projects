import numpy as np


def calculate(list):
    """
    Function that uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.

    input:  list containing 9 digits
    """
    # convert input list into 3x3 np array
    try:
        numbers = np.array(list).reshape(3, 3)
    except:
        raise ValueError('List must contain nine numbers.')
    # initialize necessary variables
    calculations = dict()
    my_mean = []
    my_var = []
    my_std = []
    my_max = []
    my_min = []
    my_sum = []
    # calculate mean, var, std, max, min, sum
    for i in range(3):
        if i == 2:
            axis = None
        else:
            axis = i
        my_mean.append(np.mean(numbers, axis=axis).tolist())
        my_var.append(np.var(numbers, axis=axis).tolist())
        my_std.append(np.std(numbers, axis=axis).tolist())
        my_max.append(np.max(numbers, axis=axis).tolist())
        my_min.append(np.min(numbers, axis=axis).tolist())
        my_sum.append(np.sum(numbers, axis=axis).tolist())
    # combine results into the calculations dict
    results = [my_mean, my_var, my_std, my_max, my_min, my_sum]
    keys = ['mean', 'variance', 'standard deviation', 'max', 'min', 'sum']
    for k, r in zip(keys, results):
        calculations[k] = r
    return calculations
