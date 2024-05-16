# 브루트 포스
from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# in을 이용한 탐색

def twoSum(nums: List[int], target: int) -> List[int]:
    for idx, n in enumerate(nums):
        complement = target - n
        # in으로 구현하면 같은 시간 복잡도라고 해도 내부 구현에 의해 더 빠르게 실행된다.
        if complement in nums[idx+1:]:
            return [nums.index(n), nums[idx+1:].index(complement) + (idx+1)]
        

def twoSum(nums: List[int], target: int) -> List[int]:
    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i
    
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]

# 조회 구조 개선
def twoSum(nums: List[int], target: int) -> List[int]:
    nums_map = {}
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i
        

# 투 포인터 사용 불가능


