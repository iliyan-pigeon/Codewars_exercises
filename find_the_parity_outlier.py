def find_outlier(integers):
    result = 0
    odd_numbers = [number for number in integers if number % 2 != 0]
    even_numbers = [number for number in integers if number % 2 == 0]

    if len(odd_numbers) == 1:
        result = odd_numbers[0]
    else:
        result = even_numbers[0]

    return result