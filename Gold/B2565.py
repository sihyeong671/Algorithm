N = int(input())
lst = []
for i in range(N):
    _a, _b = map(int, input().split())
    lst.append([_a, _b])

dp = [1] * N

lst.sort()

for i in range(N):
    for j in range(i):
        if lst[i][1] > lst[j][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(N-max(dp))



