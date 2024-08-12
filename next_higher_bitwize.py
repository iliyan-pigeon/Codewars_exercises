def next_higher(n):
    number_bits = bin(n).replace("b", "")
    number_bits_zeros = len([i for i in number_bits if i == "0"])
    number_bits_ones = len([i for i in number_bits if i == "1"])

    next_number = n
    while True:
        next_number += 1
        next_bits = bin(next_number)[2:].replace("b", "")
        next_bits_zeros = len([i for i in next_bits if i == "0"])
        next_bits_ones = len([i for i in next_bits if i == "1"])

        if number_bits_zeros == next_bits_zeros and number_bits_ones == next_bits_ones:
            return next_number
