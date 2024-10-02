def digitwise_addition(N, K):
    digits = [str(N).count(str(i)) for i in range(10)]

    for _ in range(K):
        digits = digits[9:] + digits[:9]
        digits[1] += digits[0]

    return sum(digits) % (10**9 + 7)
  
