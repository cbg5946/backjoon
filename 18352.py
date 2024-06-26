from collections import deque
import sys
input = sys.stdin.readline
N, M, K, X = map(int, input().split())

city = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    city[a].append(b)

dis = [0]*(N+1)
visited = [False]*(N+1)

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = True
    while q:
        node = q.popleft()
        for now in city[node]:
            if visited[now] == False and dis[now] < K:
                visited[now] = True
                dis[now] = dis[node]+1
                q.append(now)

bfs(X)

flag = False
for i in range(1, N+1):
    if dis[i] == K:
        flag = True
        print(i)
if flag == False:
    print(-1)