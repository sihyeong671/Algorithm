# 분수 합

def gcd(a, b):
    while a % b != 0:
        temp = a % b
        a = b
        b = temp
    return b


N_1, D_1 = map(int, input().split())
N_2, D_2 = map(int, input().split())

ans_N = N_1 * D_2 + N_2 * D_1
ans_D = D_1 * D_2

tmp = gcd(ans_N, ans_D)
print(ans_N//tmp, ans_D//tmp)

