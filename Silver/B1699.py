# 제곱수의 합
N = int(input())
dp = [0]*100001
# s = [i**2 for i in range(1, 317)]
for i in range(1, N+1):
    # temp = []
    # for j in s:
    #     if j > i:
    #         break
    #     temp.append(dp[i-j])
    # dp[i] = min(temp) + 1
    j = 1
    while True:
        if (i - (j**2)) < 0:
            break
        if j > 1:
            dp[i] = min(dp[i], dp[i - (j**2)] + 1)
            j += 1
        else:
            dp[i] = dp[i - (j**2)] + 1
            j += 1
print(dp[N])

