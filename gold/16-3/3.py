'''
区间 dp

dp[i][j]表示区间[i,j]中所有数字合并出来的一个数
中间枚举 k，如果dp[i][k] == dp[k+1][j] 则进行合并，dp[i][j] = max(dp[i][j], dp[i][k] + 1)

这里可能存在疑虑的是有的区间可能无法合并成一个数，应该怎么处理？
我曾想过是否可以用 dp[i][j][0/1] 来表示左右两端的数
但是这个方法存在问题，因为合并可能连续发生，这个状态转移起来太麻烦了

其实可以干脆一点dp[i][j]就表示所有数字合并出来的一个数，无法合并的就按默认值 0 —— 表示无法合并，值为 0
又因为我们 [i][j] 会取到所有的区间，所以无法合并的区间不会影响正确答案
但是会不会有干扰呢？会有的 dp[i][k] 和 dp[k+1][j] 都为默认值 0的时候，就会合并出莫名其妙的 1 （testcase: 1 2 3 4）
处理的方法也很简单，合并的时候加一个 dp值不为 0的判断即可
'''

import sys

sys.stdin = open('248.in', 'r')
sys.stdout = open('248.out', 'w')

n = int(input())
nums = [int(input()) for i in range(n)]
dp = [[0]*n for _ in range(n)]  # 表示区间[i,j]中所有数字合并出来的一个数（可能存在无法合并的情况，其 dp值为 0）
ans = 0
for i in range(n)[::-1]:
    dp[i][i] = nums[i]
    for j in range(i+1, n):
        for k in range(i, n-1):
            if dp[i][k]==dp[k+1][j] and dp[i][k]!=0:  # 避免 dp值为 0的项进行合并
                dp[i][j] = max(dp[i][j], dp[i][k]+1)
        ans = max(ans, dp[i][j])
print(ans)

