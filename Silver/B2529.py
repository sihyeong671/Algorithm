# 부등호

k = int(input())
n = list(input().split())

visited = [False]*10
min_ans = 9999999999
max_ans = 0
temp = ['', '']

# 리스트로 시작하지 말고 문자열 자체로 시작하면 더 짧은 코드 구현 가능
def dfs(num, lst):
    global min_ans
    global max_ans

    if len(lst)-1 == k:
        for i in range(len(lst)):
            lst[i] = str(lst[i])
        ans = ''.join(lst)

        if int(ans) <= min_ans:
            min_ans = int(ans)
            temp[1] = ans
        elif int(ans) >= max_ans:
            max_ans = int(ans)
            temp[0] = ans
        return

    if n[len(lst)-1] == '<':
        for i in range(10):
            if not visited[i] and i > num:
                visited[i] = True
                dfs(i, lst+[i])
                visited[i] = False

    elif n[len(lst)-1] == '>':
        for i in range(10):
            if not visited[i] and i < num:
                visited[i] = True
                dfs(i, lst+[i])
                visited[i] = False


for i in range(10):
    visited[i] = True
    dfs(i, [i])
    visited[i] = False

for k in temp:
    print(k)
