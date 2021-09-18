# 문자열 폭발
import sys
stack = []

n = input()
bomb = list(input())

for i in n:
    stack.append(i)
    if i == bomb[-1]:
        if bomb == stack[-len(bomb):]:
            # stack = stack[:len(stack)-len(bomb)]
            del stack[-len(bomb):]

if stack:
    for i in stack:
        sys.stdout.write(i)
else:
    print("FRULA")