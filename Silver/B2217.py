# 로프

N = int(input())
ropes = []
for _ in range(N):
    ropes.append(int(input()))

ropes.sort(reverse=True)
for i in range(1, N+1):
    ropes[i-1] *= i

print(max(ropes))