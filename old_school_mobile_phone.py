def search(dct, char):
    for key, value in dct.items():
        if char in value: return [key, value.index(char) + 1]


def send_message(message):
    dct = {
        "1": ['.', ',', '?', '!', '1'],
        "2": ['a', 'b', 'c', '2'],
        "3": ['d', 'e', 'f', '3'],
        "4": ['g', 'h', 'i', '4'],
        "5": ['j', 'k', 'l', '5'],
        "6": ['m', 'n', 'o', '6'],
        "7": ['p', 'q', 'r', 's', '7'],
        "8": ['t', 'u', 'v', '8'],
        "9": ['w', 'x', 'y', 'z', '9'],
        "*": ["'", '-', '+', '=', '*'],
        "0": [" ", '0'],
        "#": ['#']
    }

    result = ""
    _case = False
    prev = ""
    for i in message:
        index = search(dct, i.lower())
        if i.isdigit() or i == "*" or i == "#":
            if index[0] == prev and (_case != i.islower() or _case == i.isupper()):
                result += " "
            result += f"{index[0]}-"
            prev = ""
            continue
        if index[0] == prev and (_case != i.islower() or _case == i.isupper()):
            result += " "
        prev = index[0]
        if (i.isupper() and _case == False) or (i.islower() and _case == True):
            _case = not _case
            result += "#"

        result += index[0] * index[1]
    print(message)
    print(result)
    return result
