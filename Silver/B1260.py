N, M, V = map(int, input().split())
arr = [[0]*N for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1
    arr[b-1][a-1] = 1
visted_lst_d = [0] * N
visted_lst_b = [0] * N

def dfs(V):
    visted_lst_d[V] = 1 # 방문 = 1
    print(V+1, end=" ")
    for i in range(N):
        if visted_lst_d[i] == 0 and arr[V][i] == 1:
            dfs(i)

def bfs(V):
    q = [V]
    visted_lst_b[V] = 1
    while q:
        k = q.pop(0)
        print(k+1, end=" ")
        for i in range(N):
            if visted_lst_b[i] == 0 and arr[k][i] == 1:
                q.append(i)
                visted_lst_b[i] = 1

dfs(V-1)
print()
bfs(V-1)




