# 에디터

import sys
N = input()
M = int(input())
stack_1 = list(N)
stack_2 = []

for _ in range(M):
    command = sys.stdin.readline().rstrip()
    if len(command) == 3:
        stack_1.append(command[-1])
    else:
        if command == 'L':
            if len(stack_1) == 0:
                continue
            stack_2.append(stack_1.pop())
        elif command == 'B':
            if len(stack_1) == 0:
                continue
            stack_1.pop()
        elif command == 'D':
            if len(stack_2) == 0:
                continue
            stack_1.append(stack_2.pop())

ans = stack_1 + stack_2[::-1]
for i in range(len(ans)):
    print(ans[i], end="")


