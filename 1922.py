import heapq, sys
input = sys.stdin.readline

N = int(input())
M = int(input())

heap = []
parent = [0] * (N+1)

for i in range(N+1):
    parent[i] = i

for _ in range(M):
    a, b, c = map(int, input().split())
    heapq.heappush(heap, [c, a, b])

def union(a, b):
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
    
result = 0
use_Edge = 0

while use_Edge < N-1:
    v, s, e = heapq.heappop(heap)
    if find(s) != find(e):
        union(s, e)
        result += v
        use_Edge += 1

print(result)