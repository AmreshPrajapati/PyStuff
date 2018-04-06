def minion_game(string):
    stuart = []
    kevin = []
    cons = []
    vow = []
    for i in (string):
        if i.upper() not in ['A','E','I','O','U']:
            cons.append(i.upper())
        elif i.upper() in ['A','E','I','O','U']:
            vow.append(i.upper())
    cons = "".join(cons)
    vow  = "".join(vow)
    for i in range(len(string)):
        if string[i] in cons:
            stuart.append(string[i:])
            k=len(stuart)-1
            for j in range(len(stuart[k]),1,-1):
                stuart.append(stuart[k][:j-1])
    for i in range(len(string)):
        if string[i] in vow:
            kevin.append(string[i:])
            k=len(kevin)-1
            for j in range(len(kevin[k]),1,-1):
                kevin.append(kevin[k][:j-1])
    print("Stuart %d" % len(stuart) if len(stuart) > len(kevin) else "Kevin %d" % len(kevin))
