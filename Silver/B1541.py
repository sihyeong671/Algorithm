import sys

tmp = sys.stdin.readline().strip()

tmp = tmp.split('-')
for i in range(len(tmp)):
    n = map(int, tmp[i].split('+'))
    tmp[i] = str(sum(n))

res = eval('-'.join(tmp))
print(res)
