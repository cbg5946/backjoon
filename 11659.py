import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = []
arr.append(0)
arr += list(map(int, input().split()))

for i in range(1, N+1):
    arr[i] += arr[i-1]

for _ in range(M):
    s, e = map(int, input().split())
    print(arr[e] - arr[s-1])