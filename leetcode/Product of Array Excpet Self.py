# 니눗셈 하지 않고 푸는 방법
# 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
from typing import List
def productExceptSelf(nums: List[int]) -> List[int]:
    out = []
    p = 1
    # left
    for i in range(0, len(nums)):
        out.append(p)
        p = p * nums[i]
    p = 1
    # 오른쪽 값 곱셈
    for i in range(len(nums) - 1, -1, -1):
        out[i] *= p
        p *= nums[i]
        
    return out


