import heapq, sys
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

m_list = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    m_list[u].append([v, w])

visited = [False]*(V+1)
m_distance = [90000000]*(V+1)

heap = []
heapq.heappush(heap, [0, K])
m_distance[K] = 0

while heap:
    node = heapq.heappop(heap)[1]
    if visited[node]:
        continue
    visited[node] = True
    
    for i in range(len(m_list[node])):
        next = m_list[node][i][0]
        value = m_list[node][i][1]
        if m_distance[next] > m_distance[node]+value:
            m_distance[next] = m_distance[node]+value
            heapq.heappush(heap, [m_distance[next], next])

for i in range(1, V+1):
    if visited[i]:
        print(m_distance[i])
    else:
        print("INF")