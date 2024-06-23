N = int(input())

arr = list(map(int, input().split()))
x = int(input())

arr.sort()

a, b = 0, N-1
count = 0
while a < b:
    sum = arr[a] + arr[b]
    if sum <= x:
        if sum == x:
            count += 1
        a += 1
    elif sum >= x:
        if sum == x:
            count += 1
        b -= 1

print(count)