# 都手写列出来就行
# 余n个时，对应的处理

# ps 题目不允许有牛未编入组
n = int(input())
cows = list(map(int, input().split()))

even_count = 0
odd_count = 0

for cow in cows:
    if cow%2 == 0:
        even_count += 1
    else:
        odd_count += 1

min_count = min(even_count, odd_count)
ans = min_count*2
even_count -= min_count
odd_count -= min_count

if odd_count == 0:
    ans += 1
else:
    ans += (odd_count//3)*2
    odd_count %= 3
    if odd_count == 2:
        ans += 1
    elif odd_count == 1:
        ans -= 1
print(ans)