import sys
input = sys.stdin.readline
N = int(input())

arr = []
color = [0] * (N+1)
ans = [0] * (N+1)
arr.append([])
for i in range(1, N+1):
    c, s = map(int, input().split())
    arr.append([s, c, i])

arr.sort()
j = 1
total = 0
for i in range(1, N+1):
    while arr[j][0] < arr[i][0]:
        color[arr[j][1]] += arr[j][0]
        total += arr[j][0]
        j += 1
    ans[arr[i][2]] = total - color[arr[i][1]]

for i in range(1, N+1):
    print(ans[i])