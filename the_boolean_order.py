def solve(values, operators):
    n = len(values)
    dp_true = [[0] * n for _ in range(n)]
    dp_false = [[0] * n for _ in range(n)]

    for i in range(n):
        dp_true[i][i] = 1 if values[i] == 't' else 0
        dp_false[i][i] = 1 if values[i] == 'f' else 0

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                if operators[k] == '&':
                    dp_true[i][j] += dp_true[i][k] * dp_true[k + 1][j]
                    dp_false[i][j] += dp_true[i][k] * dp_false[k + 1][j] + dp_false[i][k] * dp_true[k + 1][j] + dp_false[i][k] * dp_false[k + 1][j]
                elif operators[k] == '|':
                    dp_true[i][j] += dp_true[i][k] * dp_true[k + 1][j] + dp_true[i][k] * dp_false[k + 1][j] + dp_false[i][k] * dp_true[k + 1][j]
                    dp_false[i][j] += dp_false[i][k] * dp_false[k + 1][j]
                else:  # operators[k] == '^'
                    dp_true[i][j] += dp_true[i][k] * dp_false[k + 1][j] + dp_false[i][k] * dp_true[k + 1][j]
                    dp_false[i][j] += dp_true[i][k] * dp_true[k + 1][j] + dp_false[i][k] * dp_false[k + 1][j]

    return dp_true[0][n - 1]


print(solve("tft", "^&"))
print(solve("ttftff", "|&^&&"))