n, k = map(int, input().split())

arr = list(map(int, input().split()))

def quick(s, e, k):
    global arr
    if s < e:
        pivot = partition(s, e)
        if pivot == k:
            return
        elif k < pivot:
            quick(s, pivot-1, k)
        else:
            quick(pivot+1, e, k)

def partition(s, e):
    global arr
    
    if s+1 == e:
        arr[s], arr[e] = arr[e], arr[s]
        return e

    m = (s+e)//2
    arr[s], arr[m] = arr[m], arr[s]
    pivot = arr[s]
    i = s+1
    j = e

    while i <= j:
        while pivot < arr[j] and j > 0:
            j -= 1
        while pivot > arr[i] and i < len(arr)-1:
            i += 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    
    
    arr[s], arr[j] = arr[j], arr[s]
    return j

quick(0, n-1, k-1)
print(arr[k-1])