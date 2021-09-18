# 요세푸스 문제 0

from collections import deque

N, K = map(int, input().split())

arr = deque([i for i in range(1, N+1)])
ans = []
cnt = 1
while arr:
    if cnt % K == 0:
        ans.append(str(arr.popleft()))
    else:
        arr.append(arr.popleft())
    cnt += 1

print('<' + ', '.join(ans) + '>')
# print(', '.join(ans))

