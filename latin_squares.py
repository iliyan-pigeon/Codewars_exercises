def make_latin_square(n):
    return [[(i+j)%n+1 for i in range(n)] for j in range(n)]
