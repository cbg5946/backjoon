from collections import deque

def bfs(i, j):
    q = deque()
    q.append((i, j))
    x, y = q.popleft()
    print(x, y)

bfs(1, 1)