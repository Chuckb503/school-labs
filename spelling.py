"""
>>>Word(believe)
'true'

>>>Word(ceiling)
'true'

>>>Word(science)

'false'

>>>Word(weird)

'false'
"""
 def spell(word):
     for i in range(len(word)):

    print("scanning {0}".format(word[i:i+3]))
    if word[i:i+3].lower() == "cie":
        return false
    if word[i:i+3].lower() == "cei":
        return true
