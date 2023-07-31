def snail(snail_map):
    snail_path = []
    path_finished = False
    row = 0
    upper_border = 0
    lower_border = len(snail_map) - 1
    right_border = len(snail_map[0]) - 1
    left_border = 0
    upper_lower_border = "upper"

    while not path_finished:
        if row == upper_border:
            for i in range(left_border, right_border + 1):
                snail_path.append(snail_map[row][i])

            if len(snail_path) > len(snail_map[0]):
                left_border += 1
                lower_border -= 1
                upper_lower_border = "upper"
            row += 1

        elif row == lower_border:
            for i in range(right_border, left_border - 1, -1):
                snail_path.append(snail_map[row][i])

            upper_lower_border = "lower"
            upper_border += 1
            right_border -= 1
            row -= 1


        elif upper_lower_border == "upper":
            snail_path.append(snail_map[row][right_border])
            row += 1

        elif upper_lower_border == "lower":
            snail_path.append((snail_map[row][left_border]))
            row -= 1

        if len(snail_path) == len(snail_map) * len(snail_map[0]):
            path_finished = True

    return snail_path


print(snail([[1, 2, 3, 4, 5],
             [6, 7, 8, 9, 10],
             [11, 12, 13, 14, 15],
             [16, 17, 18, 19, 20],
             [21, 22, 23, 24, 25]]))
