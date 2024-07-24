from collections import deque
import copy
N, K = map(int, input().split())

N = str(N)

check = [[False for _ in range(1000001)] for _ in range(11)]

arr = []
for i in N:
    arr.append(i)

q = deque()

q.append((arr, 0))
ans = []
while q:
    now, cnt = q.popleft()
    if cnt >= K:
        break
    for i in range(len(N)):
        for j in range(len(N)):
            if i == j:
                continue
            test = copy.deepcopy(now)
            test[i], test[j] = test[j], test[i]
            num = ""
            for k in test:
                num += k
            if num[0] == '0':
                continue
            else:
                num = int(num)
                if not check[cnt+1][num]:
                    check[cnt+1][num] = True
                    q.append((test, cnt+1))
flag = False
for i in range(1000000, -1, -1):
    if check[K][i]:
        flag = True
        print(i)
        break

if not flag:
    print(-1)