import itertools
a = map(int, input().split())
b = map(int, input().split())
lst = list(itertools.product(a,b))
for x in lst:
    print(x,end=" ")