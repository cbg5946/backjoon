from collections import deque
N = int(input())
A = list(map(int, input().split()))
shape = deque()
for i in A:
    shape.append(i)

samples = []
M = int(input())

for _ in range(M):
    samples.append(list(map(int, input().split())))

arr = []

for i in range(N):
    tmp = list(shape)
    arr.append(tmp)
    
    shape.append(shape.popleft())
    
for i in range(N):
    tmp = list(shape)
    tmp.reverse()
    for j in range(N):
        tmp[j] = (tmp[j]+2)%4
        if tmp[j] == 0:
            tmp[j] = 4
    arr.append(tmp)
    shape.append(shape.popleft())
    
cnt = 0
res = []
for sample in samples:
    if sample in arr:
        res.append(sample)
        cnt += 1
print(cnt)
for i in res:
    print(*i)