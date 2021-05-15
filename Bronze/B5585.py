# 거스름 돈
N = int(input())
N = 1000 - N
count = 0
while N != 0:
    if N >= 500:
        count += N // 500
        N %= 500
    elif N >= 100:
        count += N // 100
        N %= 100
    elif N >= 50:
        count += N // 50
        N %= 50
    elif N >= 10:
        count += N // 10
        N %= 10
    elif N >= 5:
        count += N // 5
        N %= 5
    else:
        count += N
        N = 0
print(count)







