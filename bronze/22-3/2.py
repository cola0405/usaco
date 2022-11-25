# 调试才发现数据读错了
# G.append(int(s[2:]))
# 而不是G.append(int(s[2]))
# 难怪只有前两个测试用例过了

# 这个模拟很巧妙的
# 结合着G_max 和 L_min的规律按贪心的方法去模拟拿
# 可以极大减少枚举的数量

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
    line = input().split()
    word = line[0]
    if word == 'G':
        G.append(int(line[1]))
    else:
        L.append(int(line[1]))

G.sort()
L.sort()

n = len(G)
ans = 1000
for i in range(len(G)):
    for j in range(len(L)):
        G_max = G[n-1-i]
        L_min = L[j]
        if G_max <= L_min:
            ans = min(ans, i+j)
            break
ans = min(ans, len(G), len(L))
print(ans)


