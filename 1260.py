from collections import deque
N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
dfs_res = []
bfs_res = []

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()



def dfs(v):
    visited[v] = True
    dfs_res.append(v)
    for next in graph[v]:
        if not visited[next]:
            dfs(next)
dfs(V)

visited = [False for _ in range(N+1)]
def bfs(v):
    q = deque()
    q.append(v)
    bfs_res.append(v)
    visited[v] = True
    while q:
        now = q.popleft()
        for next in graph[now]:
            if not visited[next]:
                q.append(next)
                bfs_res.append(next)
                visited[next] = True
bfs(V)

for _ in dfs_res:
    print(_, end = ' ')
print()
for _ in bfs_res:
    print(_, end = ' ')