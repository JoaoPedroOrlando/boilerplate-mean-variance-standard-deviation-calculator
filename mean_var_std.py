from array import ArrayType
import numpy as np

def check_list_length(list_to_check):
    length = len(list_to_check)
    if length != 9:
        raise ValueError("List must contain nine numbers.")

def sum_axis(np_arr: ArrayType, axis_num: int):
    return np.sum(np_arr, axis=axis_num)

def max_values(np_arr: ArrayType, axis_num: int):
    return np.max(np_arr, axis=axis_num)

def min_values(np_arr: ArrayType, axis_num: int):
    return np.min(np_arr, axis=axis_num)

def mean_values(np_arr: ArrayType, axis_num: int):
    return np.mean(np_arr, axis=axis_num)

def variance(np_arr: ArrayType, axis_num: int):
    return np.var(np_arr, axis=axis_num)

def deviation(np_arr: ArrayType, axis_num: int):
    return np.std(np_arr, axis=axis_num)

def calculate(list):
    # Check list length
    check_list_length(list)
    # Split the number into three arrays
    arr1 = list[0:3]
    arr2 = list[3:6]
    arr3 = list[6:9]
    ma = np.array([arr1, arr2, arr3])
    flatten_arr = np.array(list)

    calculations = {
        'mean': [
            mean_values(ma, 0).tolist(),
            mean_values(ma, 1).tolist(),
            mean_values(flatten_arr, 0)
        ],
        'variance': [
            variance(ma, 0).tolist(),
            variance(ma, 1).tolist(),
            variance(flatten_arr, 0)
        ],
        'standard deviation': [
            deviation(ma, 0).tolist(),
            deviation(ma, 1).tolist(),
            deviation(flatten_arr, 0)
        ],
        'max': [
            max_values(ma, 0).tolist(),
            max_values(ma, 1).tolist(),
            max_values(flatten_arr, 0)
        ],
        'min': [
            min_values(ma, 0).tolist(),
            min_values(ma, 1).tolist(),
            min_values(flatten_arr, 0)
        ],
        'sum': [
            sum_axis(ma, 0).tolist(),
            sum_axis(ma, 1).tolist(),
            sum_axis(flatten_arr, 0)
        ]
    }

    return calculations