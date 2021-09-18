# 구간 합 구하기
# 세그먼트 트리

# import sys
# from math import ceil, log2
#
#
# def make_tree(start, end, node):
#     if start == end: # 가장 하위의 값 ( 하나만 있는 경우 )
#         tree[node] = lst_N[start]
#         return tree[node]
#     else:
#         mid = (start+end)//2
#         tree[node] = make_tree(start, mid, node*2) + make_tree(mid+1, end, node*2 + 1)
#         return tree[node]
#
#
# def update(start, end, node, index, dif):
#     if index < start or index > end: # 범위 벗어나면 return
#         return
#     tree[node] += dif # 헌재 노드에 변화값 더하기
#     if start != end: # 제일 하위(리프노드)가 아닌 경우 자식노드도 변경
#         mid = (start+end)//2
#         update(start, mid, node*2, index, dif)
#         update(mid+1, end, node*2+1, index, dif)
#
#
# def sum_(start, end, node, left, right):
#     if left > end or right < start:
#         return 0
#     if left <= start and end <= right:
#         return tree[node]
#     mid = (start+end)//2
#     return sum_(start, mid, node*2, left, right) + sum_(mid+1, end, node*2+1, left, right)
#
#
# N, M, K = map(int, sys.stdin.readline().split())
# lst_N = []
# for _ in range(N):
#     lst_N.append(int(sys.stdin.readline()))
#
# h = ceil(log2(N))
# tree_size = (1 << (h+1))
# tree = [0]*tree_size
# make_tree(0, N-1, 1)
# for i in range(M+K):
#     a, b, c = map(int, sys.stdin.readline().split())
#     if a == 1:
#         diff = c - lst_N[b-1]
#         lst_N[b-1] = c
#         update(0, N-1, 1, b-1, diff)
#     elif a == 2:
#         print(sum_(0, N-1, 1, b-1, c-1))


import sys


def update(n, diff):
    while n <= N:
        tree[n] += diff
        n += (n & -n)


def sum_(n):
    result = 0
    while n > 0:
        result += tree[n]
        n -= (n & -n)
    return result


def interval_sum(start, end):
    return sum_(end) - sum_(start-1)

N, M, K = map(int, sys.stdin.readline().split())

tree = [0]*(N+1)
arr = [0]*(N+1)

for i in range(1, N+1):
    num = int(sys.stdin.readline())
    arr[i] = num
    update(i, num)

for i in range(M+K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        update(b, c-arr[b])
        arr[b] = c
    elif a == 2:
        print(interval_sum(b, c))










