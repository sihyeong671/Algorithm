# 비슷한 단어

N = int(input())
first_word = [0]*26
word = input()
for i in word:
    first_word[ord(i)-65] += 1

cnt = 0
for _ in range(N-1):
    lst = [0]*26
    w = input()
    # 각 알파벳 갯수 리스트에 저장
    for i in w:
        lst[ord(i)-65] += 1
    add = 0
    sub = 0
    for f, l in zip(first_word, lst):
        if abs(f-l) == 1:
            if f > l:
                sub += 1
            else:
                add += 1
        elif (f - l) == 0:
            continue
        else:
            add = sub = -1
            break

    if add == 1 and sub == 1:
        cnt += 1
    elif add == 0 and sub == 1:
        cnt += 1
    elif add == 1 and sub == 0:
        cnt += 1
    elif add == 0 and sub == 0:
        cnt += 1

print(cnt)





# 빼는 경우
# 더하는 경우
# 바꾸는 경우
# 빼고 더하기
#
# 더하고 빼기
#

