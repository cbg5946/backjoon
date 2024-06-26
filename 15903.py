import heapq
n, m = map(int, input().split())

arr = list(map(int, input().split()))
heap = []
for i in arr:
    heapq.heappush(heap, i)

for _ in range(m):
    a, b = heapq.heappop(heap), heapq.heappop(heap)
    tmp = a + b
    for _ in range(2):
        heapq.heappush(heap, tmp)

res = sum(heap)
print(res)