# 연산자 끼워넣기

from itertools import permutations

max_ans = -1000000000
min_ans = 1000000000

N = int(input())

nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

operators = ['+']*add + ['-']*sub + ['*']*mul + ['/']*div
arr = permutations(operators, N-1)
arr = list(set(arr)) # 중복제거
for i in arr:
    temp = nums[0]
    for j in range(len(nums)-1):
        if i[j] == '+':
            temp += nums[j+1]
        elif i[j] == '-':
            temp -= nums[j+1]
        elif i[j] == '*':
            temp *= nums[j+1]
        elif i[j] == '/':
            temp = int(temp/nums[j+1])

    max_ans = max(max_ans, temp)
    min_ans = min(min_ans, temp)

print(max_ans)
print(min_ans)

#
# import sys
#
# ans_1 = sys.maxsize # 최소값
# ans_2 = -sys.maxsize # 최대값
#
#
# def dfs(n, num, add, sub, mul, div):
#     global ans_1, ans_2
#     if n == len(lst_num):
#         ans_1 = min(ans_1, num)
#         ans_2 = max(ans_2, num)
#         return
#     if add > 0:
#         dfs(n+1, num+lst_num[n], add-1, sub, mul, div)
#     if sub > 0:
#         dfs(n+1, num-lst_num[n], add, sub-1, mul, div)
#     if mul > 0:
#         dfs(n+1, num*lst_num[n], add, sub, mul-1, div)
#     if div > 0:
#         dfs(n+1, int(num/lst_num[n]), add, sub, mul, div-1)
#
#
# N = int(input())
# lst_num = list(map(int, input().split()))
# lst_operator = list(map(int, input().split()))
# dfs(1, lst_num[0], lst_operator[0], lst_operator[1], lst_operator[2], lst_operator[3])
#
# print(ans_2)
# print(ans_1)

