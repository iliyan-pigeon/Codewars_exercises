def calculate_sum(n, k):
    s = 0
    while n > 0:
        s += n * (n + 1) // 2
        n //= k
        s -= k * n * (n + 1) // 2
    return s
