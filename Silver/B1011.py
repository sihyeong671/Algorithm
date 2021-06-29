# Fly me to the Alpha Centauri
from math import sqrt

T = int(input())

for i in range(T):
    x, y = map(int, input().split())
    r = y - x
    temp = round(sqrt(r)) # 가장 가까운 제곱수의 제곱근
    num = temp*2 - 1 # 가장 가까운 제곱수의 이동 횟수
    if temp**2 < r:
        print(num + 1)
    else:
        print(num)
