import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = []
for i in range(n+1):
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
    
def check(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        print("YES")
    else:
        print("NO")

for _ in range(m):
    tmp, a, b = map(int, input().split())
    if tmp == 0:
        union(a, b)
    elif tmp == 1:
        check(a, b)