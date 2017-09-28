"""
>>> search(mississippi, i)
["1","4","7","10"]

>>> search1(mississippi, i)
["1","4","7","10"]

"""

#def search(word, letter):
#    index = 0
#    return ([letter for letter in range(len(word)) if word.find(letter) == letter])

word = input('type word to search: ').lower()
letter= input('type letter to search for: ').lower()
def search1(w, l):
    index1 = 0 - len(w)
    try:
        while True:
            index1 = string.index(w, index1 + len(sub))
            return index1
    except ValueError:
        pass
