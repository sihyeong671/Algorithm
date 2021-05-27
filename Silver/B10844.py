# 쉬운 계단 수
N = int(input())
dp = [[0]*10 for _ in range(N)]
for i in range(N):
    if i == 0:
        for k in range(1, 10):
            dp[i][k] = 1
    else:
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][j+1]
            elif j == 9:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j+1] + dp[i-1][j-1]
print(sum(dp[N-1]) % 1000000000)



