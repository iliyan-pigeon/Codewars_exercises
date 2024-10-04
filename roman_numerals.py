def roman_fractions(integer, fraction=None):
    # Validate integer range
    if not (0 <= integer <= 5000):
        return "NaR"

    # Validate fraction range (if provided)
    if fraction is not None and not (0 <= fraction <= 11):
        return "NaR"

    # Handle case where integer is 0
    if integer == 0:
        if fraction is None or fraction == 0:
            return "N"  # 0 with no fraction or fraction 0 is "N"
        else:
            # Fraction without integer part (e.g. 0.3 as :.)
            fraction_symbols = [".", ":", ":.", "::", ":.:", "S", "S.", "S:", "S:.", "S::", "S:.:", "I"]
            return fraction_symbols[fraction - 1] if fraction > 0 else "N"

    # Roman numeral conversion (integer part)
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    
    roman_numeral = ''

    for i in range(len(val)):
        count = int(integer / val[i])
        roman_numeral += syb[i] * count
        integer -= val[i] * count

    # Handle fraction part (if any)
    if fraction and fraction > 0:
        fraction_symbols = [".", ":", ":.", "::", ":.:", "S", "S.", "S:", "S:.", "S::", "S:.:", "I"]
        roman_numeral += fraction_symbols[fraction - 1]

    return roman_numeral
