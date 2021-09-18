# 팰린드롬인지 확인하기


n = input()
start = 0
end = len(n) - 1
while True:
    if start >= end:
        print(1)
        break

    if n[start] == n[end]:
        start += 1
        end -= 1
        continue
    else:
        print(0)
        break
