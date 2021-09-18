# 트리 순회

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left_node = left
        self.right_node = right

# 전위 순회
def pre_order(node):
    print(node.data, end="")
    if node.left_node != '.':
        pre_order(tree[node.left_node])
    if node.right_node != '.':
        pre_order(tree[node.right_node])

# 중위 순회
def in_order(node):
    if node.left_node != '.':
        in_order(tree[node.left_node])
    print(node.data, end="")
    if node.right_node != '.':
        in_order(tree[node.right_node])

# 후위 순회
def post_order(node):
    if node.left_node != '.':
        post_order(tree[node.left_node])
    if node.right_node != '.':
        post_order(tree[node.right_node])
    print(node.data, end="")


tree = {}
N = int(input())
for _ in range(N):
    n, r, l = input().split()
    tree[n] = Node(n, r, l)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])



