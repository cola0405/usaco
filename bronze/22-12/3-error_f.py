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
            col = p[0]
            ch = p[1]
            for row in range(len(dest)):
                if dest[row][col] == ch:
                    if not special(row, src, dest):
                        break
            else:
                return True

    def special(row, src, dest):
        for col in range(n):
            s = set()
            for inp in src:
                s.add(inp[col])
            if dest[row][col] not in s:
                return True
        return False

    if check(zero_possible, zero, one)\
            or check(one_possible, one, zero):
        print('OK')
    else:
        print('LIE')





'''

1

2 4
00 0
01 1
10 1
11 1

1

3 4

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
11101 0
11000 0
10101 1
10111 1
10100 1
10101 1
10110 1
ok

1

3 4
101 1
010 1
000 0
111 0

1

3 4
101 1
010 1
110 0
001 0

1

3 4
101 1
010 1
111 0
001 0


1

3 4
101 1
010 1
111 0
011 0


1

3 4
101 1
000 1
111 0
011 0


1

3 4
101 1
001 0
111 1
001 1
lie

1

3 4
101 1
100 1
111 1
001 0


1

4 6
1110 0
1010 0
0101 0
0000 1
0010 1
0001 1

'''

