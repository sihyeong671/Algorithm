# LCS

S_1 = input()
S_2 = input()

dp = [[0]*(len(S_1)+1) for _ in range(len(S_2)+1)]
for i in range(1, len(S_2)+1):
    for j in range(1, len(S_1)+1):
        if S_2[i-1] == S_1[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
for x in range(len(S_2) + 1):
    for y in range(len(S_1) + 1):
        print(dp[x][y], end=" ")
    print("")
print(dp[len(S_2)][len(S_1)])


# def function(S_1, S_2):
#     LCS = [0 for _ in range(len(S_2) + 1)]
#
#     for a in range(1, len(S_1) + 1):
#         temp = 0
#         for b in range(1, len(S_2) + 1):
#             if LCS[b] > temp:
#                 temp = LCS[b]
#             elif S_1[a - 1] == S_2[b - 1]:
#                 LCS[b] = temp + 1
#         print(LCS)
#     return max(LCS)
#
# s_1 = input()
# s_2 = input()
# print(function(s_1, s_2))