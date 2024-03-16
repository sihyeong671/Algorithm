from collections import deque, defaultdict

N = int(input())

building_times = {}
dependency_buildings = defaultdict(list)
time_list = [0 for _ in range(N+1)]
connected_buildings = [0 for _ in range(N+1)]
q = deque()

for i in range(1, N+1):
    time, *pre_request = map(int, input().split())
    building_times[i] = time
    for j in pre_request[:-1]:
        dependency_buildings[j].append(i)
        connected_buildings[i] += 1
    if len(pre_request[:-1]) == 0:
        q.append(i)
        time_list[i] = time

while len(q) != 0:
    building_num = q.popleft()
    for b_idx in dependency_buildings[building_num]:

        connected_buildings[b_idx] -= 1
        if connected_buildings[b_idx] == 0:
            q.append(b_idx)
        time_list[b_idx] = max(time_list[b_idx], time_list[building_num] + building_times[b_idx])

for t in time_list[1:]:
    print(t)