# 제곱 ㄴㄴ 수
from math import ceil

m, M = map(int, input().split())

# 인덱스 신경쓰기 귀찮으니 이렇게 만들어준다
lst = [i for i in range(M+1)]
prime = []
for i in range(2, int(M**0.5)+1):
    if lst[i] != 0:
        for j in range(i*2, M+1, i):
            lst[j] = 0
    prime.append(i**2)

ans = [i for i in range(m, M+1)]
cnt = 0
for i in range(len(prime)):
    for j in range(len(ans)):
        if ans[j] % prime[i] == 0:
            cnt += 1
print(M - cnt)











