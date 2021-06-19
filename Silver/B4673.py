# 셀프 넘버

lst = [x for x in range(1, 10001)]
for i in range(10000):
    for j in str(i):
        i += int(j)
    if i in lst:
        lst.remove(i)
for i in lst:
    print(i)

