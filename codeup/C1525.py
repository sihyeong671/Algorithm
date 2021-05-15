# 제출결과 실패 확인 필요
import copy
arr = []
for _ in range(10):
    arr.append(list(map(int, input().split())))
n = int(input())
player = []
for i in range(n):
    r, c = map(int, input().split())
    player.append((r, c))
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
arr_2 = copy.deepcopy(arr)
for i in range(10):
    for j in range(10):
        if arr_2[i][j] >= 1:
            temp = arr_2[i][j]
            for x, y in zip(dx, dy):
                arr[i][j] = -2
                for k in range(1, temp+1):
                    cx = i + (k * x)
                    cy = j + (k * y)
                    if (0 <= cx < 10) and (0 <= cy < 10):
                        if arr_2[cx][cy] == -1:
                            break
                        else:
                            arr[cx][cy] = -2
for idx, (x, y) in enumerate(player):
    if arr[x-1][y-1] == 0:
        arr[x-1][y-1] = idx+1
for i in range(10):
    for j in range(10):
        print(arr[i][j], end=" ")
    print("")
print("Character Information")
for idx, (x, y) in enumerate(player):
    if arr[x-1][y-1] == -2:
        print(f"player {idx+1} dead")
    else:
        print(f"player {idx+1} survive")
