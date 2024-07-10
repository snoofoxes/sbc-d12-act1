word = []
puted = input("Input a word: ")

def words():
    sep = ''
    for w in puted:
        if w == ' ':
            word.append(sep)
            sep = ''
        else:
            sep += w
    if sep:
        word.append(sep)
words()
print(word)