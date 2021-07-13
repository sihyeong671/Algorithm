# 최단 경로
import sys
import heapq


V, E = map(int, input().split())
K = int(input())

arr = [[] for _ in range(V)]
INF = sys.maxsize
distance = [INF]*V

for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    arr[u-1].append((w, v-1))

distance[K-1] = 0
q = []
heapq.heappush(q, (0, K-1))

while q:

    cost, current_node = heapq.heappop(q)

    if distance[current_node] < cost:
        continue

    for c, next_node in arr[current_node]:
        next_cost = cost + c
        if next_cost < distance[next_node]:
            distance[next_node] = next_cost
            heapq.heappush(q, (next_cost, next_node))

for d in distance:
    print('INF' if d == INF else d)



