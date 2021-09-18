# DSLR


from collections import deque
T = int(input())


def rotate(n, c):
    if len(n) == 1:
        n = '000' + n
    elif len(n) == 2:
        n = '00' + n
    elif len(n) == 3:
        n = '0' + n

    if c == 'L':
        temp = n[1:] + n[0]
        return temp
    elif c == 'R':
        temp = n[-1] + n[:-1]
        return temp
#
# def rotate(n, c):
#     n = list(n)
#     if c == 'L':
#         n.append(n.pop(0))
#         return ''.join(n)
#     elif c == 'R':
#         n.insert(0, n.pop())
#         return ''.join(n)


for _ in range(T):
    A, B = map(int, input().split())
    q = deque()
    q.append((A, ''))
    visited = [False for _ in range(10000)]
    visited[A] = True

    while True:
        a, n = q.popleft()
        if a == B:
            print(n)
            break

        temp_d = (a*2) % 10000

        if a == 0:
            temp_s = 9999
        else:
            temp_s = a - 1

        temp_l = int(rotate(str(a), 'L'))

        temp_r = int(rotate(str(a), 'R'))

        if not visited[temp_d]:
            q.append((temp_d, n + 'D')) # d
            visited[temp_d] = True
        if not visited[temp_s]:
            q.append((temp_s, n + 'S')) # s
            visited[temp_s] = True
        if not visited[temp_l]:
            q.append((temp_l, n + 'L')) # l
            visited[temp_l] = True
        if not visited[temp_r]:
            q.append((temp_r, n + 'R')) # r
            visited[temp_r] = True




