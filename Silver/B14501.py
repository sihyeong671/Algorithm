# 퇴사

import sys
input = sys.stdin.readline

N = int(input())

arr = []
for _ in range(N):
    arr.append(tuple(map(int, input().split())))

dp = [0]*N

for i in range(N):
    if i + arr[i][0] > N: # 현재 날짜 + 상담일수가 퇴사일 초과하는 경우
        continue

    dp[i] += arr[i][1]
    j = 0
    while True:
        if i + arr[i][0] + j > N - 1:
            break
        dp[i+arr[i][0]+j] = max(dp[i+arr[i][0]+j], dp[i])
        j += 1
print(max(dp))









