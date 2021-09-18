# 수 정렬하기

import sys
N = int(input())
lst = []
for _ in range(N):
    lst.append(int(sys.stdin.readline()))

lst.sort()
for i in lst:
    sys.stdout.write(str(i)+'\n')

