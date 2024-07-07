import heapq, sys
input = sys.stdin.readline
N = int(input())

planet = []
for _ in range(N):
    planet.append(list(map(int, input().split())))

q = []
for i in range(N):
    for j in range(i, N):
        if i == j:
            continue
        heapq.heappush(q, [planet[i][j], i+1, j+1])

parent = []
for i in range(N+1):
    parent.append(i)

def Union(a, b):
    a = find(a)
    b = find(b)
    
    if a != b:
        parent[b] = a

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

min_flow = 0
use = 0
while use < N-1:
    v, a, b = heapq.heappop(q)
    if find(a) != find(b):
        Union(a, b)
        min_flow += v
        use += 1

print(min_flow)