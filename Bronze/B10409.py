# 서버

n, T = map(int, input().split())

arr = list(map(int, input().split()))

S = 0
cnt = 0
for i in range(n):
    S += arr[i]
    if S > T:
        break
    cnt += 1

print(cnt)


