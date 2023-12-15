# 需要找到使得所有片段都成立的 night
# 通过遍历交集来找

# 每个片段中可用的night

n = int(input())
s = input().split('0')

res = set(range(n+1))   # 统计所有片段都可行的 night
for i in range(len(s)):
    if len(s[i]) == 0:
        continue

    l = len(s[i])
    available = {0}     # 保底的night = 0
    if i == 0 or i == l-1:
        for night in range(1, l+1):
            if 1+night > l:     # 边缘时最少可以每晚只+1
                break
            available.add(night)
    else:
        for night in range(1,n):
            if 1+night*2 > l:   # 普通情况下每晚+2
                break
            available.add(night)
    res &= available    # 交集统计

ans = 0
night = max(res)    # night尽可能多，初始就可以尽可能少
for seg in s:   # 统计每个片段最少的 sickness
    l = len(seg)
    if l == 0:
        continue

    for x in range(1, l+1):
        if x*(1+2*night) >= l:
            ans += x
            break
print(ans)