# 메모리 초과
from itertools import permutations

N = int(input())
arr = tuple(map(int, input().split()))

lst = [i+1 for i in range(N)]
p = list(permutations(lst, N))
for idx, i in enumerate(p):
    if i == arr:
        if idx == 0:
            print("-1")
            break
        else:
            for k in p[idx-1]:
                print(k, end=" ")
