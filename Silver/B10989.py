import sys
N = int(input())
lst = [0]*10001
for _ in range(N):
    num = int(sys.stdin.readline())
    lst[num] += 1

for i in range(1, len(lst)):
    k = str(i)
    for _ in range(lst[i]):
        sys.stdout.write(k+'\n')