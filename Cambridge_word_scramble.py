def mix_words(string):
    is_string = isinstance(string, str)

    if not is_string:
        return "undefined"

    words = list(string)
    current_word = ""
    sentence = []
    counter = 1

    for symbol in words:
        if symbol.isalpha():
            current_word += symbol
        else:
            if len(current_word) <= 3:
                if current_word:
                    sentence.append(current_word)
                    current_word = ""
                sentence.append(symbol)
            else:
                first_letter = current_word[0]
                last_letter = current_word[-1]
                current_word = list(current_word[1:-1])
                word_set = set()
                second_set = set()
                for item in current_word:
                    if item in word_set:
                        second_set.add(item)
                    word_set.add(item)
                sentence.append(f"{first_letter}{''.join(word_set)}{''.join(second_set)}{last_letter}")
                current_word = ""
                sentence.append(symbol)

        if counter == len(words) and symbol.isalpha():
            if len(current_word) <= 3:
                if current_word:
                    sentence.append(current_word)
                    current_word = ""
            else:
                first_letter = current_word[0]
                last_letter = current_word[-1]
                current_word = list(current_word[1:-1])
                word_set = set()
                second_set = set()
                for item in current_word:
                    if item in word_set:
                        second_set.add(item)
                    word_set.add(item)
                sentence.append(f"{first_letter}{''.join(word_set)}{''.join(second_set)}{last_letter}")
                current_word = ""

        counter += 1

    return "".join(sentence)


print(mix_words("unSOMhYLVTXrqWoKjEQtsDlzvmgHfAawyePkidNZBxpcCIFJURGb"))