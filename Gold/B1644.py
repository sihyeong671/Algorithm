# 소수의 연속합

N = int(input())
lst = [True]*(N+1)
lst[1] = False

for i in range(2, int(N**0.5)+1):
    if lst[i]:
        for j in range(i*2, N+1, i):
            lst[j] = False

prime = []
for k in range(1, N+1):
    if lst[k]:
        prime.append(k)
ans = 0

p_1 = 0
p_2 = 1
while True:
    if p_1 > p_2 or p_2 > len(prime):
        break

    temp = sum(prime[p_1:p_2])
    if temp == N:
        ans += 1
        p_2 += 1
    elif temp < N:
        p_2 += 1
    elif temp > N:
        p_1 += 1

print(ans)
