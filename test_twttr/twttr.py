def shorten(word):
    text = [s for s in word if s not in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']]
    new_text = ''.join(text)
    return new_text