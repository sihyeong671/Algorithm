# 뒤집힌 덧셈

X, Y = input().split()

temp = int(X[::-1]) + int(Y[::-1])
temp = str(temp)
print(int(temp[::-1]))

