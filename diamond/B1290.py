cnt = 0
Unit = 0

N, B, U = map(int, input().split())

while True:
    if B ==0 and Unit ==0:
        break
    cnt += 1
    B -= N
    if B > 0:
        Unit += U
    N -= Unit