import heapq

N = int(input())
arr = []

for _ in range(N):
    tmp = list(map(int, input().split()))
    if not arr:
        for i in tmp:
            heapq.heappush(arr, i)
    else:
        for i in tmp:
            if arr[0] < i:
                heapq.heappop(arr)
                heapq.heappush(arr, i)
print(arr[0])