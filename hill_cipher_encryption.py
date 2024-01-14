def encrypt(text, key):
    the_text = [i for i in text.strip(" ") if i.isalpha()]
    text_matrix = []
    key_matrix = [[key[0], key[1]], [key[2], key[3]]]


encrypt('Five + Seven = Twelve', 'math')