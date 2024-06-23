from collections import deque
N, M = map(int, input().split())

Map = [[0] for _ in range(N+1)]
visited = [[False for _ in range(M+1)] for _ in range(N+1)]

for i in range(1, N+1):
    s = input()
    for c in s:
        if c == '1':
            Map[i].append(10000)
        else:
            Map[i].append(0)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
    q = deque()
    q.append((1, 1))
    Map[1][1] = 1
    visited[1][1] = True
    while q:
        x, y = q.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 1 <= nx <= N and 1 <= ny <= M and not visited[nx][ny] and not Map[nx][ny] == 0:
                Map[nx][ny] = min(Map[x][y] + 1, Map[nx][ny])
                q.append((nx, ny))
                visited[nx][ny] = True

bfs()
print(Map[N][M])