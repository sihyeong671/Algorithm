# 완전 이진 트리

# 이중for문으로 간단하게도 풀 수 있음
from collections import deque

K = int(input())
arr = list(map(int, input().split()))
start = 0
end = len(arr)-1
cnt = 0
q = deque()
q.append((start, end, 1))
while q:
    s, e, d = q.popleft()
    cnt += 1
    mid = (s+e)//2
    print(arr[mid], end=" ")
    if d == K:
        continue
    if cnt == (2**d)-1:
        print()
    q.append((s, mid-1, d+1))
    q.append((mid+1, e, d+1))


