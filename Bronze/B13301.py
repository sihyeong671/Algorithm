# 타일 장식물

N = int(input())
lst = [1, 1]

if N == 1:
    print(4)
elif N == 2:
    print(6)
else:
    for i in range(2, N):
        lst.append(lst[-1] + lst[-2])
    print(lst[-1] * 4 + lst[-2] * 2)