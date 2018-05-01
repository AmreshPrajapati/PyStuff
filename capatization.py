def capitalize(string):
    st = string.split()
    print(st)
    hello = []
    for i in st:
        if(i[0].isdigit()):
            print(i)
            hello.append(i.lower())
            
        else:
            hello.append(i.title())
        
    return " ".join(hello)