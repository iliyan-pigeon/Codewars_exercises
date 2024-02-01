def delta(values, n):
    values_list = [value for value in values]
    results = []

    for i in range(n):
        for value in range(1, len(values_list)):
            current_result = values_list[value] - values_list[value-1]
            results.append(current_result)

        values_list = results
        results = []

    return values_list


print(delta([1,2,3,4,5,6], 1))
print(delta([3, 3, -5, 77], 2))