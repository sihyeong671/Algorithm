# 콘테스트

W = []
K = []
for _ in range(10):
    W.append(int(input()))
for _ in range(10):
    K.append(int(input()))

W.sort()
K.sort()

print(sum(W[-3:]), sum(K[-3:]))