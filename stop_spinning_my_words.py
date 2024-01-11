def spin_words(sentence):
    sentence_list = sentence.split(" ")
    adjusted_words = []

    for word in sentence_list:
        if len(word) > 4:
            word = word[::-1]
        adjusted_words.append(word)

    result = " ".join(adjusted_words)

    return result


print(spin_words('Hey wollef sroirraw'))