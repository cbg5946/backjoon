from collections import deque

N = int(input())
Map = [[] for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]

for i in range(N):
    s = input()
    for c in s:
        if c == '0':
            Map[i].append(0)
        elif c == '1':
            Map[i].append(1)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(i, j):
    size = 1
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    while q:
        x, y = q.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and Map[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] = True
                size += 1
    return size

count = 0
house = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and Map[i][j] == 1:
            house.append(bfs(i, j))
            count += 1

house.sort()
print(count)
for i in house:
    print(i)

