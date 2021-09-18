# 슈퍼마리오

lst = []
for _ in range(10):
    lst.append(int(input()))

ans = 0
for i in range(10):
    ans += lst[i]
    if ans >= 100:
        if abs(ans-100) > abs(ans-lst[i]-100):
            ans -= lst[i]
        break

print(ans)