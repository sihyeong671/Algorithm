N = input()

if '0' not in N:
    print(-1)
else:
    n = sum(map(int, list(N)))
    if n % 3 == 0:
        print(''.join(sorted(N, reverse=True)))
    
    else:
        print(-1)
