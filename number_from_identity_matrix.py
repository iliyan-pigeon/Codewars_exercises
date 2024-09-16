def soln(n):
    binary_representation = []

    for i in range(n):
        for j in range(n):
            if i == j:
                binary_representation.append('1')
            else:
                binary_representation.append('0')

    binary_string = ''.join(binary_representation)

    decimal_value = int(binary_string, 2)

    return decimal_value
