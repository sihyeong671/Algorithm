# 도서관

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

position = list(map(int, input().split()))

lst_1 = [] # 가장 거리가 먼 책이 있는 리스트
lst_2 = []

position.sort()
if abs(position[0]) > position[-1]: # 음수 좌표 책의 거리가 큰 경우
    for i in position:
        if i < 0:
            lst_1.append(abs(i))
        else:
            lst_2.append(i)
else:
    for i in position:
        if i > 0:
            lst_1.append(i)
        else:
            lst_2.append(abs(i))

lst_1.sort(reverse=True)
lst_2.sort(reverse=True)

distance = 0
for i in range(0, len(lst_1), M):
    if i == 0:
        distance += lst_1[i]
    else:
        distance += lst_1[i]*2

for i in range(0, len(lst_2), M):
    distance += lst_2[i]*2

print(distance)




