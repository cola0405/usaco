'''
中位数 + 前缀和 + 贪心

a[i] = a[i]%m，然后将问题转化为使得所有 a[i]都相等的最小代价
根据贪心可知，目标值一定在 a[i]的某个数，从而把问题规模缩小到 10^5
进而我们需要高效的算法去求代价，这里用的是前缀和
但是有一点要注意，a[i]可以往 +- 两个方向变换，到底选哪个呢？

这里我们构建一个 2n 长度的 a[i] 即可把往不同方向变化的问题考虑到
举一个具体的例子：
a = [0, 3, 3, 6, 8]
扩展后得到：a = [0, 3, 3, 6, 8, 9, 12, 12, 15, 17]
然后我们考虑各个[i+n/2,i+n/2 + n]区间 (0 <= i < n)
[3,6,8,9,12] 此时取中位数 8作为最终 target
left = 7, right = 5, 总代价 = 12
right所包含的 9、12 其实就是表示 0、3 做减法时的消耗

下一个区间 [6,8,9,12,12] 则是 0、3、3 做减法的消耗，以此类推来解决前面提到的可加可减的问题

不过还有很多细节的地方要注意，比如前缀和数组的构建、填充位等
'''

t = int(input())
while t:
    n,m = map(int,input().split())
    a = list(map(lambda x: x%m, map(int, input().split())))
    a.sort()
    a += a[:]
    a.insert(0, 0)              # 填充位
    for i in range(1,n+1):      # 将 a扩展到 2n长度
        a[i+n] = a[i] + m
    pre = [0] * (2*n+1)
    for i in range(1, 2*n+1):
        pre[i] = pre[i-1] + a[i]
    ans = float('inf')
    for i in range(1,n+1):
        mid = int(i + n/2)
        left = a[mid]*(mid-i) - (pre[mid-1] - pre[i-1])         # 左边所有元素到中位数的总花费
        right = (pre[i+n-1] - pre[mid]) - a[mid]*(i+n-1-mid)    # 右边所有元素到中位数的总花费
        ans = min(ans, left+right)
    print(ans)
    t -= 1
