I = []
II = []
III = []
IV = []

user = input('List a sequence of 16 numbers, using 1-9 putting a space between each: ').split(" ")
I = user


def d_l(u):
    u.pop(-1)
    return u
d_l(user)

def l_b(a):
    a.reverse()
    return a
l_b(I)

def m_e_n(b,c):
    for d in range(len(b)):
        if d % 2 == 0:
            c.append(int(b[d])*2)
        else:
            c.append(int(b[d]))
m_e_n(I,II)

def m_e_n_t_o(e,f):
    for g in range(len(e)):
        if e[g] > 9:
            e[g] -= 9
            f.append(int(e[g]))
        else:
            f.append(int(e[g]))
m_e_n_t_o(II,III)


def  j_k(h,i):
    i = str(sum(h))
    return i
j_k(III,IV)

def l_m(m,o):
    for r in range(m):
        if m[r](-1) = u.pop(-1):
            return "Valid!"
        else:
            return "Invalid!"
