
# 可以二分的核心在于该点左边的答案比当前点小，不用再去考虑
# 如此，即可利用二分去处理10^5的数据


# 需要注意的一点是，h指数不仅限于cites中出现的过的数字
# 3 0
# 0 99 99

# 6 10
# 2 2 3 3 3 3
# 应该输出：4
# 如果按照当前算法，输出的是3，因为他只往左看



n, L = map(int, input().split())
cites = list(map(int, input().split()))
cites.sort()

left = 0
right = n-1
ans = 0
while left <= right:
    mid = (left+right)//2
    h = cites[mid]
    l_one = 0
    e = 0
    g = 0
    for i in cites:
        if i+1 == h:
            l_one += 1
        if i == h:
            e += 1
        if i > h:
            g += 1

    # 取cites[i]，在L允许范围内引用次数为(cites[i]-1)的那些点
    # 同时二分向右尝试增大h指数
    if min(l_one, L)+e+g >= h:
        left = mid+1
        ans = max(h, ans)

    # 取cites[i]+1，在L允许范围内引用同为(cites[i])的那些点，再引用一次
    # 同时二分向右尝试增大h指数
    # 6 10
    # 2 2 3 3 3 3
    # 应该输出：4
    if min(e, L)+g >= h+1:
        left = mid+1
        ans = max(h+1, ans)

    # 前面两种方案都不行，即当前h指数过大，需要往左边收敛
    # 然后注意，h指数不仅限于cites中出现的过的数字
    # h指数的来源，可以是引用次数相同的文章的数量

    # 3 0
    # 0 99 99
    # 应该输出：2
    if right > mid:
        ans = max(ans, min(h, e+g))
        right = mid - 1

print(ans)



