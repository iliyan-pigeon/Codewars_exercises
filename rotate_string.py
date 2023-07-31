def rotate(str_):
    if str_ == "":
        return []
    elif len(str_) == 1:
        return [str_]

    result = []

    for i in range(len(str_)):
        str_ = str_[1:] + str_[0]
        result.append(str_)

    return result


print(rotate("abc"))