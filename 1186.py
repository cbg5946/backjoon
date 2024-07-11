N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    arr[b].append(a)

def dfs(a, b):
    if a == b:
        return True
    for i in arr[a]:
        if i == b:
            return True
        else:
            dfs(i, b)
    return False
    

Q = int(input())
for _ in range(Q):
    a, b = map(int, input().split())
    if dfs(a, b):
        print(b)
    else:
        if dfs(b, a):
            print(a)
        else:
            print("gg")
