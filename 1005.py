from collections import deque
import sys
input = sys.stdin.readline
T = int(input())
        
while T>0:
    T -= 1
    N, K = map(int, input().split())
    building = [0]
    building += list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y].append(x)
    W = int(input())
    
    s = W
    time = [0] * (N+1)
    q = deque()
    q.append(s)
    time[s] += building[s]
    flag = False
    while q:
        now = q.popleft()
        for next in graph[now]:
            if time[next] < time[now] + building[next]:
                time[next] = time[now] + building[next]
                q.append(next)
    print(max(time))