# 버블소트

import sys

input = sys.stdin.readline

N = int(input())
arr = []

for i in range(N):
    n = int(input())
    arr.append((n, i))

ans = 0
arr.sort()
for idx, (num, pre_idx) in enumerate(arr):
    ans = max(ans, pre_idx - idx)

print(ans+1)
