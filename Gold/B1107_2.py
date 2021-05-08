N = input()
M = int(input())
arr = list(map(int, input().split()))
num = [i for i in range(10)]
for i in arr:
    num.remove(i)

CH = 100
case_1 = abs(CH - int(N))

N_lst = list(N)
k = [] # 0 or 1 or 2
idx = 0
for idx_, i in enumerate(N_lst):
    if int(i) in num:
        continue
    else:
        idx = idx_
        temp = 10
        for j in num:
            temp = min(temp, abs(j-int(i))) # 차이
        for j in num:
            if temp == abs(j - int(i)):
                k.append(j) # 작은 것 부터 저장됨
        break
case_2 = 0
if len(k) == 2:
    temp_1 = N_lst[:idx] + [str(k[0])] + [str(num[-1]) for _ in range(len(N) - idx - 1)]
    temp_2 = N_lst[:idx] + [str(k[1])] + [str(num[0]) for _ in range(len(N) - idx - 1)]
    num_1 = int("".join(temp_1))
    num_2 = int("".join(temp_2))
    m = min(abs(int(N)-num_1),abs(int(N)-num_2))
    case_2 = len(N) + m
elif len(k) == 1:
    if int(N_lst[idx]) > k[0]:
        temp_ = N_lst[:idx] + [str(k[0])] + [str(num[-1]) for _ in range(len(N) - idx - 1)]
        num_ = int("".join(temp_))
        case_2 = len(N) + abs(int(N)-num_)
    else:
        temp_ = N_lst[:idx] + [str(k[0])] + [str(num[0]) for _ in range(len(N) - idx - 1)]
        num_ = int("".join(temp_))
        case_2 = len(N) + abs(int(N)-num_)
else:
    case_2 = len(N)
print(min(case_1, case_2))
