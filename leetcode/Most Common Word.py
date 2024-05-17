from typing import List
from collections import Counter, defaultdict
import re
# 리스트 컴프리헨션 + defaultdict
def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', '', paragraph).lower().split() if word not in banned]
    counts = defaultdict(int)
    for word in words:
        counts[word] += 1
    
    return max(counts, key=counts.get)
        

def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', '', paragraph).lower().split() if word not in banned]
    counts = Counter(words)
    return counts.most_common(1)[0][0]
    
