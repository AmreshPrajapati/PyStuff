n,m = map(int, input().split())
for i in range(n):
    if(i<n/2-1):
        print(((2*i+1)*'.|.').center(m,"-"))
    if(i==int(n/2)):
        print('WELCOME'.center(m,'-'))
    elif(i>n/2):
        print(((2*(n-i-1)+1)*'.|.').center(m,"-"))
