N = int(input())
M = int(input())
arr = list(map(int,input().split()))
num = [i for i in range(10)]
for i in arr:
    num.remove(i)

