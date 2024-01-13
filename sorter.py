def sorter(textbooks):
    # Sort the textbooks (case-insensitive)
    sorted_textbooks = sorted(textbooks, key=lambda x: x.lower())
    return sorted_textbooks