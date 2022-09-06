import sys

doc = sys.stdin.readline().strip()
word = sys.stdin.readline().strip()

cnt = 0
idx = 0

while idx < len(doc):
    if word == doc[idx:idx+len(word)]:
        idx += len(word)
        cnt += 1
    else:
        idx += 1

print(cnt)
