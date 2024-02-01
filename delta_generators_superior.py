from itertools import pairwise

def delta(values: iter, n: int) -> iter:
    return delta((b - a for a, b in pairwise(values)), n - 1) if n > 0 else values