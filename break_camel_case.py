def solution(s):
    result = ""

    for symbol in s:
        if symbol.isupper():
            result += " "
        result += symbol

    return result
