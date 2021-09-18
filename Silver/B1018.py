# 체스판 다시 칠하기

N, M = map(int, input().split())

board = [input() for i in range(N)]

lst = [
    [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW'
    ],
    [
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    ]
]

def diff_chcek(arr):
    cnt = 2500
    for l in lst:
        temp = 0
        for i in range(8):
            for j in range(8):
                if arr[i][j] != l[i][j]:
                    temp += 1

        cnt = min(cnt, temp)
    return cnt


ans = 2500
for i in range(N-7):
    for j in range(M-7):
        temp_arr = []
        for k in range(8):
            temp_arr.append(board[i+k][j:j+8])
        ans = min(ans, diff_chcek(temp_arr))

print(ans)

