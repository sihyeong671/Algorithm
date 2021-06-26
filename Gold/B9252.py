#LCS2

# from copy import deepcopy
# S_1 = input()
# S_2 = input()
# lst = [[0, ''] for _ in range(len(S_1)+1)]
# dp = [deepcopy(lst) for _ in range(len(S_2)+1)]
# for i in range(1, len(S_2)+1):
#     for j in range(1, len(S_1)+1):
#         if S_2[i-1] == S_1[j-1]:
#             dp[i][j][0] = dp[i-1][j-1][0] + 1
#             dp[i][j][1] = dp[i-1][j-1][1] + S_2[i-1]
#         else:
#             if dp[i-1][j][0] < dp[i][j-1][0]:
#                 dp[i][j] = dp[i][j-1]
#             else:
#                 dp[i][j] = dp[i-1][j]

# for x in range(len(S_2)+1):
#     for y in range(len(S_1)+1):
#         print(dp[x][y], end=" ")
#     print("")
# print('\n\n')
# print(dp[len(S_2)][len(S_1)][0])
# print(dp[len(S_2)][len(S_1)][1])

S_1 = input()
S_2 = input()

dp = [[0]*(len(S_1)+1) for _ in range(len(S_2)+1)]
dp_s = [['']*(len(S_1)+1) for _ in range(len(S_2)+1)]
for i in range(1, len(S_2)+1):
    for j in range(1, len(S_1)+1):
        if S_2[i-1] == S_1[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            dp_s[i][j] = dp_s[i-1][j-1] + S_1[j-1]
        else:
            if dp[i - 1][j] < dp[i][j - 1]:
                dp[i][j] = dp[i][j-1]
                dp_s[i][j] = dp_s[i][j-1]
            else:
                dp[i][j] = dp[i-1][j]
                dp_s[i][j] = dp_s[i-1][j]
# for x in range(len(S_2) + 1):
#     for y in range(len(S_1) + 1):
#         print(dp[x][y], end=" ")
#     print("")
# print('\n\n')
# for x in range(len(S_2) + 1):
#     for y in range(len(S_1) + 1):
#         print(dp_s[x][y], end=" ")
#     print("")
print(dp[len(S_2)][len(S_1)])
print(dp_s[len(S_2)][len(S_1)])