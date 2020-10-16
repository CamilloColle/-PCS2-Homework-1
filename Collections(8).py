#collections.Counter():
from collections import Counter

X = int(input())
c = Counter(list(input().split()))
tot = 0

for i in range(int(input())):

    size, cost = input().split()

    if c[size]:
        tot += int(cost)
        c[size] -= 1

print(tot)


#DefaultDict Tutorial:
from collections import defaultdict

n, m = input().split()
A = defaultdict(list)
B = []

for i in range(int(n)):
    A[input()].append(i+1)

for i in range(int(m)):
    B.append(input())

for i in B:
    if i in A:
        print(*A[i])
    else:
        print(-1)


#Collections.namedtuple()
from collections import namedtuple

N = int(input())
columns = namedtuple('columns', input().split())
tot = 0

for i in range(N):
    c1, c2, c3, c4 = input().split()
    column = columns(c1, c2, c3, c4)
    tot += int(column.MARKS)

print(tot / N)


#Collections.OrderedDict():
from collections import OrderedDict

N = int(input())
D = OrderedDict()
D1 = OrderedDict()

for i in range(N):
    ist = input().split()
    if ' '.join(ist[0:-1]) in D:
        D[' '.join(ist[0:-1])] += int(ist[-1])
    else:
        D[' '.join(ist[0:-1])] = int(ist[-1])

for i in D:
    print(i, D[i])


#Word Order:
from collections import *

n = int(input())
lst = []

for i in range(n):
    w = input()
    lst.append(w)
c = Counter(lst)


print(len(c))
print(*c.values())


#Collections.deque():
from collections import deque

N = int(input())
d = deque()
for i in range(N):
    com = input().split()
    if com[0] == 'append':
        d.append(com[1])
    elif com[0] == 'appendleft':
        d.appendleft(com[1])
    elif com[0] == 'pop':
        d.pop()
    elif com[0] == 'popleft':
        d.popleft()
print(*d)


#Company Logo: (Here I deleted the 'if __name__ == '__main__':' line and the following sincei haven't used a function)
d = dict()
st = sorted(list(input()))
c = Counter(st)
l = []

for i in c:
    if c[i] not in d:
        d[c[i]] = i
    else:
        d[c[i]] = d[c[i]] + i

lst = sorted(d.items())
lst.reverse()

for i in lst:
    if len(i[1]) == 1:
        if len(l) < 3:
            l.append((sorted(i[1])[0], i[0]))
    elif len(i[1]) == 2:
        x = 0
        while len(l) < 3 and x < 2:
            l.append((sorted(i[1])[x], i[0]))
            x += 1
    elif len(i[1]) >= 3:
        x = 0
        while len(l) < 3:
            l.append((sorted(i[1])[x], i[0]))
            x += 1

for i in l:
    print(i[0], i[1])


#Piling Up!
from collections import *

n = int(input())

for i in range(n):
    x = 'Yes'
    k = int(input())
    q = deque(map(int, input().split()))

    for i in reversed(sorted(q)):
        if q[0] == i:
            q.popleft()
        elif q[-1] == i:
            q.pop()
        else:
            x = 'No'
            break

    print(x)
