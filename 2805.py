N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 1
end = max(trees)

max_tree = 0
while start <= end:
    mid = (start + end)//2
    
    sum = 0
    for tree in trees:
        if tree > mid:
            sum += (tree - mid)
    
    if sum >= M:
        max_tree = max(mid, max_tree)
        start = mid + 1
    else:
        end = mid - 1
        
print(max_tree)