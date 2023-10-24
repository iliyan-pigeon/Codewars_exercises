def solve_runes(runes):
    unknown_digit = -1
    runes_copy = runes

    for i in range(10):
        if str(i) not in runes_copy:
            while "?" in runes_copy:
                index = runes_copy.index("?")
                runes_copy = runes_copy[:index] + str(i) + runes_copy[index+1:]

            first_number = []
            operator = ""
            second_number = []
            numbers, result = runes_copy.split("=")
            numbers = list(numbers)
            result = list(result)

            for j in range(len(numbers)-1):
                if numbers[j] == "-" and j == 0:
                    continue
                if numbers[j] == "-" or numbers[j] == "+" or numbers[j] == "*":
                    operator = numbers[j]
                    first_number = numbers[:j]
                    second_number = numbers[j+1:]
                    break

            if first_number[0] == "0" and len(first_number) > 1 or \
                    second_number[0] == "0" and len(second_number) > 1:
                runes_copy = runes
                continue

            if result[0] == "0" and len(result) > 1:
                runes_copy = runes
                continue

            if operator == "+":
                if int("".join(first_number)) + int("".join(second_number)) == int("".join(result)):
                    unknown_digit = i
                    break
            elif operator == "-":
                if int("".join(first_number)) - int("".join(second_number)) == int("".join(result)):
                    unknown_digit = i
                    break
            elif operator == "*":
                if int("".join(first_number)) * int("".join(second_number)) == int("".join(result)):
                    unknown_digit = i
                    break
            runes_copy = runes

    return unknown_digit



print(solve_runes("?*11=??"))