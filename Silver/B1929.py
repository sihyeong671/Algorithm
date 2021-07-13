# 소수 구하기
import math
import sys
M, N = map(int, input().split())

num = [i for i in range(N+1)]
num[0] = num[1] = -1
for n in range(2, int(math.sqrt(len(num)))+1):
    if num[n] != -1:
        for i in range(n * 2, len(num), n):
            # if num[i] % num[n] == 0:
            num[i] = -1
for i in range(M, N+1):
    if num[i] != -1:
        # print(num[i])
        sys.stdout.write(str(num[i])+'\n')


