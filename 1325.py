import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
com = [[] for _ in range(N+1)]
visited = [False]*(N+1)
res = [0]*(N+1)

for _ in range(M):
    a, b = map(int, input().split())
    com[b].append(a)

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = True
    while q:
        node = q.popleft()
        for now in com[node]:
            if visited[now] == False:
                visited[now] = True
                res[x] += 1
                q.append(now)

for i in range(1, N+1):
    visited = [False]*(N+1)
    bfs(i)

max_num = max(res)

for i in range(1, N+1):
    if res[i] == max_num:
        print(i, end = ' ')