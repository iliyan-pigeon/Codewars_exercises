def late_clock(*a):
    for h in range(23, -1, -1):
        for m in range(59, -1, -1):
            x = f'{h:02}'
            y = f'{m:02}'
            s = list(map(int,list(x + y)))
            if sorted(s)==sorted(a):
                return f'{x}:{y}'


print(late_clock(9, 1, 3, 8))