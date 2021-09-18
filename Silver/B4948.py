# 베르트랑 공준

# prime = []
# lst = [i for i in range(246913)]
# # 1 ~ 123456*2
# for j in range(2, int(246912**0.5)+1):
#     if lst[j] != 0:
#         for k in range(j*2, 246913, j):
#             lst[k] = 0
# lst[1] = 0
# for i in lst:
#     if i != 0:
#         prime.append(i)
#
# while True:
#     cnt = 0
#     n = int(input())
#     if n == 0:
#         break
#     for i in prime:
#         if n < i <= n*2:
#             cnt += 1
#     print(cnt)


is_prime = [1]*246913
is_prime[0] = is_prime[1] = 0
# 1 ~ 123456
for i in range(2, int(246912**0.5)+1):
    if is_prime[i] == 1:
        for j in range(i*2, 246913, i):
            is_prime[j] = 0
while True:
    n = int(input())
    if n == 0:
        break
    print(sum(is_prime[n+1:n*2+1]))


