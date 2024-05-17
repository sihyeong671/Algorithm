# KMP
T = input()
P = input()

def make_pi():
    pi = [0 for _ in range(0, len(P))]

    j = 0
    for i in range(1, len(P)):
        while j > 0 and P[i] != P[j]:
            j = pi[j-1]

        if P[i] == P[j]:
            j += 1
            pi[i] = j
        breakpoint()
    return pi

make_pi()
    



 