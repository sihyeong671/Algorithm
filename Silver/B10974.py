from itertools import permutations

N = int(input())
lst = [i+1 for i in range(N)]
p = permutations(lst, N)
for i in p:
    for j in i:
        print(j, end=" ")
    print("")

#