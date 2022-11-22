#  10^5 暴力枚举肯定没办法全过（60p）
# 也没有更好的办法，那就枚举+优化

# 可优化的点在于当有一系列连续的G或H时，计数是直接+1
# 基于这一点，创建same数组，记录从当前位出发，往右共有多少个连续的G或H
# 到时候统计次数的时候直接加，甚至还可以直接跳

# 这种思路的难点在于：
# 1.如何处理各种类型的次数统计
# 2.如何“跳”过已记录的点




n = int(input())
s = list(input())
ans = 0

same = [1]*n
same[-1] = 1
for i in range(n)[::-1]:
    if n-1 > i >= 0 and s[i] == s[i+1]:
        same[i] += same[i+1]

NOT_YET = 0
ALREADY = 1

for i in range(n):
    g = 0
    h = 0
    j = i
    flag = NOT_YET
    while j < n:
        if s[j] == 'G':
            g += same[j]
        else:
            h += same[j]

        if h > 1 and g > 1:
            # 面对GGGHHH，直接加没办法， 但是至少有一个可以
            if flag == NOT_YET:
                ans += 1
            break
        if h+g >= 3 and (g == 1 or h == 1):
            # 面对GHHHHH，重点是在连续H的个数
            if flag == NOT_YET and same[j] > 1:
                ans += max(g, h)-1
            # 面对GGGGGGH，仅+1，其他的之后会枚举到
            elif flag == NOT_YET and same[j] == 1:
                ans += 1
            # GGGHGGG，flag过后，还有连续的G，则有多少加多少
            else:
                ans += same[j]
            flag = ALREADY

        # 跳过已记录的
        if same[j] > 1:
            j += same[j]
            continue
        else:
            j += 1

print(ans)




