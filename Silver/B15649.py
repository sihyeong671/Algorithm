# N과 M (1)
import sys


def dfs(arr, num):
    if num == M:
        for i in range(M):
            sys.stdout.write(str(arr[i]+1) +' ')
        sys.stdout.write('\n')
        return

    for i in range(N):
        if i not in lst:
            arr.append(i)
            dfs(arr, num+1)
            arr.pop()

N, M = map(int, input().split())
lst = []
dfs(lst, 0)
