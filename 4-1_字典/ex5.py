sentence = "Assassin's Creed: Odyssey is one of my favorite AC games. Well done, Ubisoft."
dict = {}

for letter in sentence:
    dict.setdefault(letter, 0)
    dict[letter] += 1

for key, value in dict.items():
    print("{}: {}".format(key, value))
