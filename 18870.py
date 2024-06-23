N = int(input())

array = list(map(int, input().split()))

sort_array = set(array)
sort_array = list(sort_array)
sort_array.sort()

dic = {}
for i in range(len(sort_array)):
    dic[sort_array[i]] = i

for i in array:
    print(dic[i], end = ' ')