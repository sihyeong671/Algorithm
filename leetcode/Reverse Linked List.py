class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 재귀 풀이    
def reverseList(head: ListNode) -> ListNode:
    
    def reverse(node: ListNode, prev: ListNode = None):
        if not node:
            return prev
        
        next, node.next = node.next, prev
        return reverse(next, node)
    
    return reverse(head)
    
# 반복구조로 뒤집기
def reverseList(head: ListNode) -> ListNode:
    node, prev = head, None
    
    while node:
        next, node.next = node.next, prev
        prev, node = node, next 
    
    return prev