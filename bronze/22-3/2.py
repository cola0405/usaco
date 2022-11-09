# 调试才发现数据读错了
# G.append(int(s[2:]))
# 而不是G.append(int(s[2]))
# 难怪只有前两个测试用例过了

# 这个模拟很巧妙的，结合着G_max 和 L_min的规律按贪心的方法去模拟拿，可以极大减少枚举的数量

# 6
# G 1
# G 2
# G 100
# L 1
# L 5
# L 100


n = int(input())

G = []
L = []
for i in range(n):
    s = input()
    if s[0] == 'G':
        G.append(int(s[2:]))
    else:
        L.append(int(s[2:]))

G.sort()
L.sort()

def f():
    ans = 1000
    for i in range(0, len(G)):
        for j in range(0, len(L)):
            G_max = G[-i-1]
            L_min = L[j]
            if G_max <= L_min:
                ans = min(ans, i+j)
                break
    return min(len(G), len(L), ans)

print(f())



