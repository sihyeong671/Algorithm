# 쉽게 푸는 문제

lst = []

for i in range(1, 51):
    for _ in range(i):
        lst.append(i)

a, b = map(int, input().split())
print(sum(lst[a-1:b]))

