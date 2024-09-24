def cuckoo_clock(time, n):
    h, m = map(int, time.split(':'))
    if m % 15 == 0:
        if m == 0:
            h -= 1
            m = 60
        m -= 1
    m //= 15
    while n > 0:
        if m < 3:
            m += 1
            n -= 1
        else:
            m = 0
            h += 1
            h = (h-1) % 12 + 1
            n -= h
    return f'{h:02}:{m*15:02}'
  
