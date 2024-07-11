import sys
input = sys.stdin.readline
from collections import defaultdict, deque

N, M = map(int, input().split())
arr = defaultdict(list)

for _ in range(M):
    a, b = input().split()
    arr[b].append(a)

def bfs(x):
    q = deque()
    q.append(x)
    
    a = defaultdict(int)
    while q:
        v = q.popleft()
        
        for i in arr[v]:
            if not a[i]:
                a[i] = 1
                q.append(i)
    
    return a.keys()

Q = int(input())
for _ in range(Q):
    a, b = input().split()
    if a == b:
        print('gg', end = ' ')
    elif b in bfs(a):
        print(b, end = ' ')
    elif a in bfs(b):
        print(a, end = ' ')
    else:
        print('gg', end = ' ')
