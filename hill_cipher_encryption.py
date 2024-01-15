def encrypt(text, key):
    alphabet_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6,
                     'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13,
                     'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20,
                     'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
    the_text = [alphabet_dict[i.lower()] for i in text.strip(" ") if i.isalpha()]
    text_matrix = []
    key_matrix = [[alphabet_dict[key[0]], alphabet_dict[key[1]]], [alphabet_dict[key[2]], alphabet_dict[key[3]]]]
    result = ''

    if len(the_text) % 2 != 0:
        the_text.append(25)

    current_matrix = []

    for i in range(len(the_text)):
        current_matrix.append(the_text[i])

        if i % 2 != 0:
            text_matrix.append(current_matrix)
            current_matrix = []


    for pair in range(len(text_matrix)):
        text_matrix[pair] = [(text_matrix[pair][0] * key_matrix[0][0]) + (text_matrix[pair][1] * key_matrix[0][1]),
                (text_matrix[pair][0] * key_matrix[1][0]) + (text_matrix[pair][1] * key_matrix[1][1])]

        text_matrix[pair] = [text_matrix[pair][0] % 26, text_matrix[pair][1] % 26]

    for pair in text_matrix:
        for key, value in alphabet_dict.items():
            if pair[0] == value:
                result += key.upper()
                break

        for key, value in alphabet_dict.items():
            if pair[1] == value:
                result += key.upper()
                break

    return result


print(encrypt('Five + Seven = Twelve', 'math'))
print(encrypt('Hi', 'cats'))