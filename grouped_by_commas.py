def group_by_commas(n):
    if len(str(n)) <= 3:
        return str(n)

    result = []
    counter = 0

    for i in list(str(n))[::-1]:
        if counter == 3:
            result += ","
            result += i
            counter = 1
        else:
            result += i
            counter += 1

    return "".join(result[::-1])

# wtf solution
#def group_by_commas(n):
#    return '{:,}'.format(n)
