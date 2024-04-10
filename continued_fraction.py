def continued_fraction(numerator, denominator):
    if numerator == 0:
        return []

    result = []
    while denominator != 0:
        result.append(numerator // denominator)
        numerator, denominator = denominator, numerator % denominator

    return result


the_numerator = 311
the_denominator = 144
the_result = continued_fraction(the_numerator, the_denominator)
print(the_result)  # Output: [2, 6, 3, 1, 5]