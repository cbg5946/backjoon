N, M = map(int, input().split())
array = list(map(int, input().split()))

array.sort()

res = []
def backtracking(cnt):
    if cnt == M:
        for j in range(cnt):
            print(res[j], end = ' ')
        print()
        return
    for i in range(N):
        if array[i] not in res:
            res.append(array[i])
            backtracking(cnt+1)
            res.pop()
backtracking(0)