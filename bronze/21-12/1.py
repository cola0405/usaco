# 10^5 暴力枚举肯定没办法全过
# 即使 break 剪枝也只能过（60p）
# 说明这道题肯定需要构建数据结构优化

# 观察 GGHGG 不难发现左右两边的数量可变 —— GHG 或者 GHGG
# 抽象成数学
# 左边放0个，右边可以放2
# 左边放1个，右边可以放1个、2个
# 左边放2个，右边可以放0个、1个、2个

# 总结规律
# (0, 2)
# (1, 1), (1, 2)
# (2, 0), (2, 1), (2, 2)

# 一、如果左边不放，那右边至少放2个 —— 可以放(2,3,4,..n)
# 共 (n+1)-2 种方案数, 除了开头的 0,1 不行

# 二、如果左边放1个，那右边 (1,2,3,4,..n)
# 共 (n+1)-1 种方案数, 除了开头的 0 不行

# 三、如果左边放2个，那右边 (0,1,2,3,4,..n)
# 共 (n+1) 种方案数, 放任意数量都可以

# 四、如果左边放了大于2个，那右边 (0,1,2,3,4,..n) ——  (n+1)

def count(breed):
    cnt = 0
    for i in range(n):
        if cows[i] == breed:
            l = i-1
            while l >= 0 and cows[l] != breed:
                l -= 1
            left = i-l  # 左边的总方案数 —— (0,1,2,...left) 所以有+1

            r = i+1
            while r < n and cows[r] != breed:
                r += 1
            right = r-i     # 右边的总方案数

            cnt += max(0, right-2)  # left=0  —— right: (2,3,4,..n) —— 除了0、1
            if left > 1:        # left=1  —— right: (1,2,3,..n) —— 除了0
                cnt += max(0, right-1)
            cnt += max(0, left-2) * right   # left>=2 -- right所有方案都行
    return cnt

n = int(input())
cows = input()
print(count('H') + count('G'))
