# 하노이 탑 이동 순서

def recursive(from_, temp, to, n):
    if n == 1:
        print(from_, to)
        return
    recursive(from_, to, temp, n - 1)
    print(from_, to)
    recursive(temp, from_, to, n - 1)
    return

N = int(input())

print(2**(N)-1)
recursive(1, 2, 3, N)
