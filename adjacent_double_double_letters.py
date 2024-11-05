def adjacent_double_double_letters(word):
    return any(a == b and c == d for a,b,c,d in zip(word, word[1:], word[2:], word[3:]))
  
