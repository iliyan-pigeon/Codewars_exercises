def generate_hashtag(data):
    data = data.split(" ")
    result = []

    for word in data:
        result.append(word.capitalize())

    result = "".join(result)

    if len(result) > 140 or len(result) < 1:
        return False
    else:
        return "#" + result
