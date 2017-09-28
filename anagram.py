"""

>>> anagram('anagram', 'nag a ram')
True

>>> anagram('Right. One... two... five!', 'Three, sir.')
False

>>> anagram('My ideal time', 'Immediately')
True

"""

# Write your code below.

def anagram(str1, str2):
    str1 = sorted(s1)
    str2 = sorted(s2)
    if str1 == str2:
       return 'true'
    else:
       return 'false'
