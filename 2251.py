from collections import deque
now = list(map(int, input().split()))
visited = [[False for _ in range(201)] for _ in range(201)]

answer = [False]*201
send = [0, 0, 1, 1, 2, 2]
receive = [1, 2, 0, 2, 0, 1]

def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    answer[now[2]] = True
    while q:
        a, b = q.popleft()
        c = now[2] - (a + b)
        for _ in range(6):
            next = [a, b, c]
            next[receive[_]] += next[send[_]]
            next[send[_]] = 0
            if next[receive[_]] > now[receive[_]]:
                next[send[_]] = next[receive[_]] - now[receive[_]]
                next[receive[_]] = now[receive[_]]
            
            if visited[next[0]][next[1]] == False:
                visited[next[0]][next[1]] = True
                q.append((next[0], next[1]))
                
                if next[0] == 0:
                    answer[next[2]] = True

bfs()
for i in range(201):
    if answer[i] == True:
        print(i, end = ' ')