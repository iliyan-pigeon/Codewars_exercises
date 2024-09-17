def digital_root(n):

    the_number = str(n)

    while len(the_number) > 1:
        number = 0
        for i in the_number:
            number += int(i)

        the_number = str(number)

    return int(the_number)
