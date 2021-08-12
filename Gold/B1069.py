# 집으로

import math

X, Y, D, T = map(int, input().split())

dist = math.sqrt(X**2+Y**2)

if D > dist:
    t = min(2*T, dist, T+D-dist)
    print(t)
else:
    cnt = dist//D
    t = min(dist, dist - D * cnt + cnt * T, T * (cnt + 1))
    print(t)




