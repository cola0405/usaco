# 都手写列出来就行
# 余n个时，对应的处理

# ps 题目不允许有牛未编入组
n = int(input())
cows = list(map(int, input().split()))

even = 0
odd = 0

for cow in cows:
    if cow%2 == 0: even += 1
    else: odd += 1

mn = min(even, odd)  
ans = mn*2          # 统计完奇数和偶数的个数后，最终答案肯定至少有 min*2 组
even -= mn
odd -= mn

if odd == 0 and even > 0:
    ans += 1
else:
    ans += (odd//3)*2  # 每3个奇数又可以凑出一个 "偶奇"
    odd %= 3
    if odd == 2:       # 如果还剩2个奇数，那还能凑出一个偶数来
        ans += 1
    elif odd == 1:     # 如果还剩奇数，那只能往前合并到最近的奇数组
        ans -= 1
print(ans)