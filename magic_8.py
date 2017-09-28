import sys
import random
import time
import os

os.system('cls')

def t_cls():
    time.sleep(4)
    os.system('cls')

def answers():
    l_ans = ["I don't know, 42?","I see... it's fuzzy ask later","Yes? or No? wait I'm suppose to know","I wouldn't beat the farm on it!", "I see a bright outcome", "Look out behind you! wait that's for me!!","NO!","Yes??"]
    random.choice(l_ans)
    return print(random.choice(l_ans))

ans = True

while ans:
    question = input("Ask the magic 8 ball a question: (Type exit to quit) ")

    if question == ("exit"):
        print("GOOD BYE! You will be missed!")
        t_cls()
        sys.exit()

    elif question is not ("exit"):
        answers()
        t_cls()
