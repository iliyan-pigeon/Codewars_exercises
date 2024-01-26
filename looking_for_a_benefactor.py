import math


def new_avg(arr, newavg):
    current_sum = sum(arr)
    current_length = len(arr)
    target_sum = newavg * (current_length + 1)
    difference = target_sum - current_sum

    if difference <= 0:
        raise ValueError

    return math.ceil(difference)