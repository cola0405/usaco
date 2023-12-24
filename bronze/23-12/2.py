# 看2_1.py 详细解释

# 贪心
# 每个片段的 nights 是统一的
# 那我们要找到一个所有片段都有效的nights，而且尽可能让nights更大（最小的最大值问题 -- 遍历更新即可）
# 这样，最初始的病人数量就会尽可能得少

from math import ceil
n = int(input())
s = input().split('0')

count = float('inf')   # 符合要求的天数
for i in range(len(s)):
    l = len(s[i])
    if l == 0: continue

    if i == 0 or i == len(s)-1:     # 边缘的增长方式比较特殊，每晚可以只+1
        count = min(count, l-1)
    else:
        count = min(count, (l-1)//2)  # 多少晚可以到l, -1是因为初始就有1个

ans = 0
for seg in s:   # 统计每个片段最少的病人
    l = len(seg)
    if len(seg) == 0: continue
    ans += ceil(l/(1+2*count))   # 向上取整
print(ans)
