# 제로

import sys
K = int(input())

lst = []

for _ in range(K):
    n = int(sys.stdin.readline())
    if n != 0:
        lst.append(n)
    else:
        lst.pop()

print(sum(lst))
