N, M = map(int, input().split())
s = 10000000
relation = [[s for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    relation[a][b] = 1
    relation[b][a] = 1


for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == j: continue
            relation[i][j] = min(relation[i][j], relation[i][k] + relation[k][j])

min_kbnum = s*(N+1)
ans = 0
for i in range(1, N+1):
    if sum(relation[i]) < min_kbnum:
        ans = i
        min_kbnum = sum(relation[i])
print(ans)