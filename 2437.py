n = int(input())

arr = list(map(int, input().split()))
arr.sort()
sum = 1

for i in arr:
    if sum < i:
        break
    
    sum += i

print(sum)