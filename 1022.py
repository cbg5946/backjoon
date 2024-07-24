r1, c1, r2, c2 = map(int, input().split())
cnt = (c2-c1+1)*(r2-r1+1)
arr = [[0 for _ in range(c2-c1+1)] for _ in range(r2-r1+1)]

x, y = 0, 0
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
num = 1
distance = 1
dir = 0

max_len = 0
while cnt > 0:
    for i in range(2):
        for j in range(distance):
            if r1 <= x <= r2 and c1 <= y <= c2:
                arr[x-r1][y-c1] = num
                cnt -= 1
                max_len = len(str(num))
            x += dx[dir]
            y += dy[dir]
            num += 1
        dir = (dir +1) % 4
    distance += 1

for i in range(r2-r1+1):
    for j in range(c2-c1+1):
        print(str(arr[i][j]).rjust(max_len), end = ' ')
    print()