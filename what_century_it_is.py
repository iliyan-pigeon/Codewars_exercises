def what_century(year):
    first_two_digits = year[:2]
    last_three_digits = year[1:]

    century = ""

    if last_three_digits == "000":
        century = first_two_digits
    else:
        century = str(int(first_two_digits)+1)

    first_digit = century[0]
    second_digit = century[1]

    if second_digit == "0":
        century += "th"
    elif second_digit == "1":
        if first_digit == "1":
            century += "th"
        else:    
            century += "st"
    elif second_digit == "2":
        century += "nd"
    elif second_digit in "3":
        if first_digit == "1":
            century += "th"
        else:
            century += "rd"
    elif second_digit in "3":
        century += "rd"
    elif second_digit in "4":
        century += "th"
    elif second_digit in "5":
        century += "th"
    elif second_digit in "6":
        century += "st"
    elif second_digit in "7":
        century += "th"
    elif second_digit in "8":
        century += "th"
    elif second_digit in "9":
        century += "th"

    return century
