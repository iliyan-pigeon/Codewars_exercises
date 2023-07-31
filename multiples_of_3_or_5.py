def solution(number):
    all_multiples = []

    for number in range(number-1, 0, -1):
        if number % 3 == 0 and number not in all_multiples:
            all_multiples.append(number)

        if number % 5 == 0 and number not in all_multiples:
            all_multiples.append(number)

    result = sum(all_multiples)
    if result < 0:
        result = 0
    return result


print(solution(6))
