# 피보나치와 수열과 쿼리
import sys
N = int(sys.stdin.readline())
Fibo = [1, 1]
for i in range(2, N+1):
    Fibo.append(Fibo[-1] + Fibo[-2])
Q = int(sys.stdin.readline())
lst = [0]*N
for _ in range(Q):
    l, r = map(int, sys.stdin.readline().split())
    for i in range(l-1, r):
        lst[i] += Fibo[i-l+1]

for j in range(len(lst)):
    lst[j] = int((lst[j] * Fibo[j]) % (10e9 + 7))

for i in lst:
    if i == lst[-1]:
        sys.stdout.write(str(i))
    else:
        sys.stdout.write(str(i)+' ')
