def exp_sum(n):
    memo = {}

    def count_partitions(target, max_num):
        if target == 0:
            return 1
        if target < 0 or max_num == 0:
            return 0
        if (target, max_num) in memo:
            return memo[(target, max_num)]

        include = count_partitions(target - max_num, max_num)
        exclude = count_partitions(target, max_num - 1)

        memo[(target, max_num)] = include + exclude
        return memo[(target, max_num)]

    return count_partitions(n, n)


