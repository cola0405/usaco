# 贪心
# 每个片段的 nights 是统一的
# 那我们要找到一个所有片段都有效的nights，而且尽可能让nights更大（最小的最大值问题 -- 遍历更新即可）
# 这样，最初始的病人数量就会尽可能得少

# 如何找每个片段都有效的nights呢
# 首先贪心，要让 nights 尽可能大，那就设一开始的生病人数是 1
# 不断尝试+1，看当前nights 是否能够增长到 len(seg)
# 这里要注意！不要让 nights 后的病人数量 > len(seg)
# 以 len(seg) 为 upper_bound 去找 nights 即可
# 没办法恰好相等，那只是说明初始肯定不止1个病人
# 具体几个呢 -- 下面for循环尝试即可

n = int(input())
s = input().split('0')

count = float('inf')   # 符合要求的天数
for i in range(len(s)):
    if len(s[i]) == 0: continue

    l = len(s[i])
    if i == 0 or i == len(s)-1:     # 边缘的增长方式比较特殊，每晚可以只+1
        for night in range(l+1):    # nights 可以更大
            if 1+night > l:
                count = min(count, night-1)
                break
    else:
        for night in range(l+1):    # for 出来就是当前片段最多的天数
            if 1+night*2 > l:       # 注意这里的增长 -- 1 3 5 7 奇数 -- 没办法恰好取到的必定是偶数
                count = min(count, night-1)
                break

ans = 0
for seg in s:   # 统计每个片段最少的 sickness
    l = len(seg)
    if l == 0:
        continue

    for p in range(1, l+1):     # 最少多少个病人
        if p*(1+2*count) >= l:  # 这里求多个p的最多人数
            ans += p            # 只要能覆盖到，就能灵活调整 -- 两块连接之后就不是+2 而不是+4了
            break
print(ans)