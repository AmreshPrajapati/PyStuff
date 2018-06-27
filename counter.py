from collections import Counter
n = int(input())
slist = Counter(map(int, input().split()))
c = int(input())
sum = 0
for i in range(c):
    size, price = list(map(int, input().split()))
    if(slist[size]):
        sum+=price
        slist[size]-=1    
print(sum)