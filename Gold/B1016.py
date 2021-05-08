m, M = map(int,input().split())
cnt = 0
for num in range(m,M+1):
    i = 2
    noS = True
    while i**2 <= num:
        if num%(i**2)==0:
            noS = False
            break
        i += 1
    if noS:
        cnt += 1

print(cnt)



