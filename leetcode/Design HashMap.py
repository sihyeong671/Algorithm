from collections import defaultdict
class ListNode:
    def __init__(self, key=None, value=None) -> None:
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = defaultdict(ListNode)
    
    def put(self, key: int, value: int) -> None:
        pass
    
    def get(self, key: int) -> int:
        pass
    
    def remove(self, key: int) -> None:
        pass
    