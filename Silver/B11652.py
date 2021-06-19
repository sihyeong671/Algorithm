# 카드

# 딕셔너리로 풀어야 함

import sys

N = int(sys.stdin.readline())

card_dict = {}
for _ in range(N):
    num = int(sys.stdin.readline())
    if num in card_dict.keys():
        card_dict[num] += 1
    else:
        card_dict[num] = 1

card_dict = sorted(card_dict.items(), key=lambda x: (-x[1], x[0]))
print(card_dict[0][0])
