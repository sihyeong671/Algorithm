# 알파벳
import sys
R, C = map(int, input().split())
lst = [chr(i) for i in range(65, 91)]
arr = [sys.stdin.readline().strip() for _ in range(R)]

# 상 하 좌 우
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]
q = [(0, 0, [arr[0][0]])]
cnt = 0
while q:
    r, c, d = q.pop(0)
    cnt = max(cnt, len(d))
    for j in range(4):
        nr = r + dr[j]
        nc = c + dc[j]
        if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] not in d:
            q.append((nr, nc, d+[arr[nr][nc]]))

print(cnt)


import sys
def dfs(r, c, d):
    global ans
    ans = max(ans, d)
    for j in range(4):
        nr = r + dr[j]
        nc = c + dc[j]
        if 0 <= nr < R and 0 <= nc < C:
            if not lst_bool[ord(arr[nr][nc])-65]:
                lst_bool[ord(arr[nr][nc])-65] = True
                dfs(nr, nc, d+1)
                lst_bool[ord(arr[nr][nc])-65] = False


R, C = map(int, input().split())
lst_bool = [False]*26
arr = [sys.stdin.readline().strip() for _ in range(R)]
lst_bool[ord(arr[0][0])-65] = True
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]
ans = 1
dfs(0, 0, ans)
print(ans)
