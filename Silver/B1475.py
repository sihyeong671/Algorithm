N = input()
count = 1 # 세트의 개수
arr = [i for i in range(0,10)] # 카드

for i in N: # str 자료형으로 생각하고 하나씩 뺀다
    i = int(i) # int로 변환
    if i not in arr: # arr안에 N이 없을 시에
        if i == 9 and 6 in arr: # 9는 6으로 대체
            arr.remove(6)
            continue # 중간에 끊고 for문으로 되돌아가기
        if i == 6 and 9 in arr: # 6은 9로 대체
            arr.remove(9)
            continue # 중간에 끊고 for문으로 되돌아가기
        for j in range(0, 10): # 카드 없으면 추가
            arr.append(j)
        arr.remove(i)
        count += 1 # 세트의 개수 추가
    else:
        arr.remove(i) # 카드 제거

print(count)