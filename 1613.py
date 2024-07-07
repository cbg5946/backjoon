import sys
input = sys.stdin.readline
n, k = map(int, input().split())

case = [[False]*(n+1) for _ in range(n+1)]

for _ in range(k):
    a, b = map(int, input().split())
    case[b][a] = True
    
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if case[j][i] and case[i][k]:
                case[j][k] = True

s = int(input())
for _ in range(s):
    a, b = map(int, input().split())
    if case[a][b] and not case[b][a]:
        print(1)
    elif not case[a][b] and case[b][a]:
        print(-1)
    elif not case[a][b] and not case[b][a]:
        print(0)
