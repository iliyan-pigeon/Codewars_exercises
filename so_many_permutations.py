from itertools import permutations


def permutation(s):
    all_permutations = []

    for p in permutations(s):
        the_string = ""
        for i in p:
            the_string += i

        all_permutations.append(the_string)


    return all_permutations


permutation("abc")