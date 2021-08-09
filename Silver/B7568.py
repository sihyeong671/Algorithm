# 덩치

N = int(input())

person = []
for _ in range(N):
    w, h = map(int, input().split())
    person.append((w, h))

ans = [1]*N

for i in range(N):
    for j in range(N):
        if person[i][1] < person[j][1] and person[i][0] < person[j][0]:
            ans[i] += 1

print(*ans)
# idx = 0
# rank = [0]*N
# while idx < N:
#     for i in range(N):
#         if ans[i] == idx:
#             rank[i] += (idx+1)
#     idx += 1
#
# print(*rank)
