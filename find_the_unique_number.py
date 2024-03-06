from collections import Counter

def find_uniq(arr):
    counts = Counter(arr)

    unique_element = [element for element, count in counts.items() if count == 1][0]

    return unique_element