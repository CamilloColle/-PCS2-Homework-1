#itertools.product():
from itertools import product
A = list(map(int, input().split()))
B = list(map(int, input().split()))
pr = (product(A,B))
for i in pr:
    print(i, end = ' ')


#itertools.permutations():
from itertools import permutations
S = input().split()
l = permutations(sorted(S[0]),int(S[1]))

for i in l:
    i = ''.join(i)
    print(i)


#itertools.combinations():
from itertools import combinations

S = input().split()
nl = []
for i in range(1, int(S[1]) + 1):
    l = combinations(sorted(S[0]), i)
    for h in l:
        nl.append(h)

for i in nl:
    i = ''.join(i)
    print(i)


#itertools.combinations_with_replacement():
from itertools import combinations_with_replacement
S = input().split()
l = combinations_with_replacement(sorted(S[0]),int(S[1]))

for i in l:
    i = ''.join(i)
    print(i)


#Compress The String!
from itertools import groupby

for j,k in groupby(input()):
    l = [(len(list(k)), int(j))]
    print(*l, end = ' ')


#Iterables and Iterators:
from itertools import combinations
N = int(input())
S = input().split()
k = int(input())
c = list(combinations(S,k))
num = 0
div = len(c)

for i in c:
    if 'a' in i:
        num += 1

print (num/div)

