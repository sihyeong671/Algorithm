T = int(input())


building = [[i for i in range(1, 15)]]
for i in range(14):
    next_floor = [sum(building[i][:j+1]) for j in range(14)]
    building.append(next_floor)
for _ in range(T):
    k = int(input())
    n = int(input())
    print(building[k][n-1])

    
