'''
Python 没办法全过

博弈论
题目大意：有 n堆石子，开局 Bessie可以取 s个石子，随后每次游戏双方必须取 s的倍数数量的石子 (1倍也算)
问 Bessie有多少种必胜的开局法

分析什么时候 Bessie 必胜
常规考虑奇偶性
在取石子问题上，不难想到我们要去考虑每堆石子可取的次数 (这道题要进一步压缩，研究 cnt[X])
假设在 s下，每堆石子可取次数为 Xi，cnt[X]为可取 X次的堆的数量
1.当所有 cnt[X]都为偶数时，Bessie 必败 —— Elsie可以把可取石子都取光，轮到 Bessie时没石子取了
2.当所有 cnt[X]中存在一个奇数时，且 X==1 时，Bessie 必胜 —— 把必输的局面留给了 Elsie
3.当所有 cnt[X]中存在两个奇数时，如果恰好是相邻的 cnt[X] 和 cnt[X-1] 为奇数，则 Bessie必胜 —— Bessie可以取 X的堆
此时，cnt[X]-1变为偶数，然后使得 cnt[X-1]+1也变成偶数，又把必输的局面留给了 Elsie
4.对于其他情况，Bessie必败

这道题还有一个比较麻烦的地方，需要优化 cnt[X]的统计方法
因为我们需要计算出所有的可能方案，所以得要枚举所有可能的 s
对于每一个 s我们都要重新计算 cnt[X]
这里用的是利用了前缀和来进行优化，具体步骤看下面的解析
'''


n = int(input())
a = list(map(int, input().split()))
max_a = max(a)
cnt1 = [0] * (max_a+1)       # cnt1[i] 表示石子数量小于等于 i的堆的数量
for x in a: cnt1[x] += 1
for i in range(1, max_a+1):
    cnt1[i] += cnt1[i-1]
cnt2 = [0] * (max_a+1)      # cnt2[i] 表示当前 s下，可以取 i次的堆的数量
ans = 0
for s in range(1, max_a+1):     # 枚举 Bessie第一次取 s个
    max_t = max_a // s          # 最多可以取 max_t次
    for i in range(1, max_t+1):
        # cnt1[s*(i+1)-1] 表示在s下，取(i+1)次， s*(i+1)-1个石子的堆的数量
        # cnt1[s*i-1] 表示在s下，取i次， s*i-1个石子的堆的数量
        # 得到的就是cnt2[i]，当前 s下，可以取 i次的堆的数量
        cnt2[i] = cnt1[min(s*(i+1)-1, max_a)] - cnt1[s*i-1]

    odd_cnt = 0
    for i in range(1, max_t+1):
        if cnt2[i] % 2 == 1: odd_cnt += 1

    if odd_cnt == 1 and cnt2[1]%2 == 1: ans += cnt2[1]

    if odd_cnt == 2:
        for i in range(2, max_t+1):
            if cnt2[i]%2 == 1 and cnt2[i-1]%2 == 1:
                ans += cnt2[i]
print(ans)

