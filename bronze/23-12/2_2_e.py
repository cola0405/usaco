n = int(input())
s = input().split('0')

low = float('inf')  # 符合要求的天数
for i in range(len(s)):
    if len(s[i]) == 0:
        continue

    l = len(s[i])
    if i == 0 or i == l-1:
        for night in range(l+1):
            if 1+night >= l:     # 边缘时最少可以每晚只+1
                low = min(low, night)
                break
    else:
        for night in range(l+1):
            if 1+night*2 >= l:   # 普通情况下每晚+2
                low = min(low, night)
                break

ans = 0
for seg in s:   # 统计每个片段最少的 sickness
    l = len(seg)
    if l == 0:
        continue

    for x in range(1, l+1):
        if x*(1+2*low) >= l:
            ans += x
            break
print(ans)