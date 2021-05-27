# 주몽
import sys
N = int(input())
M = int(input())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
one = 0
two = len(lst)-1
count = 0
while one < two:
    if lst[one] + lst[two] == M:
        one += 1
        two -= 1
        count += 1
    elif lst[one] + lst[two] > M:
        two -= 1
    else:
        one += 1
print(count)

# 개수만 세는 코드이기 때문에 브루트포스 필요없음 + 전부 다 다름