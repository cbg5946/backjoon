import copy, sys
input = sys.stdin.readline
N = int(input())
board = []
visited = [[False for _ in range(N)] for __ in range(N)]
for _ in range(N):
    board.append(list(map(int, input().split())))

def down(arr):
    for j in range(N):
        last = N-1
        for i in range(N-1, -1, -1):
            x, y = i, j
            if arr[x][y] != 0:
                tmp = arr[x][y]
                arr[x][y] = 0
                
                if arr[last][y] == 0:
                    arr[last][y] = tmp
                elif arr[last][y] == tmp:
                    arr[last][y] *= 2
                    last -= 1
                else:
                    last -= 1
                    arr[last][y] = tmp
def right(arr):
    for i in range(N):
        last = N-1
        for j in range(N-1, -1, -1):
            x, y = i, j
            if arr[x][y] != 0:
                tmp = arr[x][y]
                arr[x][y] = 0
                
                if arr[x][last] == 0:
                    arr[x][last] = tmp
                elif arr[x][last] == tmp:
                    arr[x][last] *= 2
                    last -= 1
                else:
                    last -= 1
                    arr[x][last] = tmp
def up(arr):
    for j in range(N):
        first = 0
        for i in range(1, N):
            x, y = i, j
            if arr[x][y] != 0:
                tmp = arr[x][y]
                arr[x][y] = 0
                
                if arr[first][y] == 0:
                    arr[first][y] = tmp
                elif arr[first][y] == tmp:
                    arr[first][y] *= 2
                    first += 1
                else:
                    first += 1
                    arr[first][y] = tmp
def left(arr):
    for i in range(N):
        first = 0
        for j in range(1, N):
            x, y = i, j
            if arr[x][y] != 0:
                tmp = arr[x][y]
                arr[x][y] = 0
                
                if arr[x][first] == 0:
                    arr[x][first] = tmp
                elif arr[x][first] == tmp:
                    arr[x][first] *= 2
                    first += 1
                else:
                    first += 1
                    arr[x][first] = tmp

ans = 0

def backtracking(arr, cnt):
    global ans

    if cnt == 5:
        for i in range(N):
            for j in range(N):
                ans = max(ans, arr[i][j])
        return
    for i in range(4):
        origin = copy.deepcopy(arr)
        if i == 0:
            down(arr)
        elif i == 1:
            up(arr)
        elif i == 2:
            right(arr)
        elif i == 3:
            left(arr)
        backtracking(arr, cnt+1)
        arr = copy.deepcopy(origin)
backtracking(board, 0)

print(ans)
