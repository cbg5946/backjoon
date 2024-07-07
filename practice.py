a, b = map(int, input().split())

arr = []
for i in range(a, b+1):
    arr.append(i)
print(arr)
for i in arr:
    if i == 1:
        arr.remove(i)
    else:
        print(arr)
        for j in range(2, int(i**(1/2)+1)):
            if i%j == 0:
                arr.remove(i)
                break
print(arr)
print(sum(arr), min(arr))

