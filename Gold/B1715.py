from heapq import heappush, heappop

N = int(input())


heap = []
for _ in range(N):
    num = int(input())     
    heappush(heap, num)
    
ans = 0
if N > 1:
    for _ in range(N-1, 0, -1):
        num_1 = heappop(heap)
        num_2 = heappop(heap)
        result = num_1 + num_2
        ans += result
        heappush(heap, result)
        
print(ans)