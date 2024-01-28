def make_valley(arr):
    sorted_arr = sorted(arr, reverse=True)

    left_wing = sorted_arr[::2]
    right_wing = sorted_arr[1::2][::-1]

    valley_array = left_wing + right_wing

    return valley_array