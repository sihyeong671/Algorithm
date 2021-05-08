N = int(input())
cnt = 0
for _ in range(N):
    S = input()
    if len(S)==1:
        cnt+=1
        continue
    lst = []
    lst.append(S[0])
    for i in range(1,len(S)):
        if S[i] in lst: # 나온 문자 중에
            if S[i-1] == S[i]: # 연속된 문자
                if i == len(S) - 1:
                    cnt += 1
                continue
            else:
                break
        else:
            lst.append(S[i])
        if i == len(S)-1:
            cnt += 1
print(cnt)





