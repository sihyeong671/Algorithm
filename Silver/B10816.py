from collections import defaultdict

N = int(input())
card_dict = defaultdict(int)
for n in map(int, input().split()):
    card_dict[n] += 1
M = int(input())
for n in map(int, input().split()):
    print(card_dict[n], end=" ")
