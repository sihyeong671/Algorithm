# 파도반 수열

T = int(input())
lst = [1, 1, 1, 2, 2]
for i in range(4, 100):
    lst.append(lst[i] + lst[i-4])

for _ in range(T):
    N = int(input())
    print(lst[N-1])


