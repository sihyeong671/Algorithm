# 오름차순 풀이
from typing import List
def arrayPariSum(nums: List[int]) -> int:
    sum = 0
    pair = []
    nums.sort()
    
    for n in nums:
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []
    return sum

# 짝수번째 값 합산

# 파이썬다운 방식

def arrayPariSum(nums: List[int]) -> int:
    return sum(sorted(nums)[::2])