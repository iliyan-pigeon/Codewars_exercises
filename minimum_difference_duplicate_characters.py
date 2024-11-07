def min_repeating_character_difference(text):
    for i in range(1, len(text)):
        for a, b in zip(text, text[i:]):
            if a == b:
                return i, a
              
