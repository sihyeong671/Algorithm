# 골드바흐의 추측


# prime = []
# lst = [i for i in range(10001)]
# lst[1] = 0
# for i in range(int(10000**0.5)+1):
#     if lst[i] != 0:
#         for j in range(i*2, 10001, i):
#             lst[j] = 0
#
# for n in lst:
#     if n != 0:
#         prime.append(n)
#
# T = int(input())
# ans_1 = 0
# ans_2 = 0
# for _ in range(T):
#     even = int(input())
#     for i in range(len(prime)):
#         if prime[i] > even:
#             break
#         for j in range(i, len(prime)):
#             if prime[i] + prime[j] == even:
#                 ans_1 = prime[i]
#                 ans_2 = prime[j]
#             elif prime[i] + prime[j] > even:
#                 break
#     print(ans_1, ans_2)


prime = [False, False]+[True]*9999
for i in range(2, int(10000**0.5)+1):
    if prime[i]:
        for j in range(2*i, 10001, i):
            prime[j] = False

T = int(input())
for _ in range(T):
    even = int(input())

    index_1 = index_2 = even//2

    while True:
        if prime[index_1] and prime[index_2]:
            print(index_1, index_2)
            break
        index_1 -= 1
        index_2 += 1








