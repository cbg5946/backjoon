n = int(input())
arr = list(map(int, input().split()))    
lastIdx = len(arr) - 1
c = 0
swapped  = True
i = 0
while swapped: 
    swapped = False
    for j in range(i, lastIdx-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            c += 1
            swapped = True

    if swapped:
        for j in range(lastIdx-i, i, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                c += 1
                swapped = True
    
    i = i + 1
print(c)