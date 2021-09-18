#  바이러스

N = int(input())
L = int(input())
computer = {}
for i in range(N):
    computer[i+1] = set()
for _ in range(L):
    a, b = map(int, input().split())
    computer[a].add(b)
    computer[b].add(a)

visited = [True]+[False]*(N-1)


def dfs(index, com):
    for i in computer[index]:
        if not visited[i-1]:
            visited[i-1] = True
            dfs(i, com)


dfs(1, computer)
print(visited.count(True)-1)


