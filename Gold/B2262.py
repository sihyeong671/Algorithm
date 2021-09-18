# 토너먼트 만들기


n = int(input())
arr = list(map(int, input().split()))
ans = 0
for _ in range(n-1):

    max_value = max(arr)
    max_index = arr.index(max_value)

    if max_index == 0:
        ans += (arr[max_index] - arr[max_index + 1])
    elif max_index == (len(arr) - 1):
        ans += (arr[max_index] - arr[max_index - 1])
    else:
        if max_value - arr[max_index - 1] < max_value - arr[max_index + 1]:
            ans += (max_value - arr[max_index - 1])
        else:
            ans += (max_value - arr[max_index + 1])

    arr.remove(max_value)

print(ans)
