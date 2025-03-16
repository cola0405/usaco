'''
递推优化
Python 优化后没办法满分，需要 C++

大体思路：把所有可能的 l和 r逆序都尝试一遍
优化的关键在于配对的数量是可递推的，可迭代的，不用每次都重新计算，从而达到 O(n^2) 的时间复杂度


'''

def expand():
    global l,r,cnt
    l -= 1
    r += 1
    # 逆序，则认为 l到 r位置，r到 l位置
    # 后面减法是减去逆序前的数量
    cnt += (a[l] == b[r]) + (a[r] == b[l]) - (a[l] == b[l]) - (a[r] == b[r])   # 递推部分
    ans[cnt] += 1

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
l = r = cnt = 0

fit = 0
for i in range(n):
    if a[i] == b[i]: fit += 1

ans = [0]*(n+1)
for i in range(n):      # 之所以放到 for + 双指针是因为这些逆序操作之间存在递推关系，不用每次都重新计算
    cnt = fit
    l = i+1
    r = i-1
    while l-1 >= 0 and r+1 < n: expand()

for i in range(n):
    cnt = fit
    l = i+1         # 处理偶数长度的逆序（上面只处理了奇数长度序列）
    r = i
    while l-1 >= 0 and r+1 < n: expand()

for x in ans: print(x)

