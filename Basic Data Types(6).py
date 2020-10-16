#List Comprehension:
x = int(input())
y = int(input())
z = int(input())
n = int(input())
nl = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
print(sorted(nl))


#Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    s = sorted(set(arr))
    print(s[-2])


#Nested Lists:
if __name__ == '__main__':
    N = int(input())
    nl = []
    v = []
    sl_stud = []

    for _ in range(N):
        l = []
        name = input()
        grade = float(input())
        l.append(name)
        l.append(grade)
        v.append(grade)
        nl.append(l)

    for l in nl:
        if l[1] == sorted(set(v))[1]:
            sl_stud.append(l[0])

    print('\n'.join(sorted(sl_stud)))


#Finding the Percentage:
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    avg = sum(student_marks[query_name])
    div = 0
    for score in student_marks[query_name]:
        div += 1
    avg = avg / div

    print('%.2f' % (avg))


#Lists:
if __name__ == '__main__':
    N = int(input())
    L = []
    for _ in range(N):
        com = list(input().split())
        if com[0] == 'insert':
            L.insert(int(com[1]),int(com[2]))
        elif com[0] == 'print':
            print(L)
        elif com[0] == 'remove':
            L.remove(int(com[1]))
        elif com[0] == 'append':
            L.append(int(com[1]))
        elif com[0] == 'sort':
            L.sort(key = int)
        elif com[0] == 'pop':
            L.pop()
        elif com[0] == 'reverse':
            L.reverse()

#Tuples:
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))