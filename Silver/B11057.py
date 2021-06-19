#오르막 수
N = int(input())
if N >= 3:
    arr = [i for i in range(10, 0 , -1)]
    for i in range(N-2):
        arr_temp = []
        temp = []
        for idx in range(len(arr)):
            arr_temp.append(arr[idx:])
        for j in range(len(arr_temp)):
            temp.append(sum(arr_temp[j]))
        arr = temp[:]
    print(sum(arr) % 10007)
elif N == 2:
    print(55)
else:
    print(10)