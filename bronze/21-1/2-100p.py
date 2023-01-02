# 都手写列出来就行
# 余n个时，对应的处理

# ps 题目不允许有牛未编入组

n = int(input())
cows = list(map(int, input().split()))

even = 0
odd = 0

for i in cows:
    if i%2 == 0:
        even += 1
    else:
        odd += 1

min_num = min(even, odd)
ans = 2*min_num

even -= min_num
odd -= min_num

if odd != 0:
    if odd%3 == 0:
        ans += odd//3*2
    elif odd%3 == 1:
        ans += odd//3*2 - 1
    elif odd%3 == 2:
        ans += odd//3*2 + 1
elif even != 0:
    ans += 1

print(ans)

