# 부르트 포스 : 타임 아웃

# 
from typing import List
import sys
def maxProfit(prices: List[int]) -> int:
    profit = 0
    min_price = sys.maxsize
    
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)
    
    return profit
