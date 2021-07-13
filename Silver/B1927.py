# 최소 힙
import sys
import heapq

N = int(input())
heap = []
for i in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(heap) == 0:
            sys.stdout.write('0\n')
        else:
            temp = heapq.heappop(heap)
            sys.stdout.write(str(temp)+'\n')
    else:
        heapq.heappush(heap, x)
