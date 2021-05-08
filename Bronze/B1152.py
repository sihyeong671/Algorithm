N = input()
# 문자열 익덱싱(제거)하는 경우에는 문자열 길이가 0일경우 아주 많을 경우 극단적을 생각해보기
if len(N) >= 2:
    nlst = N[1:-1]
    print(nlst.count(' ')+1)
elif N == " ":
    print(0)
else:
    print(1)