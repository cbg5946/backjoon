import sys
from collections import deque

r, c = map(int, input().split())

cave = []
arr = [[0]*c for _ in range(r)]
arr_list = []
cnt = 0

for i in range(r):
    tmp = input()
    tmp = list(tmp)
    cave.append(tmp)
for i in range(r):
    for j in range(c):
        if cave[i][j] == 'x':
            cnt += 1

n = int(input())
n_list = list(map(int, input().split()))

def shoot(idx):
    global cnt
    k = n_list[idx]
    if idx%2 == 0:
        j = 0
        while True:
            if cave[r-k][j] == 'x':
                cave[r-k][j] = '.'
                cnt -= 1
                return r-k, j
            j += 1
            if j == c:
                break
    else:
        j = c-1
        while True:
            if cave[r-k][j] == 'x':
                cave[r-k][j] = '.'
                cnt -= 1
                return r-k, j
            j -= 1
            if j == -1:
                break
    return 0, 0

x_cnt = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
max_depth = -1
def check_air(a, b):
    if cave[a][b] == '.':
        return
    global x_cnt
    global max_depth
    q = deque()
    q.append([a, b])
    arr_list.append([a, b])
    arr[a][b] = 1
    x_cnt += 1
    while len(q) != 0:
        x, y = q.popleft()
        max_depth = max(max_depth, x)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and cave[nx][ny] == 'x' and arr[nx][ny] == 0:
                arr[nx][ny] = 1
                x_cnt += 1
                arr_list.append([nx, ny])
                q.append([nx, ny])

min_dif = 110

def different():
    global min_dif
    for y in range(c):
        x = -1
        flag = False
        dif = 0
        while True:
            x += 1
            if x == r:
                break
            if arr[x][y] == 1:
                flag = True
                dif = 0
            elif arr[x][y] == 0 and cave[x][y] == '.':
                dif += 1
            elif flag == True and arr[x][y] == 0 and cave[x][y] == 'x':
                break
        if flag:
            min_dif = min(min_dif, dif)
    return min_dif

def down(k):
    tmp = []
    for l in arr_list:
        tmp.append([l[0]+k, l[1]])
        cave[l[0]][l[1]] = '.'
    for l in tmp:
        cave[l[0]][l[1]] = 'x'

def reset():
    global min_dif, max_depth, arr, arr_list
    min_dif = 110
    max_depth = -1
    arr = [[0]*c for _ in range(r)]
    arr_list.clear()

for idx in range(n):
    k = n_list[idx]
    max_depth = 0
    x, y = shoot(idx)
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1): 
            reset()
            if x+i < 0 or x+i > r-1:
                i = 0
            if y+j < 0 or y+j > c-1:
                j = 0
            check_air(x+i, y+j)
            if 0 <= max_depth < r-1:
                k = different()
                down(k)
        
for _ in cave:
    print(''.join(_))