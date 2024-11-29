from math import log10

def count(n):
    return sum(log10(x) for x in range(1, n + 1)).__ceil__()
  
