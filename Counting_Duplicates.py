def duplicate_count(text):
    detected_characters = []
    duplicates = []

    for ch in text:
        if ch.isalpha():
            ch = ch.lower()

        if ch in detected_characters:
            if ch not in duplicates:
                duplicates.append(ch)
        else:
            detected_characters.append(ch)

    return len(duplicates)

