# 회의실 배정
import sys

# 입력
arr = []
N = int(input())
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    arr.append((a, b))
arr.sort(key=lambda x: (x[1], x[0]))
cnt = 1
end = arr[0][1]
for idx in range(1, len(arr)):
    if end <= arr[idx][0]:
        end = arr[idx][1]
        cnt += 1

print(cnt)

# 오류
# import sys
#
# # 입력
# arr = []
# N = int(input())
# for _ in range(N):
#     a, b = map(int, sys.stdin.readline().split())
#     arr.append((a, b))
# arr.sort(key=lambda x: (x[0], x[1]))
# cnt = 1
# end = arr[0][1]
# for idx in range(1, len(arr)):
#     if arr[idx][1] < end:
#         end = arr[idx][1]
#         cnt = 1
#     elif end <= arr[idx][0]:
#         end = arr[idx][1]
#         cnt += 1
#
# print(cnt)

