# 더하기 사이클

N = int(input())
temp = N
cnt = 0
while True:
    cnt += 1
    Nsum = (N//10) + (N%10)
    newnumber = (N%10)*10 + (Nsum%10)
    if newnumber != temp:
        N = newnumber
    else:
        print(cnt)
        break