t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    cows = input()
    G = []
    H = []
    for i in range(n):
        if cows[i] == 'G':
            G.append(i)
        else:
            H.append(i)

    lst = ['.']*n
    if len(G) > 0:
        j = G[0]+k
        while j >= n:
            j -= 1
        lst[j] = 'G'
    for i in range(1, len(G)):
        if G[i] > j+k:
            j = G[i]+k
            while j >= n or lst[j] != '.':
                j -= 1
            lst[j] = 'G'

    if len(H) > 0:
        j = H[0]+k
        while j >= n or lst[j] != '.':
            j -= 1
        lst[j] = 'H'
    for i in range(1, len(H)):
        if H[i] > j+k:
            j = H[i]+k
            while j >= n or lst[j] != '.':
                j -= 1
            lst[j] = 'H'

    print(n - lst.count('.'))
    print(''.join(lst))


'''
1
5 1
GGGGG

1
4 1
GGGG

'''