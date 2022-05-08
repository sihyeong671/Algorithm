n = [[1,2,3], [4,5,6], [7,8,9]]

n_copy = n[:]

n_copy[0][0] = -1

print(id(n))
print(id(n_copy))

for i in range(3):
    print(id(n[i]), id(n_copy[i]))
