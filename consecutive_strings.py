def longest_consec(strarr, k):
    if len(strarr) == 0 or len(strarr) < k or k == 0:
        return ""

    longest = ""

    for i in range(len(strarr)):
        current = ""
        for j in range(k):
            if i + j < len(strarr):
                current += strarr[i + j]

        if len(longest) < len(current):
            longest = current

    return longest
