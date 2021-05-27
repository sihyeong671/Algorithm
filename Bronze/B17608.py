# 막대기
import sys

N = int(input())
lst = []
for i in range(N):
    if i == 0:
        lst.append(int(sys.stdin.readline()))
        continue
    t = int(sys.stdin.readline())
    while t >= lst[-1]:
        lst.pop()
        if len(lst) == 0:
            break
    lst.append(t)
print(len(lst))
