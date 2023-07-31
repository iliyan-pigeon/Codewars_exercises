def score(dice):
    total_points = 0

    if 1 in dice:
        if dice.count(1) == 3:
            total_points += 1000
        elif dice.count(1) < 3:
            total_points += (dice.count(1) * 100)
        elif dice.count(1) > 3:
            total_points += 1000
            total_points += ((dice.count(1) - 3) * 100)

    if dice.count(2) >= 3:
        total_points += 200

    if dice.count(3) >= 3:
        total_points += 300

    if dice.count(4) >= 3:
        total_points += 400

    if 5 in dice:
        if dice.count(5) == 3:
            total_points += 500
        elif dice.count(5) < 3:
            total_points += (dice.count(5) * 50)
        elif dice.count(5) > 3:
            total_points += 500
            total_points += ((dice.count(5) - 3) * 50)

    if dice.count(6) >= 3:
        total_points += 600

    return total_points