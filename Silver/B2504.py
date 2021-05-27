# 괄호의 값
N = input()
stack = []
stack_num = []
for idx, n in enumerate(N):
    if (N.count('(') != N.count(')')) or (N.count('[') != N.count(']')):
        print(0)
        exit()
    if n == ")":
        if len(stack) == 0:
            print(0)
            exit()
        if stack.pop() == "(":
            if N[idx-1] == "(":
                stack_num[-1] = 2
                print("stack:", end=" ")
                print(stack)
                print("stack_num:",end=" ")
                print(stack_num)
            else:
                temp = 0
                length = len(stack_num) - 1
                for i in range(length, -1, -1):
                    if stack_num[i] == '(':
                        stack_num[-1] = temp * 2
                        print("stack:", end=" ")
                        print(stack)
                        print("stack_num:",end=" ")
                        print(stack_num)
                        break
                    else:
                        temp += stack_num[i]
                        stack_num.pop()
                        print("stack:", end=" ")
                        print(stack)
                        print("stack_num:",end=" ")
                        print(stack_num)
        else:
            print(0)
            exit()
    elif n == "]":
        if len(stack) == 0:
            print(0)
            exit()
        if stack.pop() == "[":
            if N[idx - 1] == "[":
                stack_num[-1] = 3
                print("stack:", end=" ")
                print(stack)
                print("stack_num:",end=" ")
                print(stack_num)
            else:
                temp = 0
                length = len(stack_num) - 1
                for i in range(length, -1, -1):
                    if stack_num[i] == '[':
                        stack_num[-1] = temp * 3
                        print("stack:", end=" ")
                        print(stack)
                        print("stack_num:",end=" ")
                        print(stack_num)
                        break
                    else:
                        temp += stack_num[i]
                        stack_num.pop()
                        print("stack:", end=" ")
                        print(stack)
                        print("stack_num:", end=" ")
                        print(stack_num)
        else:
            print(0)
            exit()

    else:
        stack.append(n)
        stack_num.append(n)
        print("stack:", end=" ")
        print(stack)
        print("stack_num:",end=" ")
        print(stack_num)
print(sum(stack_num))


