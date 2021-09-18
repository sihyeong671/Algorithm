# 팰린드롬수

while True:

    check = True
    T = input()
    if T == '0':
        break

    for i in range(len(T)//2):
        if T[i] != T[-1-i]:
            check = False

    if check:
        print('yes')
    else:
        print('no')

