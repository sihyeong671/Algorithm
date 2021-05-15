arr = []
for _ in range(9):
    arr.append(list(map(int,input().split())))

r, c = map(int, input().split())
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [1, 1, 1, 0, 0, -1, -1, -1]

check = 0
if arr[r-1][c-1] == 1:
    print(-1)
    exit()
for x, y in zip(dx, dy):
    cx = (r-1) + x
    cy = (c-1) + y
    if (0 <= cx < 9) and (0 <= cy < 9):
        if arr[cx][cy] == 1:
            check += 1
print(check)


