# N-Queen

def dfs(arr, n, row):
    global count

    if row == n:
        count += 1
        return

    for col in range(n): # 전체 열 하나씩 확인
        arr[row] = col
        for x in range(row):
            if arr[x] == arr[row]: # 겹치는 열 확인
                break
            elif abs(arr[x]-arr[row]) == (row - x): # 대각선 겹치는지 확인
                break
        else:
            dfs(arr, n, row+1)

N = int(input())
lst = [0]*N
count = 0
dfs(lst, N, 0)
print(count)