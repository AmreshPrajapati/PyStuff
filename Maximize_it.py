from itertools import product
k,m = map(int, input().split())
n = (list(map(int, input().split()))[1:] for _ in range(k))
mylist = list(n)
final = []
combination = list(product(*mylist))
for i in combination:
    final.append(sum(j*j for j in i) % m)
print(max(final))
