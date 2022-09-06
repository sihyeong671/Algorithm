T = int(input())

answer = []
for _ in range(T):
    L = input()

    lst_1 = []
    lst_2 = []

    for i in L:
        if i == '>':
            if len(lst_2) != 0:
                tmp = lst_2.pop()
                lst_1.append(tmp)
        elif i == '<':
            if len(lst_1) != 0:
                tmp = lst_1.pop()
                lst_2.append(tmp)
        elif i == '-':
            if len(lst_1) != 0:
                lst_1.pop()
        else:
            lst_1.append(i)
        
    answer.append(''.join(lst_1)+''.join(lst_2[::-1]))

for p in answer:
    print(p)