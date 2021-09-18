# 랜선자르기


import sys
K, N = map(int, input().split())

lst = []
for _ in range(K):
    lst.append(int(sys.stdin.readline()))


start = 1
end = max(lst)

while True:
    if start > end:
        break
    cnt = 0
    mid = (start + end) // 2
    for n in lst:
        cnt += (n//mid)

    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)



