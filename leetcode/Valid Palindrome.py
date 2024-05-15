# 일반적 리스트를 이용한 문제 풀이
def isPalindrome(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    return True


# deque를 이용한 문제 풀이
from typing import Deque
from collections import deque
def isPalindrome(s: str) -> bool:
    strs : Deque = deque()
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    
    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True


import re
# 슬라이싱 이용
def isPalindrome(s: str) -> bool:
    s = s.lower()
    # 정규식 사용
    s = re.sub('[^a-z0-9]', '', s)
    return s == s[::-1]