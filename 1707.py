import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
k = int(input())
flag = True

def dfs(v):
    global flag
    visited[v] = True # visited 방문 표시
    for now in arr[v]:
        if not visited[now]:
            check[now] = (check[v]+1)%2 # 인접한 노드끼리는 집합을 달리한다(0, 1로 구분)
            dfs(now)
        elif check[v] == check[now]:
            flag = False

for _ in range(k):
    v, e = map(int, input().split())
    arr = [[] for _ in range(v+1)]
    visited = [False]*(v+1)
    check = [0]*(v+1)
    flag = True
    for _ in range(e):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    for i in range(1, v+1):
        if flag:
            dfs(i)
        else:
            break
    if flag:
        print("YES")
    else:
        print("NO")
        