# 해시 테이블
def numJewelsInStones(J: str, S: str) -> int:
    freqs = {}
    count = 0

    for char in S:
        if char not in freqs:
            freqs[char] = 1
        else:
            freqs[char] += 1
    
    for char in J:
        if char in freqs:
            count += freqs[char]
    
    return count


from collections import defaultdict
def numJewelsInStones(J: str, S: str) -> int:
    freqs = defaultdict(int)
    count = 0

    for char in S:
        freqs[char] += 1
    
    for char in J:
        count += freqs[char]
    
    return count


from collections import Counter
def numJewelsInStones(J: str, S: str) -> int:
    freqs = Counter(S)
    count = 0
    for char in J:
        count += freqs[char]
    return count

    
def numJewelsInStones(J: str, S: str) -> int:
    return sum(s in J for s in S)

