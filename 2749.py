n = int(input())
arr = [0, 1]

i, j = 0, 1
while True:
    arr.append((arr[i]+arr[j])%1000000)
    if arr[-2] == 0 and arr[-1] == 1:
        break
    i += 1
    j += 1
n %= j
print(arr[n])
