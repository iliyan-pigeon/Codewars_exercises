
import math

def count_ones_1(left, right):
    result = 0

    while right >= left:
        single_result = list(str(bin(right))).count("1")
        result += count_ones_1(left, right-1)

    return result


print(count_ones_1(4,7))


def count_ones_2(left, right):
    if right < left:
        return 0

    single_result = bin(right).count("1")
    return single_result + count_ones_2(left, right - 1)

# Example usage:
print(count_ones_2(4, 7))


def count(n):
    if n is 0: return 0
    x = int(math.log(n, 2))
    return x * 2 ** (x - 1) + n - 2 ** x + 1 + count(n - 2 ** x)

def count_ones_3(left, right):
    return count(right) - count(left - 1)