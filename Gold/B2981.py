# 검문
# def gcd(n1, n2):
#     while n2 != 0:
#         n1, n2 = n2, (n1 % n2)
#     return n1
#
# N = int(input())
# arr = []
# for _ in range(N):
#     arr.append(int(input()))
# arr.sort()
#
# ans = arr[1]-arr[0]
# for i in range(2, N):
#     ans = gcd(ans, arr[i] - arr[i-1])
#
# for i in range(2, ans//2 + 1):
#     if ans % i == 0:
#         print(i, end=" ")
# print(ans) # 자기자신 출력하기위한 print

import sys

def gcd(n1, n2):
    while n2 != 0:
        n1, n2 = n2, (n1 % n2)
    return n1

N = int(input())

arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
arr.sort()

ans = arr[1]-arr[0]
for i in range(2, N):
    ans = gcd(ans, arr[i] - arr[i-1])

lst_1 = []
lst_2 = [ans]
for i in range(2, int(ans ** 0.5) + 1):
    if ans % i == 0:
        lst_1.append(i)
        if i != ans//i:
            lst_2.append(ans // i)
for i in range(len(lst_1)):
    sys.stdout.write(str(lst_1[i]) + ' ')
for i in range(len(lst_2)-1, -1, -1):
    sys.stdout.write(str(lst_2[i]) + ' ')






