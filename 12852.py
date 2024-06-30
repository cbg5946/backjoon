N = int(input())

dp = [0]*(10**6+1)

dp[1] = 0

for i in range(2, N+1):
    dp[i] = dp[i-1]+1
    
    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i%3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[N])
while True:
    if N == 1:
        print(N)
        break
    if dp[N-1] == dp[N]-1:
        print(N, end = ' ')
        N -= 1
    if N % 2 == 0 and dp[N//2] == dp[N]-1:
        print(N, end = ' ')
        N //= 2
    if N % 3 == 0 and dp[N//3] == dp[N]-1:
        print(N, end = ' ')
        N //= 3