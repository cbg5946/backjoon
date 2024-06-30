arr = []

for _ in range(10):
    arr.append(list(map(int, input().split())))

x, y = 1, 1
arr[x][y] = 9

while True:
    if arr[x][y+1] == 0:
        arr[x][y+1] = 9
        y += 1
    elif arr[x][y+1] == 2:
        arr[x][y+1] = 9
        break
    elif arr[x][y+1] == 1:
        if arr[x+1][y] == 0:
            arr[x+1][y] = 9
            x += 1
        elif arr[x+1][y] == 1:
            break
        elif arr[x+1][y] == 2:
            arr[x+1][y] = 9
            break
    
for i in arr:
    for j in i:
        print(j, end = ' ')
    print()
print()