import sys
input = sys.stdin.readline
N = int(input())

A = list(map(int, input().split()))

res = []
res.append(A[0])

for i in range(1, N):
    if A[i] > res[-1]:
        res.append(A[i])
    else:
        s, e = 0, len(res)-1
        while s < e:
            mid = (s+e)//2
            if res[mid] < A[i]:
                s = mid + 1
            else:
                e = mid
        res[s] = A[i]

print(len(res))