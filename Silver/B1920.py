# 수 찾기
def find_num(array, num, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == num:
            return 1
        elif array[mid] > num:
            end = mid - 1
        else:
            start = mid + 1
    return 0


N = int(input())
arr_N = list(map(int, input().split()))
arr_N.sort()
M = int(input())
arr_M = list(map(int, input().split()))


for i in range(M):
    print(find_num(arr_N, arr_M[i], 0, N - 1))
