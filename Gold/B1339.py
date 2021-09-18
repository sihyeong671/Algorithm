# 단어 수학

# from itertools import permutations as per
#
# N = int(input())
# arr = [] # 입력받은 단어들
# lst = [] # 존재하는 알파벳
# ans = 0 # 최댓값
# for _ in range(N):
#     word = input()
#     arr.append(word)
#     for i in word:
#         if i not in lst:
#             lst.append(i)
#
# num_lst = [k for k in range(10 - len(lst), 10)] # 알파벳 숫자에 대입
# nums = per(num_lst, len(lst))
#
#
# for n in nums:
#     arr_temp = []
#     for j in arr:
#         num = ''
#         for w in j:
#             for t in range(len(lst)):
#                 if lst[t] == w:
#                     num += str(n[t])
#                     break
#         arr_temp.append(int(num))
#     ans = max(ans, sum(arr_temp))
# print(ans)

# 딕셔너리 이용

n = int(input())

words = []

for i in range(n):
    words.append(input())

dict = {}
for word in words:
    t = len(word) - 1
    for a in word:
        if a in dict:
            dict[a] += 10 ** t
        else:
            dict[a] = 10 ** t
        t -= 1

number = []

for num in dict.values():
    number.append(num)

number.sort(reverse=True)

ans = 0
for i in range(len(number)):
    ans += (number[i]*(9-i))

print(ans)

