N, M = map(int, input().split())

parent = []
for i in range(N+1):
    parent.append(i)

true_people = list(map(int, input().split()))[1:]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a != b:
        parent[b] = a

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

count = 0
arr = []
for _ in range(M):
    arr.append(list(map(int, input().split()))[1:])

if true_people:
    for i in true_people:
        union(true_people[0], i)

        
    for _ in range(M):
        for i in range(M):
            for j in arr[i]:
                if j in true_people:
                    for k in arr[i]:
                        union(true_people[0], k)
                        if k not in true_people:
                            true_people.append(k)
    for i in arr:
        flag = True
        for j in i:
            if find(j) == find(true_people[0]):
                flag = False
        if flag:
            count += 1
    print(count)
else:
    print(len(arr))