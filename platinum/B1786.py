T = input()
P = input()


def make_preset():
    pi = [0 for _ in range(len(P))]
    
    j = 0
    for i in range(1, len(P)):
        while j > 0 and P[i] != P[j]:
            j = pi[j-1]
        
        if P[i] == P[j]:
            j += 1
            pi[i] = j
    return pi

pos = []
cnt = 0

j = 0
pi = make_preset()
for i in range(len(T)):
    while j > 0 and T[i] != P[j]:
        j = pi[j-1]
    
    if T[i] == P[j]:
        if j == (len(P)-1):
            pos.append(i - len(P) + 2) # index check
            cnt += 1
            j = pi[j] # 0으로 가면 안됨
        else:
            j += 1


print(cnt)
print(*pos)