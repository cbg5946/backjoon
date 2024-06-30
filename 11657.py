import sys
input = sys.stdin.readline
N, M = map(int, input().split())

edges = []
for _ in range(M):
    edges.append(list(map(int, input().split())))

m_distance = [sys.maxsize] * (N+1)

m_distance[1] = 0

for _ in range(N-1):
    for s, e, v in edges:
        if m_distance[s] != sys.maxsize and m_distance[e] > m_distance[s] + v:
            m_distance[e] = m_distance[s] + v

is_minus = False

for s, e, v in edges:
    if m_distance[s] != sys.maxsize and m_distance[e] > m_distance[s] + v:
        is_minus = True

if is_minus:
    print(-1)
else:
    for i in range(2, N+1):
        if m_distance[i] == sys.maxsize:
            print(-1)
        else:
            print(m_distance[i])