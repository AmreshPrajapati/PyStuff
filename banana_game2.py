def minion_game(string):
    s = 0
    k = 0
    vowel = 'AEIOU'
    for i in range(len(string)):
        if string[i] in vowel:
            k+=len(string)-i
        else:
            s+=len(string)-i
    if (s > k):
        print("Stuart %d" % s)
    elif (s < k):
        print ("Kevin %d" % k)
    else:
        print ("Draw")
