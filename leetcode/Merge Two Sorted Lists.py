# 재귀 구조로 연결
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def mergeTowLists(l1: ListNode, l2: ListNode) -> ListNode:
    if (not l1) or (l2 and l1.val > l2.val):
        # 작은 값이 l1으로 오도록 함
        l1, l2 = l2, l1
    
    if l1:
        l1.next = mergeTowLists(l1.next, l2)
    return l1