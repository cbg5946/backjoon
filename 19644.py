import sys
from collections import deque
input = sys.stdin.readline
L = int(input())
ML, MK = map(int, input().split())
C = int(input())
enemy = []
isDie = False
tmp = 0
use_ammo = deque()
for _ in range(ML):
    use_ammo.append(False)
ammo_cnt = 0
for i in range(L):
    num = int(input())
    tmp += 1
    if tmp > ML:
        tmp = ML
    if num > (tmp-ammo_cnt)*MK:
        C -= 1
        use_ammo.append(True)
        ammo_cnt += 1
    else:
        use_ammo.append(False)
    if use_ammo.popleft() == True:
        ammo_cnt -= 1
    if C < 0:
        isDie = True
        break
if isDie:
    print("NO")
else:
    print("YES")
