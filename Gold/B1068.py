# 트리

import sys
input = sys.stdin.readline

def find_leaf(n):
    global cnt
    if n not in tree: # 자식이 없는 경우
        cnt += 1
        return
    for child in tree[n]:
        find_leaf(child)


N = int(input())
arr = list(map(int, input().split()))
remove_node = int(input())

tree = {}
root = 0

for i in range(len(arr)):
    if i == remove_node or arr[i] == remove_node:
        continue
    if arr[i] in tree:
        tree[arr[i]].append(i)
    else:
        tree[arr[i]] = [i]

cnt = 0
if -1 in tree:
    for i in tree[-1]:
        find_leaf(i)
    print(cnt)
else:
    print(cnt)
# cnt = 0
# for i in tree:
#     if not tree[i]:
#         cnt += 1
# print(cnt)


# import sys
# input = sys.stdin.readline
#
#
# def remove(n):
#     if not tree[n]:
#         del tree[n]
#         return
#
#     for i in tree[n]:
#         remove(i)
#     del tree[n]
#
#
# N = int(input())
# arr = list(map(int, input().split()))
# remove_node = int(input())
#
# tree = {}
#
# for i in range(len(arr)):
#     tree[i] = set()
#     if arr[i] != -1:
#         tree[arr[i]].add(i)
#
# remove(remove_node)
#
# cnt = 0
# for i in tree:
#     if not tree[i]:
#         cnt += 1
# print(cnt)
