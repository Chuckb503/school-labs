import sys
import time
import os

def t_cls():
    time.sleep(2)
    os.system('cls')

t_cls()
user = []
user = input('List a sequence of numbers, sperated by a space: ').split(' ')
print(user)
#def m_e_n_t_o(e,f):
#    for g in range(len(e)):
#        if e[g] > 9:
#            e[g] -= 9
#            f.append(int(e[g]))
#        else:
#            f.append(int(e[g]))
def shrink():
    user = sum(user)
    for sti in range(len(user)):
        if user > 9:
            shrink()
        else:
            ans_er = []
            ans_er.append(int(user))
            return ans_er
shrink()
