import string
def print_rangoli(size):
    alpha = (string.ascii_lowercase)[0:size]
    P = []
    for i in range(size):
        s = "-".join(alpha[i:size])
        P.append(s[::-1]+s[1:])
    w=len(P[0])
    for i in range(size-1,-1,-1):
        print(P[i].center(w,'-'))
    for i in range(1,size):
        print(P[i].center(w,'-'))
