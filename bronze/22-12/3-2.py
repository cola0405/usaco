t = int(input().strip())


def lier(t):
    for _ in range(t):
        input()
        n, m = map(int, input().strip().split())
        ans = True
        inp = []
        outp = []
        for _ in range(m):
            a, b = input().strip().split()
            inp.append(a)
            outp.append(int(b))
        v = [0 for _ in range(m)]

        while ans:
            flag = True
            for x in range(m):
                if not v[x]:
                    flag = False
                    break
            if flag:
                break
            pre = False

            for i in range(n):
                finding = [[0, 0], [0, 0]]
                for j in range(m):
                    if v[j]:
                        continue
                    finding[int(inp[j][i])][outp[j]] = 1
                if (not finding[0][0] and finding[0][1]) or (finding[0][0] and not finding[0][1]):
                    pre = True
                    for k in range(m):
                        if inp[k][i] == '0':
                            v[k] = 1
                    break
                if (not finding[1][0] and finding[1][1]) or (finding[1][0] and not finding[1][1]):
                    pre = True
                    for k in range(m):
                        if inp[k][i] == '1':
                            v[k] = 1
                    break
            if not pre:
                ans = False
        if ans:
            print("OK")
        else:
            print('LIE')
    return 0


lier(t)
