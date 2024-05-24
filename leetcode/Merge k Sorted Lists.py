import heapq # 최소 힙 지원
from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
def mergeKLists(lists: List[ListNode]) -> ListNode:
    root = result = ListNode(None)

    heap = []
    
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (lists[i].val, i, lists[i]))
    
    while heap:
        node = heapq.heappop(heap)
        idx = node[1]
        result.next = node[2]
        
        result = result.next
        if result.next:
            heapq.heappush(heap, (result.next.val, idx, result.next))
    
    return root.next
    

