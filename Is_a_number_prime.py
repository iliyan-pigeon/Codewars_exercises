from math import sqrt


def is_prime(num):
    result = True

    if num <= 1:
        result = False

    for n in range(2, sqrt(num)):
        if sqrt(num) % n == 0:
            result = False
            break

    return result
