# 암호만들기
def check(array):
    consonant = 0
    vowel = 0
    for i in range(len(array)):
        if 'a' == array[i]:
            vowel += 1
        elif 'e' == array[i]:
            vowel += 1
        elif 'i' == array[i]:
            vowel += 1
        elif 'o' == array[i]:
            vowel += 1
        elif 'u' == array[i]:
            vowel += 1
        else:
            consonant += 1

    if consonant >= 2 and vowel >= 1:
        return True
    else:
        return False


def func(array, n):
     # 출력 조건 : 모음 한개 이상 , 자음 두개 이상
    if len(array) == L:
        if check(array):
            for j in range(len(array)):
                print(array[j], end='')
            print('')
        return
    elif n == C: # 종료 조건
        return

    func(array+[lst[n]], n+1)
    func(array, n+1)
    return


L, C = map(int, input().split())
lst = list(map(str, input().split()))
lst.sort() # 증가하는 순 배치
arr = []
func(arr, 0)


