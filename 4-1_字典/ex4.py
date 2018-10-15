sentence = "Assassin's Creed: Odyssey is one of my favorite AC games. Well done, Ubisoft."


def word_count(sentence):
    dict = {}
    print(sentence)
    for letter in sentence:
        letter = letter.lower()
        dict.setdefault(letter, 0)
        dict[letter] += 1

    for key, value in dict.items():
        print("{}: {}".format(key, value))

word_count(sentence)
