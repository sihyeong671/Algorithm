# 정사각형
import sys
T = int(input())

for _ in range(T):
    arr = []
    for i in range(4):
        arr.append(list(map(int, sys.stdin.readline().split())))

    arr.sort(key=lambda x:(x[0], x[1]))
    # 대각선 길이
    # 네 변의 길이
    # if arr[0][0] - arr[3][3] == arr[1][1] + arr[2][2]
