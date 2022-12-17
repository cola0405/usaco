t = int(input())


for _ in range(t):
    input()
    zero = []
    one = []
    n,m = map(int, input().split())
    for i in range(m):
        line = input()
        if line[-1] == '0':
            zero.append(line.split()[0])
        else:
            one.append(line.split()[0])


    # column all zero
    zero_possible = set()
    for i in range(n):
        for tmp in ('0','1'):
            for inp in zero:
                if inp[i] != tmp:
                    break
            else:
                zero_possible.add((i, tmp))

    # column all one
    one_possible = set()
    for i in range(n):
        for tmp in ('0', '1'):
            for inp in one:
                if inp[i] != tmp:
                    break
            else:
                one_possible.add((i, tmp))

    def check(possible, src, dest):
        for p in possible:
            for i in range(len(dest)):
                if dest[i][p[0]] == p[1]:
                    if not isSpecial(i, dest, src):
                        break
            else:
                return True

    def isSpecial(j, dest, src):
        for i in range(n):
            s = set()
            for y in src:
                s.add(y[i])
            if dest[j][i] not in s:
                return True
        return False

    if check(zero_possible, zero, one)\
            or check(one_possible, one, zero):
        print('OK')
    else:
        print('LIE')





'''
1

3 4
000 0
001 0
010 1
011 1
ok


1

3 4
010 0
101 0
010 1
011 1
lie


1

5 7
00101 0
10000 0
10101 1
10111 1
10100 1
11101 1
11110 1
ok
'''

