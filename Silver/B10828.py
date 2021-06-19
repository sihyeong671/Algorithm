# 스택
import sys
N = int(sys.stdin.readline())

stack = []
for _ in range(N):
    command = sys.stdin.readline().strip()
    if command == "top":
        if len(stack) == 0:
            sys.stdout.write("-1\n")
        else:
            sys.stdout.write(str(stack[-1])+"\n")
    elif command == "pop":
        if len(stack) == 0:
            sys.stdout.write("-1\n")
        else:
            sys.stdout.write(str(stack.pop())+"\n")
    elif command == "size":
        sys.stdout.write(str(len(stack))+"\n")
    elif command == "empty":
        if len(stack) == 0:
            sys.stdout.write("1\n")
        else:
            sys.stdout.write("0\n")
    else:
        temp = int(command[5:])
        stack.append(temp)