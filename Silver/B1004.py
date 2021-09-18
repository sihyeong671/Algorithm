# 어린왕자

import sys
T = int(input())
for t in range(T):
    start_x, start_y, end_x, end_y = map(int, sys.stdin.readline().split())

    n = int(sys.stdin.readline())

    planets = []
    for _ in range(n):
        planets.append(tuple(map(int, sys.stdin.readline().split())))
    cnt = 0
    for cx, cy, r in planets:
        # 출발 , 도착 원안에 있는 경우
        r_start = (abs(start_x-cx)**2 + abs(start_y-cy)**2)**0.5
        r_end = (abs(end_x-cx)**2 + abs(end_y-cy)**2)**0.5

        if r_start < r < r_end:
            cnt += 1
        elif r_start > r > r_end:
            cnt += 1

    print(cnt)





