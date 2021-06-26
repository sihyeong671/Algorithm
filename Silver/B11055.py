# 가장 큰 증가 부분 수열

N = int(input())
arr = list(map(int, input().split()))
dp = arr[:]
for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[j]+arr[i], dp[i])
print(max(dp))






