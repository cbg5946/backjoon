N = int(input())
M = int(input())

parent = []
for i in range(N+1):
    parent.append(i)
    
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

for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(len(arr)):
        if arr[j] == 1:
            union((i+1), (j+1))

city = list(map(int, input().split()))
res = find(city[0])
flag = False
for i in range(1, len(city)):
    if res != find(city[i]):
        flag = True
        break
if flag:
    print("NO")
else:
    print("YES")