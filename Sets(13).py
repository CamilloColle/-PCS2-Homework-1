#Introduction to Sets:
def average(array):
    average = sum(set(array))/len(set(array))
    return average


#No Idea!
l = list(input().split())
n = int(l[0])
m = int(l[1])
N = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
h = 0

for i in N:
    if i in A:
        h += 1
    elif i in B:
        h -= 1
print(h)


#Symmetric Difference:
M,N = [set(input().split()) for i in range(4)][1::2]
lst = []

for i in M:
    if i not in N:
        lst.append(i)
for l in N:
    if l not in M:
        lst.append(l)

print('\n'.join(sorted(lst, key = int)))


#Set.add():
n = int(input())
diff_c = set()

for i in range(n):
    diff_c.add(input())

print(len(diff_c))


#Set .discard(), .remove() & .pop():
n = int(input())
s = set(map(int, input().split()))

for i in range(int(input())):
    com = input().split()
    if com[0] == 'pop':
        s.pop()
    elif com[0] == 'remove':
        s.remove(int(com[1]))
    elif com[0] == 'discard':
        s.discard(int(com[1]))
print(sum(s))


#Set .union() Operation:
n,b = [set(input().split()) for _ in range(4)] [1::2]
print(len(n.union(b)))


#Set .intersection() Operation:
n,b = [set(input().split()) for _ in range(4)] [1::2]
print(len(n.intersection(b)))


#Set .difference() Operation:
n,b = [set(input().split()) for _ in range (4)] [1::2]
print(len(n.difference(b)))


#Set .symmetric_difference() Operation:
n,b = [set(input().split()) for _ in range(4)] [1::2]
print(len(n.symmetric_difference(b)))


#Set Mutations:
n = int(input())
A = set(map(int, input().split()))

for i in range(int(input())):
    com = input().split()[0]
    subs = set(map(int, input().split()))
    getattr(A, com)(subs)

print(sum(A))


#The Captain's Room:
g = int(input())
N = list(map(int, input().split()))
n = set(N)

for i in n:
    N.remove(i)
    if i not in N:
        print(i)
        break


#Check Subset:
n = int(input())

for _ in range(n):
    x = int(input())
    a = set(map(int, input().split()))
    y = int(input())
    b = set(map(int, input().split()))
    v = 'True'
    for i in a:
        if i not in b:
            v = 'False'
    print(v)


#Check Strict Superset:
A = set(map(int, input().split()))
n = int(input())
v1 = 0
v2 = 0
for _ in range(n):
    s = set(map(int, input().split()))
    for i in s:
        if i not in A:
            v1 = 1
        elif len(A.difference(s)) == 0:
            v2 = 1
if v1 != 0 or v2 != 0:
    print('False')
else:
    print('True')