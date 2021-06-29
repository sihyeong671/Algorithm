# 가장 긴 바이토닉 부분 수열
N = int(input())

arr = list(map(int, input().split()))
arr_ = arr[::-1]
dp_a = [1]*len(arr)
dp_d = [1]*len(arr)

for i in range(len(arr)):
    for j in range(i):
        if arr[i] > arr[j]:
            dp_a[i] = max(dp_a[i], dp_a[j]+1)
    for k in range(i):
        if arr_[i] > arr_[k]:
            dp_d[i] = max(dp_d[i], dp_d[k]+1)

dp = []
for i in range(N):
    dp.append(dp_a[i]+dp_d[N-i-1] - 1)
print(max(dp))