# 치즈
from collections import deque

r, c = map(int, input().split())

arr = []
for _ in range(r):
    arr.append(list(map(int, input().split()))) # 입력

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

check = True
cnt = 0
num = 0
while check:
    temp = 0
    bool_arr = [[False]*c for _ in range(r)]
    cnt += 1
    dq = deque()
    dq.append([0, 0])
    bool_arr[0][0] = True
    while len(dq) != 0:
        cord = dq.popleft()
        for i in range(4):
            dr = cord[0] + dy[i]
            dc = cord[1] + dx[i]
            if 0 <= dr < r and 0 <= dc < c: # 배열 안에 있는지 확인
                if arr[dr][dc] == 1:
                    arr[dr][dc] = 2
                elif arr[dr][dc] == 0 and not bool_arr[dr][dc]:
                    dq.append([dr, dc])
                    bool_arr[dr][dc] = True
    check = False
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 2:
                temp += 1
                arr[i][j] = 0
            if arr[i][j] == 1:
                check = True
    if not check:
        num = temp

print(cnt)
print(num)





