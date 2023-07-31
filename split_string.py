def solution(s):
    result = []

    while s:
        current_couple = ''

        for i in range(2):
            if s:
                current_couple += s[0]
                s = s[1:]
            else:
                break

        if len(current_couple) == 1:
            current_couple += "_"
        result.append(current_couple)

    return result
