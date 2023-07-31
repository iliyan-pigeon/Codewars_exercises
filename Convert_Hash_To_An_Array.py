# First Option
def convert_hash_to_array(the_hash):
    the_list = []
    for key, value in the_hash.items():
        current_list = [key, value]
        the_list.append(current_list)

    the_list = sorted(the_list, key=lambda x: x[0])
    return the_list


# Second Option
# def convert_hash_to_array(hash):
#     return sorted(map(list, hash.items()))


# Third Option
# def convert_hash_to_array(hash):
#     return sorted([k, v] for k, v in hash.items())
