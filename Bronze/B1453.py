# 피시방 알바

N = int(input())
lst = [0]*100
arr = list(map(int, input().split()))
rejected = 0
for i in arr:
    if lst[i-1] == 0:
        lst[i-1] = 1
    else:
        rejected += 1
print(rejected)
