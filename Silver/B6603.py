# 로또

def dfs(n, lst):
    if len(lst) == 6:
        for i in range(len(lst)):
            print(lst[i], end=" ")
        print()
        return
    elif n == k:
        return

    dfs(n+1, lst+[S[n]])
    dfs(n+1, lst)
    return


while True:
    test = list(map(int, input().split()))
    if test[0] == 0:
        break
    k = test[0]
    S = test[1:]
    arr = []
    dfs(0, arr)
    print()



