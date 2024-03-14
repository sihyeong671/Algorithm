N = int(input())

costs = [[] for _ in range(N)]
for i in range(N):
    r, g, b = map(int, input().split())
    costs[i] = [r, g, b]
    
answers = []

for idx, cost in enumerate(costs):
    if idx == 0:
        continue
    
    for j in range(3):
        
        if j == 0:
            costs[idx][j] = min(cost[j] + costs[idx-1][j+1], cost[j] + costs[idx-1][j+2])
        elif j == 1:
            costs[idx][j] = min(cost[j] + costs[idx-1][j-1], cost[j] + costs[idx-1][j+1])
        elif j == 2:
            costs[idx][j] = min(cost[j] + costs[idx-1][j-2], cost[j] + costs[idx-1][j-1])

print(min(costs[N-1]))

