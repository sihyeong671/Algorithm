# 단어 뒤집기

# T = int(input())
# for _ in range(T):
#     N = input()
#     pre = 0
#     for idx, i in enumerate(N):
#         if i == " ":
#             for j in reversed(N[pre:idx]):
#                 print(j, end="")
#             print(" ", end="")
#             pre = idx+1
#         elif idx == len(N)-1:
#             for j in reversed(N[pre:]):
#                 print(j, end="")
#             print(" ", end="")
#     print("")

from collections import deque # stack 라이브러리
import sys
T = int(sys.stdin.readline())
dq = deque() # 스택 생성
for _ in range(T):
    lst = []
    N = sys.stdin.readline()# 문자열 입력
    for idx, i in enumerate(N):
        if i == " ": # 공백이 나오면 스택에 있는 문자 출력
            for j in range(len(dq)):
                lst.append(dq.pop())
            lst.append(' ')
        elif idx == len(N)-1:
            for j in range(len(dq)):
                lst.append(dq.pop())
            lst.append(i)
        else:
            dq.append(i)
    sys.stdout.write(''.join(lst))