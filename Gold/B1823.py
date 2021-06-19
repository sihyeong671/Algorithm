# 수확
import sys
N = int(sys.stdin.readline())
arr = [0]
for i in range(N):
    arr.append(int(sys.stdin.readline()))
arr += [0]
lst = [[0]*(N+2) for i in range(N+2)]

ans = []
for count in range(1, N+2):
    for n in range(1, count+1):
        # print(n, N-count+n)
        lst[n][N-count+n] = max(lst[n-1][N-count+n]+arr[n-1]*(count-1), lst[n][N-count+n+1]+arr[N-count+n+1]*(count-1))
        if count - 1 == N:
            ans.append(lst[n][N-count+n])

# for i in range(N+2):
#     for j in range(N+2):
#         print(lst[i][j], end=" ")
#     print("")
print(max(ans))
