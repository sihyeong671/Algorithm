# AC

T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    arr = input()
    arr = arr[1:-1].split(",")

    p = p.replace("RR", "")
    f = 0 # 앞자리 삭제
    b = 0 # 뒷자리 삭제
    k = 1
    for i in p:
        if i == 'R':
            k *= -1
        elif i == 'D':
            if k == 1:
                f += 1
            else:
                b += 1

    if f + b <= n:
        arr = arr[f:n-b]
        # for j in range(len(arr)):
        #     arr[j] = int(arr[j])
        if k == 1:
            print('[' + ','.join(arr) + ']')
            # print(arr)
        else:
            print('[' + ','.join(arr[::-1]) + ']')
            # print(arr[::-1])
    else:
        print('error')

