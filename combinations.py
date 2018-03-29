from itertools import combinations
n = int(input())
alpha = input().split()
count = 0
#integer = [int(x) for x in input().split()]
k = int(input())
comb_list = list(combinations(alpha,k))
flist = [i for i in comb_list if 'a' in i]
print((len(flist)/(len(comb_list))))
