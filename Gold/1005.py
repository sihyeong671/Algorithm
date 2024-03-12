from collections import defaultdict, deque


T = int(input())


for _ in range(T):
    N, K = map(int, input().split())
    building_times = [0] + list(map(int, input().split())) # 건물 짓는 시간
    graph = defaultdict(list) # 자신이 의존되는 건물 번호 리스트
    connected_buildings = defaultdict(int) # 자신을 의존하는 건물 수
    time_list = [0 for _ in range(N+1)]

    q = deque()
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[X].append(Y)
        connected_buildings[Y] += 1
    for i in range(1, N+1):
        if connected_buildings.get(i, None) is None:
            q.append(i)
            time_list[i] = building_times[i]

    W = int(input())

    while len(q) != 0:
        building_num = q.popleft()
        if building_num == W:
            break

        for b_idx in graph[building_num]:

            connected_buildings[b_idx] -= 1
            if connected_buildings[b_idx] == 0:
                q.append(b_idx)
            time_list[b_idx] = max(time_list[b_idx], time_list[building_num] + building_times[b_idx])

    print(time_list[W])