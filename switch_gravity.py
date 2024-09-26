def switch_gravity(lst):
    return list(map(list, zip(*map(sorted, zip(*lst)))))[::-1]
