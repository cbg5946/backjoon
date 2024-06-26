T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if (x2-x1)**2 + (y2-y1)**2 == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if (x2-x1)**2 + (y2-y1)**2 < (r2 - r1)**2:
            print(0)
        elif (x2-x1)**2 + (y2-y1)**2 > (r2 + r1)**2:
            print(0)
        elif (x2-x1)**2 + (y2-y1)**2 == (r2 - r1)**2:
            print(1)
        elif (x2-x1)**2 + (y2-y1)**2 == (r2 + r1)**2:
            print(1)
        else:
            print(2)