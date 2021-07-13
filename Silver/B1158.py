# 요세푸스 문제

N, K = map(int, input().split())
lst = [i+1 for i in range(N)]
idx = 0
arr = []
while lst:
    idx += (K - 1)
    if idx > len(lst)-1:
        idx %= len(lst)
    arr.append(str(lst.pop(idx)))

print('<' + ', '.join(arr) + '>')

