N, M, r, c, K = map(int, input().split())

map_lst = []
dice = [0] * 6

def roll(dice, dir, pos):
    if dir == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]
    elif dir == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]
    elif dir == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]
    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]
    
    if map_lst[pos[0]][pos[1]] == 0:
        map_lst[pos[0]][pos[1]] = dice[5]
    else:
        dice[5] = map_lst[pos[0]][pos[1]] 
        map_lst[pos[0]][pos[1]] = 0
    
    
    print(dice[0])
        
for _ in range(N):
    tmp = list(map(int, input().split()))
    map_lst.append(tmp)
    
commands = list(map(int, input().split()))

for command in commands:
    if command == 1:
        if c == M-1:
            continue
        c += 1
    elif command == 2:
        if c == 0:
            continue
        c -= 1
    elif command == 3:
        if r == 0:
            continue
        r -= 1
    else:
        if r == N-1:
            continue
        r += 1
        
    roll(dice, command, (r, c))