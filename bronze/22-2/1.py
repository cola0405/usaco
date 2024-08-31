# 贪心

# 想让操作次数尽可能少，那就要让分组尽可能多
# 累加，一旦不符，则表示必不可行

def solve():
    n = int(input())
    a = tuple(map(int, input().split()))
    s = sum(a)
    for g in range(1, n+1)[::-1]:   # 从大到小枚举组数
        if s%g == 0:
            final = s//g            # 每组的最终值
            cur = 0                 # 当前累加值
            for x in a:
                cur += x
                if cur > final: break     # 如果无法合并到final，则当前组数不可行
                if cur == final: cur = 0
            else:
                print(n - g)        # 合并一次，减少一个数字
                return
    print(n-1)                      # 最坏情况，把全部数字合并

t = int(input())
for _ in range(t):
    solve()
    
