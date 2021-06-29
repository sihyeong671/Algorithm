# 터렛

import math

T = int(input())
for i in range(T):
    x_1, y_1, r_1, x_2, y_2, r_2 = map(int, input().split())
    r = math.sqrt((x_1 - x_2)**2 + (y_1 - y_2)**2)
    lst = [r, r_1, r_2]
    lst.sort()
    if r == 0: # 좌표 같은 경우
        if r_1 == r_2:
            print(-1) # 겹칠 때
        else:
            print(0) # 안 겹칠 때
    elif lst[2] < lst[1] + lst[0]:
        print(2)
    elif r_1 + r_2 == r or r + r_1 == r_2 or r + r_2 == r_1:
        print(1)
    else:
        print(0)



