def next_bigger(n):
    digits = list(str(n))

    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1

    if i == -1:
        return -1  # No larger permutation is possible

    # Find the smallest digit to the right of digits[i] and larger than digits[i]
    j = len(digits) - 1
    while digits[j] <= digits[i]:
        j -= 1

    digits[i], digits[j] = digits[j], digits[i]

    digits[i + 1:] = sorted(digits[i + 1:])

    result = int(''.join(digits))
    return result

# Test cases
print(next_bigger(12))              # Output: 21
print(next_bigger(513))             # Output: 531
print(next_bigger(2017))            # Output: 2071
print(next_bigger(9))               # Output: -1
print(next_bigger(111))             # Output: -1
print(next_bigger(531))             # Output: -1
print(next_bigger(744714258621))