# 카탈란 수
T = int(input())
for _ in range(T):
    PS = input()
    cnt = 0
    if PS.count("(") != PS.count(")"):
        print("NO")
        continue
    for i in PS:

        if i == "(":
            cnt += 1
        elif i ==")":
            cnt -= 1

        if cnt < 0:
            print("NO")
            break

    if cnt == 0:
        print("YES")