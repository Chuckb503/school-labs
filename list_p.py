#list tests
import sys
import time
import os

def t_cls():
    time.sleep(5)
    os.system('cls')

user = input('List a sequence of random numbers using a , and space afterwards: ').split(", ")
#user = lst[], lst2[], lst3[], lst4[], lst5[]
lst = []
lst2 = []
lst3 = []
lst4 = []
lst5 = []
lst = user
lst2 = lst
lst3 = lst
lst4 = lst
lst5 = lst

def backw(xt):
    xt.reverse()
    return xt

print(backw(lst))

def ma_n(mx):
    m_n = max(mx)
    return(m_n)

print(ma_n(lst2))

def cofe(ce,cf):
    cfe = int((ce)[0])
    cfe3 = int((cf)[0])
    if str(cfe) == str(cfe3):
        return('true')
    elif str(cfe) != str(cfe3):
        return('false')


print(cofe(lst,lst3))

def sofe(se,sf):
    csl = int((se)[1])
    csl4 =  int((sf)[1])
    if str(csl) == str(csl4):
        return('true')
    elif str(csl) != str(csl4):
        return('false')

print(sofe(lst,lst4))

def sma(we):
    print('Hello User!\n Here is your list you typed.\n')
    print(we)
    inp = input('Would you like me to reverse the copy of the list I made for you?\n Type (Y)es or (N)o: ')
    if str(inp) == ('y'):
        return(backw(we))
    elif str(inp) == ('n'):
        return("GOOD BYE! You will be missed!")
        t_cls()
        sys.exit()

print(sma(lst5))
