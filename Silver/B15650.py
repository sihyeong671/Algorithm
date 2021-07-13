# N과 M(2)
import sys


def dfs(arr, n):
    if n == N:
        for j in range(N):
            sys.stdout.write(str(arr[j]+1) + ' ')
        sys.stdout.write('\n')
        return

    for i in range(M):
        if i not in arr:
            if n == 0:
                arr.append(i)
                dfs(arr, n+1)
                arr.pop()
            elif i > arr[n-1]:
                arr.append(i)
                dfs(arr, n + 1)
                arr.pop()


M, N = map(int, input().split())
lst = []
dfs(lst, 0)

