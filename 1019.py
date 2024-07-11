N = int(input())

arr = [[] for _ in range(11)]

for i in range(1, 11):
    tmp = i
    s = '0'
    while tmp > 1:
        s += str(tmp-1)
        tmp -= 1
    s = int(s)
    arr[i].append(s*9)
    for _ in range(9):
        arr[i].append(i*(10**(i-1)))

res = [0]*10

k = 1
while N >= 10:
    N_length = len(str(N))
    N_arr = []
    tmp_arr = []
    tmp_num = 10**(N_length-k) - 1
    first_num = 0
    while True:
        next = tmp_num + 10**(N_length-k)
        if next > N:
            break
        first_num += 1
        tmp_num = next
    a = arr[N_length-k][1]
    for i in range(0, 10):
        if i == 0:
            res[i] += arr[N_length-k][0]+(first_num*a)
        elif i <= first_num:
            res[i] += 10**len(str(a)) + a*(first_num+1)
        else:
            res[i] += a*(first_num+1)
    if N > tmp_num:
        tmp_num += 1
        for i in str(tmp_num):
            res[int(i)] += 1
    N -= tmp_num
    res[int(str(tmp_num)[0])] += N
    if N > 0:
        tmp_n = N
        tmp_nn = N
        len_n = len(str(tmp_num))-1
        l = 1
        while tmp_nn//(10**l):
            len_n -= 1
            res[0] += len_n*(10**l - 10**(l-1))
            tmp_n -= (10**l - 10**(l-1))
            l += 1   
        if tmp_n > 0:
            res[0] += (len_n-1)*tmp_n
if N > 0:
    for i in range(1, N+1):
        res[i] += 1
for i in res:
    print(i, end = ' ')