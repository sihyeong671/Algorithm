# counter
from typing import List
from collections import Counter
from heapq import heappop, heappush

def topKFrequent(nums: List[int], k: int) -> List[int]:
    freqs = Counter(nums)
    heap = [] # min heap
    for f in freqs:
        heappush(heap, (-freqs[f], f))
    
    topk = list()
    for _ in range(k):
        topk.append(heappop(heap)[1])
    
    return topk
    
# 파이썬 다운 방식

def topKFrequent(nums: List[int], k: int) -> List[int]:
    return list(zip(*Counter(nums).most_common(k)))[0]