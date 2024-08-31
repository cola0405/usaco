# 题意理解

# 给定两个字符串 a 和 b
# 若 a[i] == b[i] 则标记为绿色
# 若 a[i] != b[i] 但 b[i] 有在 a 中其他位置出现，则标记为黄色
# 表示猜中了品种，但是猜错了位置
# 最后输出绿色和黄色的数量

# 🌟🌟🌟 要注意的是 🌟🌟🌟
# 对与某一品种的牛，其黄色的数量 <= (字符串 a 中该品种牛的数量 – 绿色的数量)

from collections import Counter
a = "".join([input() for _ in range(3)])
b = "".join([input() for _ in range(3)])

cnt = Counter(a)
green = 0
yellow = 0

# 统计绿色
for i in range(9):
    if a[i] == b[i]:
        green += 1
        cnt[a[i]] -= 1      # 总数 - 绿色的数量，即为黄色的最大数量

# 统计黄色
for i in range(9):
    if b[i] != a[i] and cnt[b[i]] > 0:
        yellow += 1
        cnt[b[i]] -= 1

print(green)
print(yellow)