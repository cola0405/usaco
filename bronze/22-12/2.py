# 要使得草块的数量尽可能地少 —— 不难想到是贪心
# 首先一个思路是该放的时候才放
# 但是，这样的贪心策略是会有问题的，并没有达到利益最大化 —— 题目给的测试用里已经说明
# 那么就需要转变贪心策略 —— 因为草地允许两边的牛来吃
# 所以问题会转变为 —— 如何让每块草地的价值最大化
# 那就是从左往右遍历时 i+k 尽可能把草地往右边种 -- 如此一来左边顾到了，右边也能尽可能覆盖多的cow

T = int(input())
for u in range(T):
    n, k = map(int, input().split())
    cows = input()

    G, H = -float('inf'), -float('inf')     # 需要足够小，来表示一开始没有可吃的草地
    ans = ['.']*n
    count = 0
    for i in range(n):
        if cows[i] == 'G' and abs(i-G) > k:     # 覆盖不到了才铺新的
            right = min(i+k, n-1)
            while ans[right] != '.':    # 解决冲突
                right -= 1
            G = right       # 需要尽可能往右边铺
            ans[right] = 'G'
            count += 1
        elif cows[i] == 'H' and abs(i-H) > k:
            right = min(i+k, n-1)
            while ans[right] != '.':
                right -= 1
            H = right
            ans[right] = 'H'
            count += 1

    print(count)
    print(''.join(ans))
