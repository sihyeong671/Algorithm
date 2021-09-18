# 신입사원

import sys

T = int(input())

for _ in range(T):
    N = int(sys.stdin.readline())
    lst = []
    cnt = 1
    for i in range(N):
        a, b = map(int, sys.stdin.readline().split())
        lst.append([a, b])

    lst.sort(key=lambda x: x[0])
    m = lst[0][1]
    for i in range(1, N):
        if lst[i][1] < m:
            cnt += 1
            m = lst[i][1]
    print(cnt)

