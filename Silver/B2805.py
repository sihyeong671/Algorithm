# 나무 자르기

import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
h_1, h_2 = 0, max(trees)
ans = 0
while h_1 <= h_2:
    H = (h_1 + h_2) // 2

    h = 0
    for tree in trees:
        if tree > H:
            h += (tree - H)
    if h >= M:
        h_1 = H + 1
    else:
        h_2 = H - 1

print(h_2)


