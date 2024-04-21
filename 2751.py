import sys
input = sys.stdin.readline
print = sys.stdout.write

def merge(s, e):
    global arr, tmp
    if s+1 > e:
        return
    m = (s+e)//2
    merge(s, m)
    merge(m+1, e)
    
    for i in range(s, e+1):
        tmp[i] = arr[i]
    
    start = s
    idx1 = s
    idx2 = m+1
    
    while idx1 <= m and idx2 <= e:
        if tmp[idx1] < tmp[idx2]:
            arr[start] = tmp[idx1]
            start += 1
            idx1 += 1
        else:
            arr[start] = tmp[idx2]
            start += 1
            idx2 += 1
    
    while idx1 <= m:
        arr[start] = tmp[idx1]
        start += 1
        idx1 += 1
    
    while idx2 <= e:
        arr[start] = tmp[idx2]
        start += 1
        idx2 += 1

n = int(input())

arr = [0]*int(n+1)
tmp = [0]*int(n+1)
for i in range(1, n+1):
    arr[i] = int(input())
    
merge(1, n)

for i in range(1, n+1):
    print(str(arr[i])+'\n')