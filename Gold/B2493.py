import sys
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
stack = []
stack_index = []
ans = []
for idx, i in enumerate(lst):
    while True:
        if len(stack) == 0:
            stack.append(i)
            stack_index.append(idx + 1)
            ans.append(0)
            break
        if stack[-1] < i:
            stack.pop()
            stack_index.pop()
        else:
            stack.append(i)
            ans.append(stack_index[-1])
            stack_index.append(idx+1)
            break

print(*ans)



