import sys, heapq
input = sys.stdin.readline

N = int(input())
M = int(input())

m_list = [[] for _ in range(N+1)]
m_distance = [2000000000]*(N+1)
visited = [False]*(N+1)

for _ in range(M):
    s, e, v = map(int, input().split())
    m_list[s].append([e, v])

S, E = map(int, input().split())

heap = []
heapq.heappush(heap, [0, S])
m_distance[S] = 0

while heap:
    node = heapq.heappop(heap)[1]
    if visited[node]: continue
    visited[node] = True

    for i in range(len(m_list[node])):
        next = m_list[node][i][0]
        value = m_list[node][i][1]

        if m_distance[next] > m_distance[node] + value:
            m_distance[next] = m_distance[node] + value
            heapq.heappush(heap, [m_distance[next], next])

print(m_distance[E])
