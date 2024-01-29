def dead_ant_count(ants):
    return max(ants.count('a'), ants.count('n'), ants.count('t')) - ants.count('ant')


print(dead_ant_count("aaaaannnntttt"))