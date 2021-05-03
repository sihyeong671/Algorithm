T = int(input())
for _ in range(T):
    N = input()
    pre = 0
    for idx,i in enumerate(N):
        if i == " ":
            for j in reversed(N[pre:idx]):
                print(j, end="")
            print(" ", end="")
            pre = idx+1
        elif idx == len(N)-1:
            for j in reversed(N[pre:]):
                print(j, end="")
            print(" ", end="")
    print("")
