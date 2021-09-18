def duplicateZeros(arr:list) -> None:
    new_arr = []
    for i in range(len(arr)):
        if len(new_arr) == len(arr):
            break
        if arr[i] == 0:
            new_arr += [0, 0]
        else:
            new_arr.append(arr[i])

    for j in range(len(arr)):
        arr[j] = new_arr[j]

    # print(arr)

arr = [1,0,2,3,0,4,5,0]

duplicateZeros(arr)
