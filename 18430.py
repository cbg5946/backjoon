n, m = map(int, input().split())

arr = []
visited = [[False for _ in range(m)] for _ in range(n)]
for _ in range(n):
    arr.append(list(map(int, input().split())))
    

dx = [1, 0, -1, 0, 1]
dy = [0, 1, 0, -1, 0]

res = []

def dfs(x, y, v):
    if y == m:
        y = 0
        x += 1
    if x == n:
        res.append(v)
        return
    
    if visited[x][y] == False:
        for _ in range(4):
            nx1 = x + dx[_]
            ny1 = y + dy[_]
            nx2 = x + dx[_+1]
            ny2 = y + dy[_+1]
            
            if 0 <= nx1 < n and 0 <= ny1 < m and 0 <= nx2 < n and 0 <= ny2 < m:
                if visited[nx1][ny1] == False and visited[nx2][ny2] == False:
                    visited[nx1][ny1] = True; visited[nx2][ny2] = True; visited[x][y] = True
                    
                    dfs(x, y+1, v + 2*arr[x][y] + arr[nx1][ny1] + arr[nx2][ny2])

                    visited[nx1][ny1] = False; visited[nx2][ny2] = False; visited[x][y] = False
                    
    dfs(x, y+1, v)

dfs(0, 0, 0)
res.sort()
print(res[-1])