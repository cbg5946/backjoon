import sys
mod = 1000000007
a = [0]*5001
a[0] = 1

for i in range(2, 5001, 2):
    for j in range(2, i+1, 2):
        a[i] += a[j-2]*a[i-j]
    a[i]%=mod
       
t = int(sys.stdin.readline())
for _ in range(t):
    l = int(sys.stdin.readline())
    print(a[l])