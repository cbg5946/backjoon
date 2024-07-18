import sys, heapq
input = sys.stdin.readline

V, E = map(int, input().split())
m_list = [[] for _ in range(V+1)]
m_dist = [[sys.maxsize]*2 for _ in range(V+1)]

for _ in range(E):
    x, y, t, k = map(int, input().split())
    m_list[x].append([y, t, k])
    m_list[y].append([x, t, k])

m_dist[1][1] = 0
q = []
heapq.heappush(q, [0, 1, 1])

while q:
    cur = heapq.heappop(q)
    cur_c, eat_flag, cur_x = cur
    
    if m_dist[cur_x][eat_flag] < cur_c:
        continue
    
    for i in range(len(m_list[cur_x])):
        next_x, next_c, next_eat = m_list[cur_x][i]
        
        if eat_flag == 1:
            if m_dist[next_x][0] > cur_c + next_c - next_eat:
                m_dist[next_x][0] = cur_c + next_c - next_eat
                heapq.heappush(q, [m_dist[next_x][0], 0, next_x])
        
        if m_dist[next_x][eat_flag] > cur_c + next_c:
            m_dist[next_x][eat_flag] = cur_c + next_c
            heapq.heappush(q, [m_dist[next_x][eat_flag], eat_flag, next_x])

for i in range(2, V+1):
    print(min(m_dist[i][0], m_dist[i][1]))


    