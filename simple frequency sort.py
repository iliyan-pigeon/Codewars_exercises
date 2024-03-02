def solve(arr):
    my_dict = {}
    for i in arr:
        if i not in my_dict:
            my_dict[i] = 1
        else:
            my_dict[i] += 1
    my_list = sorted(my_dict.items(), key = lambda x: (-x[1], x[0]))
    my_result = []
    for a in my_list:
        my_result.extend([a[0]] * a[1])
    return my_result
