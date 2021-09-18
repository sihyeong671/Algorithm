#  분산처리

import sys
T = int(sys.stdin.readline())

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    lst = [str(a)[-1]]
    while True:
        if lst[0] == str(int(lst[-1][-1])*a)[-1]:
            break
        else:
            lst.append(str(int(lst[-1][-1])*a)[-1])
    index = b % len(lst)
    if lst[index-1] == '0':
        print(10)
    else:
        print(lst[index-1])