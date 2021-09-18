# 회전초밥

import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushi = []
arr = [0]*3001
arr[c] = 1
for i in range(N):
    s = int(input())
    sushi.append(s)
    if i < k:
        arr[s] += 1
cnt = 0
for i in arr:
    if i != 0:
        cnt += 1
ans = cnt
for i in range(k, N+k):
    if i > N-1:
        i %= N
    arr[sushi[i-k]] -= 1
    if arr[sushi[i-k]] == 0:
        cnt -= 1
    arr[sushi[i]] += 1
    if arr[sushi[i]] == 1:
        cnt += 1
    ans = max(cnt, ans)

print(ans)