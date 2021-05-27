# 동전 2
import sys
n, k = map(int, sys.stdin.readline().split())
price = []
for _ in range(n):
    price.append(int(sys.stdin.readline()))

dp = [0]*100001
for i in range(1, k+1):
    temp = []
    for j in price:
        if i - j < 0:
            continue
        else:
            if dp[i-j] == -1:
                continue
            temp.append(dp[i-j]+1)
    if len(temp) == 0:
        dp[i] = -1
    else:
        dp[i] = min(temp)

print(dp[k])
