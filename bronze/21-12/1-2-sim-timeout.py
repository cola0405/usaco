# 超时


n = int(input())
s = list(input())
ans = 0

cheat_sheet = []

for i in range(n):
    g = 0
    h = 0
    for j in range(i, n):
        if s[j] == 'G':
            g += 1
        else:
            h += 1
        if h > 1 and g > 1:
            break
        if h+g >= 3 and (g == 1 or h == 1):
            ans += 1
print(ans)




