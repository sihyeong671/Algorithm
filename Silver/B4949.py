# 균형잡힌 세상


# 바로 스택에 넣으면 코드 줄일 수 있음
while True:
    n = input()

    if n == '.':
        break

    lst = []
    for i in range(len(n)):
        stack = []
        if n[i] == '(' or n[i] == ')' or n[i] == '[' or n[i] == ']':
            lst.append(n[i])

    if lst.count('(') != lst.count(')') or lst.count('[') != lst.count(']'):
        print('no')
        continue

    check = True
    stack = []

    for s in lst:
        if s == '(' or s == '[':
            stack.append(s)

        elif s == ')':
            if len(stack) > 0:
                if stack.pop() != '(':
                    check = False
                    break
            else:
                check = False
                break

        elif s == ']':
            if len(stack) > 0:
                if stack.pop() != '[':
                    check = False
                    break
            else:
                check = False
                break

    if check:
        print('yes')
    else:
        print('no')