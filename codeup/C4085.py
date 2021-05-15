m, n, x, y = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

sum_ = 0
for i in range(n-y+1):
    for j in range(m-x+1):
        temp = 0
        for w in range(y):
            temp += sum(arr[i+w][j:j+x])
        sum_ = max(temp, sum_)
print(sum_)