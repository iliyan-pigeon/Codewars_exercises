def matryoshka(lst):
    xs = sorted((min(x), max(x)) for x in lst)
    return all(a < c and b > d for (a, b), (c, d) in zip(xs, xs[1:]))
  
