X, Y = map(int, input().split())

Z = (Y * 100) // X
# 이분 탐색 left right
# int 타입 캐스팅은 부동 소수점 오차에 의해 틀린 답이 나옴
cnt = 0
left = 0
right = X
num = X
if Z >= 99:
    print(-1)
else:
    while left <= right:
        mid = (left + right) // 2
        if ((Y+mid)*100) // (X+mid) > Z:
            num = mid
            right = mid - 1
        else:
            left = mid + 1
    print(num)