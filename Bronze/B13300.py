# 방 배정
import sys

N, K = map(int, sys.stdin.readline().split())
students = [[0]*2 for _ in range(6)]
for _ in range(N):
    S, Y = map(int, sys.stdin.readline().split())
    students[Y-1][S] += 1

room = 0
for i in range(2):
    for j in range(6):
        room += students[j][i] // K
        if students[j][i] % K != 0:
            room += 1
print(room)
