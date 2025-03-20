'''
python 过不了（加了快速幂也不行）
dp+组合数学

先用 dp计算方案数
再用组合数学计算总方案数

'''

from collections import Counter
import sys
sys.stdin = open('poetry.in', 'r')
sys.stdout = open('poetry.out', 'w')
mod = 10**9+7

n,m,k = map(int, input().split())
s = [0]*(n+1)       # 单词长度
c = [0]*(n+1)       # 单词种类
for i in range(1,n+1):      # offset
    s[i],c[i] = map(int, input().split())

schema = [input() for i in range(m)]
dp = [[0]*(n+1) for _ in range(k+1)]      # dp[i][j] 表示长度为 i 的句子以c[j]类单词结尾有多少种方案
t = [0]*(k+1)       # t[i]表示长度为 i的句子有多少种方案
t[0] = 1            # 初始状态，从来就行，dp不用设置了
for i in range(1,k+1):              # 每行最大长度为 k
    for j in range(1, n+1):         # 把 n个单词都过一遍
        if i >= s[j]:
            dp[i][c[j]] = (dp[i][c[j]] + t[i-s[j]]) % mod       # 把长度是[i-s[j]]的方案数加到 dp[i][c[j]]
            t[i] = (t[i] + t[i-s[j]]) % mod                     # 把长度是[i-s[j]]的各单词结尾的方案数加到 t[i]

# 分别诗格式每个字母的个数
cnt = Counter(schema)

# 组合数学把方案数求出来
ans = 1
for i in range(26):                             # 每个模式 A、B 都可以是任意一个单词，需要两层循环，省不了，因为每个模式的数量是不一样的
    ch = cnt[chr(i+ord('A'))]
    if ch == 0: continue
    res = 0
    for j in range(1, n+1):
        res = (res + dp[k][j]**ch) % mod        # 竖下来 ch个 A 总共有 dp[k][j]**ch 种方案，然后 A、B等的方案总数都乘起来即可 (44行)
    if res != 0:
        ans = (ans * res) % mod                 # Ps：A、B模式之间并没有要求相异，只是要求标 A的一致、B的一致

print(ans)
