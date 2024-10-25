def reverse_number(n, b):
    binary = []
    sum = 0
    if b == 1:
        return n
    else:
        while n >= 1:
            binary.append(n % b)
            n = n // b
            a = len(binary) - 1
        for i in binary:
            sum += (i*(b**a))
            a -= 1
            continue
    return sum
  
