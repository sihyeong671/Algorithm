# 자두나무

T, W = map(int, input().split())
T_arr = []
lst = []
for _ in range(T):
    T_arr.append(int(input()))

i = 1
j = 0
while i != len(T_arr) - 1:
    if T_arr[j] != T_arr[i]:
        lst.append(len(T_arr[j:i]))
        j = i
        i += 1
        if i == len(T_arr) - 1:
            lst.append(len(T_arr[j:i+1]))
    else:
        i += 1
        if i == len(T_arr) - 1:
            lst.append(len(T_arr[j:i+1]))

dp = [[0]*(W+1) for _ in range(len(lst))]

print(lst)
print(dp)


