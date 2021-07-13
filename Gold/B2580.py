# 스도쿠

import sys

def dfs(arr, x, y):
    # 종료 조건
    if x == 8 and y == 8:
        return

    # 가능한 숫자 리스트
    lst = [i for i in range(1, 10)]
    if arr[x][y] == 0:
        for c in range(9):
             

    # 행 체크
    # 열 체크
    # 칸 체크








arr = []
for _ in range(9):
    arr.append(list(map(int, sys.stdin.readline().split())))

dfs(arr, 0, 0)

# 행 체크, 열 체크, 칸 단위 체크
