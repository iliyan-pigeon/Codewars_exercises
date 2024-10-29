def distribution_of_candy(candies):
    def distribute_once(candies):
        n = len(candies)
        new_candies = [0] * n
        for i in range(n):
            if candies[i] % 2 != 0:
                candies[i] += 1

            half_candies = candies[i] // 2
            new_candies[i] -= half_candies
            new_candies[(i + 1) % n] += half_candies

        for i in range(n):
            candies[i] += new_candies[i]

        return candies
    distributions = 0

    while len(set(candies)) != 1:
        candies = distribute_once(candies)
        distributions += 1

    return [distributions, candies[0]]
  
