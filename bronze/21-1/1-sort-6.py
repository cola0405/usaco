# 效率要比模拟高得多
table = input()
target = input()

# 编号
inx = dict()
for i in range(26):
    inx[table[i]] = i

# 逆序则ans+1
# ans 初始是1
ans = 1
for i in range(len(target)-1):
    if inx[target[i]] >= inx[target[i+1]]:
        ans += 1

print(ans)