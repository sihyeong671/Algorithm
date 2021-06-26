# 피보나치 수

# N = int(input())
# for _ in range(N):
#     T = int(input())
#     if T == 0:
#         print(1, 0)
#     elif T == 1:
#         print(0, 1)
#     else:
#         arr = [(1, 0), (0, 1)]
#         for i in range(T-1):
#             temp = (arr[-1][0] + arr[-2][0], arr[-1][1] + arr[-2][1])
#             arr.append(temp)
#
# print(arr)

arr = [(1, 0), (0, 1)]
for i in range(39):
    temp = (arr[-1][0] + arr[-2][0], arr[-1][1] + arr[-2][1])
    arr.append(temp)
N = int(input())
for i in range(N):
    T = int(input())
    print(arr[T][0], arr[T][1])


