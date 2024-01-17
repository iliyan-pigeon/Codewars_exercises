def regression_line(x, y):
    n = len(x)

    sum_x = sum(x)
    sum_y = sum(y)
    sum_x_squared = sum(xi**2 for xi in x)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))

    b = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)
    a = (sum_y - b * sum_x) / n

    a = round(a, 4)
    b = round(b, 4)

    return a, b


print(regression_line([25,30,35,40,45,50], [78,70,65,58,48,42]))
print(regression_line([56,42,72,36,63,47,55,49,38,42,68,60], [147,125,160,118,149,128,150,145,115,140,152,155]))