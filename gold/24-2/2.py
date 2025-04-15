'''
c++
区间贡献 + 单调栈 + 二阶差分

题目大意：
n个装满牛奶的桶环形排列，每个桶会朝下一个桶倒入其所有的牛奶，溢出的牛奶就损失了
问倒 1,2,3,...n 次时，剩余牛奶的总量

解题思路：
暴力模拟不可取，对问题进行转化 —— 第 i分钟之后，总剩余牛奶量 = 所有长度为 i+1 的环形子区间最小值之和
进而我们可以研究 a[i]会对哪些区间有贡献 —— 即区间内最小值恰好是 a[i]的那些区间
如何得到这些区间呢 —— 这里使用单调栈求得 a[i]左/右边第一个小于它的元素，假设下标分别为 l和 r
那么，[l+1, r+1] 内所有的区间就是以 a[i]为最小值的那些区间
暴力枚举这些区间一样超时，所以又要找规律

我们研究两个量 x= i-l, y = r-i 其实就是表示 a[i]左、右边有多少个元素
假设 x=2, y=3，然后我们列举出包含了 a[i]的所有的目标区间情况
区间长度 = 1, 数量：1
区间长度 = 2，数量：2
区间长度 = 3，数量：3

区间长度 = 4，数量：3
区间长度 = 5，数量：3

区间长度 = 6，数量：2
区间长度 = 7，数量：1

以上已经囊括所有区间的情况
联系到上面，长度为 i+1其实对应第 i分钟，把对应的贡献 a[i]*数量加到对应的统计位上这道题就曲线求出来了
但是暴力统计仍然会有时间复杂度的问题，还得想办法优化
观察到其分成 3段，一段递增数列，一段相等数列，一段递减数列
这里用二阶差分来优化这部分，对应代码中的 add()

下面要补充说明的是 3个add()的参数
1.add(1, min(left, right), a[i], a[i])
我们回到上面例子中的序列情况为：a[i-2] a[i-1] a[i] a[i+1] a[i+2] a[i+3]
区间长度为 3，有哪些情况呢？
[a[i-2], a[i]]
[a[i-1], a[i+1]]
[a[i], a[i+2]]

不难发现数量其实与 min(x,y)有关
故有 add(1, min(left, right), a[i], a[i])，表示长度[1,3] 的按照首项是a[i], 公差是 a[i]去加
那为什么公差是 a[i] 而不是 1呢？

首先我们来看其真的贡献值
a[i], a[i]*2, a[i]*3, ..., a[i]*min(x, y)
就不难发现实际贡献值的公差其实就是 a[i]
公差 = 1只是对于区间数量而言

2.add(min(left, right)+1, max(left, right), min(left, right)*a[i], 0) 首项为min(left, right)*a[i]，公差为 0
这个不用过多解释

3.add(max(left, right)+1, left+right, min(left, right)*a[i] - a[i], -a[i])
减去a[i] 其实就是对应了
区间长度 = 6，数量：2
区间长度 = 7，数量：1
'''


# 二阶差分维护
def add(l, r, h, d):        # h为首项，d为公差
    if r < l: return
    p[l] += h
    p[r+1] -= d*(r-l) + h
    s[l+1] += d
    s[r+1] -= d

n = int(input())
a = list(map(int, input().split()))   # offset

L = [0] * (3*n+1)
R = [0] * (3*n+1)
a = [0] + a*3

# 找到 a[i]左边第一个比 a[i]小的下标
st = []
for i in range(1, 3*n+1):
    while st and a[st[-1]] >= a[i]:
        st.pop()
    if st: L[i] = st[-1]
    st.append(i)

# 找到 a[i]右边第一个比 a[i]小的下标
st = []
for i in range(1, 3*n+1)[::-1]:
    while st and a[st[-1]] > a[i]:      # 这里不取等号，避免重复计算区间
        st.pop()
    if st: R[i] = st[-1]
    st.append(i)

# 二阶差分数组
p = [0] * (2*n+2)
s = [0] * (2*n+2)

for i in range(1, n+1):
    L[i] = max(L[i+n], i) - n
    R[i] = min(R[i+n], i + 2*n) - n
    left = i - L[i]
    right = R[i] - i
    # 分别统计 3类区间长度
    add(1, min(left, right), a[i], a[i])
    add(min(left, right)+1, max(left, right), min(left, right)*a[i], 0)
    add(max(left, right)+1, left+right, min(left, right)*a[i] - a[i], -a[i])

# 以下还原二阶差分
for i in range(1, n+1):
    s[i] += s[i-1]
    p[i] += s[i]
for i in range(2, n+1):
    p[i] += p[i-1]
    print(p[i])
print(p[n])



