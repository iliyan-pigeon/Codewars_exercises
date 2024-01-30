def not_so_random(b, w):
    black_marbles = b
    white_marbles = w

    while True:
        if black_marbles > 0 and white_marbles > 0:
            white_marbles -= 1
        elif black_marbles > 1 and white_marbles == 0:
            black_marbles -= 2
            white_marbles += 1
        elif black_marbles == 0 and white_marbles > 1:
            white_marbles -= 1
        elif black_marbles == 1 and white_marbles == 0:
            return "Black"
        elif black_marbles == 0 and white_marbles == 1:
            return "White"
        else:
            return "Unsure"


print(not_so_random(1, 1))
print(not_so_random(6, 9))
print(not_so_random(11111, 22222))