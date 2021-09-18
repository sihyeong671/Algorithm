# 직각삼각형

while True:
    length = list(map(int, input().split()))
    length.sort()
    if length[0] == 0:
        break
    if length[0]**2 + length[1]**2 == length[2]**2:
        print('right')
    else:
        print('wrong')
