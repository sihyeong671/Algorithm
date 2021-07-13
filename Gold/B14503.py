# 로봇 청소기

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

nr = [1, -1, 0, 0]
nc = [0, 0, -1, 1]
cnt = 1
while True:
    # 청소하기
    check = False
    arr[r][c] = 2
    # 모든 방향이 청소 or 벽 확인
    for i in range(4):
        dr = r + nr[i]
        dc = c + nc[i]
        if arr[dr][dc] == 0:
            check = True

    # 뒤가 벽인지 확인
    if not check:
        if d == 0:
            if arr[r+1][c] == 1:
                break
            else:
                r += 1
        elif d == 1:
            if arr[r][c-1] == 1:
                break
            else:
                c -= 1
        elif d == 2:
            if arr[r-1][c] == 1:
                break
            else:
                r -= 1
        elif d == 3:
            if arr[r][c+1] == 1:
                break
            else:
                c += 1
        continue
    # 청소하지 않은 공간
    if d == 0:
        # 움직일 곳이 벽이 아니고 방문 안했을 경우
        if arr[r][c-1] == 0:
            c -= 1 # 이동
            d = 3 # 서쪽보기
            cnt += 1
        else: # 벽이거나 방문 했을 경우
            d = 3
    elif d == 1:
        if arr[r-1][c] == 0:
            r -= 1 # 이동
            d = 0 # 북쪽보기
            cnt += 1
        else: # 벽이거나 방문 했을 경우
            d = 0
    elif d == 2:
        if arr[r][c+1] == 0:
            c += 1 # 이동
            d = 1 # 동쪽보기
            cnt += 1
        else: # 벽이거나 방문 했을 경우
            d = 1
    elif d == 3:
        if arr[r+1][c] == 0:
            r += 1 # 이동
            d = 2 # 남쪽보기
            cnt += 1
        else: # 벽이거나 방문 했을 경우
            d = 2
print(cnt)
