# import sys
# input = sys.stdin.readline
# V, E = map(int, input().split())

# city = [[int(1E9) for _ in range(V+1)] for _ in range(V+1)]

# for _ in range(E):
#     a, b, c = map(int, input().split())
#     city[a][b] = c

# for k in range(1, V+1):
#     for i in range(1, V+1):
#         for j in range(1, V+1):
#             if city[i][k] + city[k][j] < city[i][j]:
#                 city[i][j] = city[i][k] + city[k][j]

# ans = int(1E9)
# flag = False
# for i in range(1, V+1):
#     if city[i][i] < int(1E9):
#         ans = min(ans, city[i][i])
#         flag = True

# if not flag:
#     print(-1)
# else:
#     print(ans)
    
import heapq, sys
input = sys.stdin.readline

V, E = map(int, input().split())
city = [[] for _ in range(V+1)]
m_dist = [[int(1e9)] * (V+1) for _ in range(V+1)]

q = []

for _ in range(E):
    a, b, c = map(int, input().split())
    city[a].append([b, c])
    m_dist[a][b] = c
    
    heapq.heappush(q, [c, a, b])

while q:
    v, s, e = heapq.heappop(q)
    if s == e:
        print(v)
        break
    if m_dist[s][e] < v:
        continue
    
    for de, dv in city[e]:
        nv = v + dv
        if nv < m_dist[s][de]:
            ne = de
            m_dist[s][ne] = nv
            heapq.heappush(q, [nv, s, ne])
else:
    print(-1)