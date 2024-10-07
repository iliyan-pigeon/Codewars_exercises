from itertools import zip_longest


def fill(arr, method=0):
    modified_array = []
    if method == -1:
        start = 0
        for i in range(len(arr)):
            if arr[i] is not None:
                modified_array.extend([arr[i] for j in arr[start:i+1]])
                start = i+1

        if len(modified_array) < len(arr):
            difference = len(arr) - len(modified_array)

            for i in range(difference):
                modified_array.append(None)
    elif method == 0:
        for i,item in enumerate(arr):
            if item is None:
                for pair in zip_longest(arr[i::-1], arr[i::]):
                    if pair != (None,None):
                        item = min(n for n in pair if n is not None)
                        break
            modified_array.append(item)
    elif method == 1:
        fill_value = None
        for item in arr[::method]:
            if item is not None:
                fill_value = item
            modified_array.append(fill_value)

    return modified_array
