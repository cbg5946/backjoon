P = int(input())

for k in range(1, P+1):
    arr = [0, 1]
    N, M = map(int, input().split())
    i, j = 0, 1
    while True:
        tmp = (arr[i]+arr[j])%M
        arr.append(tmp)
        if arr[-2] == 0 and arr[-1] == 1:
            print(k, j)
            break
        i += 1
        j += 1