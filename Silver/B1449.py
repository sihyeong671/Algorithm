N, L = map(int, input().split())

locations = sorted(list(map(int, input().split())))

start = locations[0]
count = 1
for location in locations:
    if location in range(start, start+L):
        continue
    else:
        start = location
        count += 1

print(count)