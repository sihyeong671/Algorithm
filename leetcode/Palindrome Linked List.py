from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# 리스트로 변환
def isPalindrome(head: Optional[ListNode]) -> bool:
    q : List = []
    
    if not head:
        return True
    
    node = head
    
    while node is not None:
        q.append(node.val)
        node = node.next
    
    while len(q) > 1:
        if q.pop(0) != q.pop(0):
            return False
    
    return True

# Deque이용한 최적화
from collections import deque
from typing import Deque

def isPalindrome(head: Optional[ListNode]) -> bool:
    q: Deque = deque()

    if not head:
        return True
    
    node = head
    
    while node is not None:
        q.append(node.val)
        node = node.next
        
    while len(q) > 1:
        if q.popleft() != q.pop():
            return False

    return True

# 런너를 이용한 우아한 풀이
def isPalindrome(head: Optional[ListNode]) -> bool:
    rev = None
    slow = fast = head
    
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next

    if fast:
        slow = slow.next
    
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    
    return not rev
    