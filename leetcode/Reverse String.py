# 투 포인터
from typing import List
def reversString(s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# 파이썬 다운 방식
def reversString(s: List[str]) -> None:
    s.reverse()
    
def reversString(s: List[str]) -> None:
    s = s[::-1]
    # 공간 복잡도 제약때문에 아래 트릭 사용
    s[:] = s[::-1]


    