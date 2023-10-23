import itertools

def get_pins(observed):
    adjacent_digits = {
        '0': ['0', '8'],
        '1': ['1', '2', '4'],
        '2': ['1', '2', '3', '5'],
        '3': ['2', '3', '6'],
        '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '8'],
        '8': ['5', '7', '8', '9', '0'],
        '9': ['6', '8', '9']
    }

    variations = ['']

    for digit in observed:
        possibilities = adjacent_digits[digit]
        variations = [prefix + possibility for prefix in variations for possibility in possibilities]

    return variations


observed_PIN = '1357'
variations = get_pins(observed_PIN)
print(variations)