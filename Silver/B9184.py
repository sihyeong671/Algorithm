# 신나는 함수 실행
def recursive(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 and b > 20 and c > 20:
        return recursive(20, 20, 20)
    if a < b < c:
        return recursive(a, b, c -1) + recursive(a, b - 1, c) - recursive(a, b - 1, c)
    else:
        

while True:
    a, b, c = map(int, input().split())
    print(f"w({a}, {b}, {c})", end="")
    print(recursive(a, b, c))

