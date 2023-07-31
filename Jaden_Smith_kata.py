def to_jaden_case(string):
    reformed_string = ''
    ch_counter = 0
    previous_character = ''

    for ch in string:
        if ch_counter == 0:
            reformed_string += ch.upper()
            ch_counter += 1
        elif previous_character == " ":
            reformed_string += ch.upper()
        elif previous_character != " " and ch.isupper():
            reformed_string += ch.lower()
        else:
            reformed_string += ch

        previous_character = ch

    return reformed_string


print(to_jaden_case("most trees are blue"))
