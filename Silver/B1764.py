# 듣보잡

# set 자료구조도 hashtable 처럼 동작
import sys

N, M = map(int, input().split())

listen = set()
for _ in range(N):
    listen.add(sys.stdin.readline().strip())
heard = set()
for _ in range(M):
    heard.add(sys.stdin.readline().strip())

ans = sorted(list(listen & heard))
print(len(ans))
print(* ans, sep="\n")


