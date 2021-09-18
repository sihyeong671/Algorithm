# ATM

N = int(input())
lst = list(map(int, input().split()))
ans = 0
lst.sort()
for i in range(len(lst)):
    ans += lst[i]*(len(lst) - i)

print(ans)