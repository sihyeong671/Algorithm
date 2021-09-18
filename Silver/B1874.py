# 스택 수열

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# lst = []
# num = []
# for i in range(n):
#     num.append(int(input()))
#
# ans = []
# idx = 1
# num_idx = 0
# while True:
#     if num_idx == len(num):
#         for i in range(len(ans)):
#             sys.stdout.write(ans[i]+'\n')
#         break
#     elif idx > n+1:
#         print('NO')
#         break
#
#     if len(lst) == 0:
#         lst.append(idx)
#         ans.append('+')
#         idx += 1
#
#     if num[num_idx] == lst[-1]:  # pop
#         num_idx += 1
#         ans.append('-')
#         lst.pop()
#         continue
#
#     lst.append(idx)
#     ans.append('+')
#     idx += 1

import sys
input = sys.stdin.readline

if __name__=='__main__':
  count = 0
  stack = []
  result = []
  isPossible = True

  num = int(input())
  for i in range(num):
    stack_num = int(input())

    while count < stack_num:
      count += 1
      stack.append(count)
      result.append('+')

    if stack[-1] == stack_num:
      stack.pop()
      result.append('-')

    else:
      isPossible = False

  if isPossible == True:
    print('\n'.join(result))
  else:
    print('NO')


