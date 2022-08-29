n = int(input())
s = list(input())
print(s)

c = set()
ans = 0

for i in range(len(s)-2):
    c.add(s[i])
    c.add(s[i+1])
    c.add(s[i+2])
    if len(c) == 2:
        ans += 1
    # 这个clear把s[0]给释放了！
    s.clear()

print(ans)




