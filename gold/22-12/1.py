'''
C++ (有一个点过不了)
复杂背包问题 + 前后缀 dp + 贪心

题目大意：
有 n个朋友要收买，每收买一个朋友可以增加收益 p，收买有两种方法，使用钱或者冰淇淋
然后每个朋友都有自己的兑换原则，可以用 x个冰淇淋可以减少 1元
问有 a块钱，b个冰淇淋最多可以获得多少收益

思路：
背包问题，但是多了一个抵用券，没法直接 dp
这里有贪心的思路，因为有 x值有大有小，我们肯定是想尽可能把冰淇淋给这些 x小的牛，可以让收益尽可能大
所以我们让牛依据 x的值进行从小到大排序，此时会出现一个很有意思的情况
牛的情况会分为三段 —— （只用冰淇淋，混用，只用钱），而且如果存在混用的牛的话，也只会是唯一的一只牛
那我们其实可以从左往右做前缀 dp1，统计只用冰激凌的情况
从右往左做后缀 dp2，统计只用钱的情况
然后枚举唯一的混用的牛，然后取其中的最大值即可

下面对三段的情况做说明：
此规律是基于贪心思想，笼统地说，因为我们要让收益尽可能大，所以我们如果冰淇淋有余，我们是不会分给两头牛的
肯定是都给 x小的那头牛，这样我们的收益才会尽可能大

或者我们用反证法来说明，如果真的存在 a、b两头牛混用（a的 x值更小）
那我为什么不把给 b的冰淇淋给 a呢？
如果给 b的冰淇淋可以给 b省 1块钱，那么这些冰激凌给 a，这样省出来的钱一定大于 1
'''

X = 0       # 1块钱所对应的冰淇淋的数量
P = 1       # 受欢迎值
C = 2       # 价格
n,a,b = map(int,input().split())        # a —— 钱、b —— 冰淇淋
cows = [(0,0,0)]
for _ in range(n):
    p,c,x = map(int,input().split())
    cows.append((x, p, c))      # 按照 x的值从小到大排序，优先把冰淇淋给 x小的

cows.sort()
dp1 = [[0]*(b+1) for _ in range(n+1)]     # 从左往右 dp，dp1[i][j] 表示前 i个牛，使用 j个冰淇淋（不使用钱），能创造的最大受欢迎度
for i in range(1, n+1):
    for j in range(b+1): dp1[i][j] = dp1[i-1][j]        # 不选第 i头牛
    ic = cows[i][X] * cows[i][C]
    for k in range(cows[i][C], b+1)[::-1]:              # 选
        if k < ic: continue
        dp1[i][k] = max(dp1[i][k], dp1[i-1][k-ic] + cows[i][P])

cows_reverse = [''] + cows[::-1]
dp2 = [[0]*(a+1) for _ in range(n+1)]    # 从右往左 dp，dp2[i][j] 表示从右往左数前 i个牛，使用 j块钱（不使用冰淇淋），能创造的最大受欢迎度
for i in range(1, n+1):
    for j in range(a+1): dp2[i][j] = dp2[i-1][j]
    for k in range(cows_reverse[i][C], a+1):
        dp2[i][k] = max(dp2[i][k], dp2[i-1][k-cows_reverse[i][C]] + cows_reverse[i][P])

ans = 0
for i in range(1,n+1):
    # 第 i头牛只用冰淇淋或钱
    ans = max(ans, dp1[i][b] + dp2[n-i][a])
    ans = max(ans, dp1[i-1][b]+dp2[n-(i-1)][a])

    # 混合用钱和冰淇淋，这里枚举第 i头牛用的钱
    for j in range(min(cows[i][C], a)+1):
        ic = (cows[i][C] - j) * cows[i][X]      # 计算需要的冰激凌数量
        if b < ic: continue
        ans = max(ans, dp1[i-1][b-ic] + dp2[n-i][a-j] + cows[i][P])
print(ans)