# 看2_1.py 详细解释

# 贪心
# 每个片段的 nights 是统一的
# 那我们要找到一个所有片段都有效的nights
# 同时要尽可能让nights大（在各片段的最大天数中取底线 —— 遍历更新即可）
# 然后对于每一个片段，一个病人最多一晚+2, 则 ceil(l/(1+2*count))就是最少人数

from math import ceil
n = int(input())
s = input().split('0')

count = float('inf')
for i in range(len(s)):     # 在各片段的最大天数中取底线 —— 需要保证所有片段有效
    if len(s[i]) != 0:
        if i == 0 or i == len(s)-1:
            count = min(count, len(s[i])-1)     # 首末可以一晚+1
        else:
            count = min(count, (len(s[i])-1)//2)  # 一晚+2 多少晚可以到l, -1是因为初始就有1个

ans = 0
for seg in s:   # 统计每个片段最少的病人
    if len(seg) != 0:
        ans += ceil(len(seg)/(1 + 2*count))   # 向上取整
print(ans)