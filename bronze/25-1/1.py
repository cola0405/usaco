'''
贪心

能够不用星就不用星
不得不用时再给上去
'''

def solve():
    n, a, b = map(int, input().split())
    g = [input() for _ in range(n)]
    ans = 0
    g1 = [['']*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            last = (i-b, j-a)
            if last[0] < 0 or last[1] < 0:
                if g[i][j] == 'B': return -1
                elif g[i][j] == 'G':
                    g1[i][j] = '*'
                    ans += 1
                else: g1[i][j] = '.'
            else:
                if g[i][j] == 'B':
                    g1[i][j] = '*'
                    ans += 1
                    if g1[last[0]][last[1]] == '.':
                        if g[last[0]][last[1]] == 'W': return -1
                        g1[last[0]][last[1]] = '*'
                        ans += 1
                elif g[i][j] == 'G':
                    if g1[last[0]][last[1]] == '*':
                        g1[i][j] = '.'
                    else:
                        g1[i][j] = '*'
                        ans += 1
                else: g1[i][j] = '.'
    return ans

t = int(input())
for _ in range(t):
    print(solve())
