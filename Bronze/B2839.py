# 설탕배달

N = int(input())

# 3x + 5y

for i in range(N // 3 + 1):
    if N % 5 == 0:
        print(i + N//5)
        break
    N = N - 3
    if N < 0:
        print(-1)
