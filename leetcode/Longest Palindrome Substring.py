# DP

# 투 포인터

def longestPalindrome(s: str) -> str:
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
    
    if len(s) < 2 or s == s[::-1]:
        return s
    
    result = ""
    for i in range(len(s) - 1): # 슬라이딩 윈도우
        # 짝수 홀수 두 경우 expand
        result = max(result, expand(i, i+1), expand(i, i+2), key=len)
    return result