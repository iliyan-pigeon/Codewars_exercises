def zeros(n):
    zeros_amount = 0
    i = 5
    while n//i > 0:
        zeros_amount += n//i
        i *= 5

    return zeros_amount


print(zeros(100))
