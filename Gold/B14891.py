import sys
from collections import deque

class Gear:
    def __init__(self, elements: list):
        self.left: Gear = None
        self.right: Gear = None
        self.q = deque()
        for e in elements:
            self.q.append(e)
    
    def __repr__(self) -> str:
        return f"{list(self.q)}"
    
    def left_prop(self, direction):
        if self.left is not None and self.q[-2] != self.left.q[2]:
            self.left.left_prop(-direction)
            self.left.rotate(-direction)
            
    
    def right_prop(self, direction):
        if self.right is not None and self.q[2] != self.right.q[-2]:
            self.right.right_prop(-direction)
            self.right.rotate(-direction)
    
    def rotate(self, direction):
        self.q.rotate(direction)

Gears: list[Gear] = []
for i in range(4):
    t = list(map(int, sys.stdin.readline().strip()))
    Gears.append(Gear(t))

for i, gear in enumerate(Gears):
    if i == 0:
        gear.right = Gears[i+1]
    elif i == 3:
        gear.left = Gears[i-1]
    else:
        gear.right = Gears[i+1]
        gear.left = Gears[i-1]


K = int(input())
for _ in range(K):
    g_idx, direction = map(int, input().split())
    g_idx -= 1
    Gears[g_idx].left_prop(direction)
    Gears[g_idx].right_prop(direction)
    Gears[g_idx].rotate(direction)

answer = 0
for i, g in enumerate(Gears):
    if g.q[0] == 1:
        answer += (2**i)

print(answer)

    


    

