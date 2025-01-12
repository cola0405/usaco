# 贪心 + 排序 + 可行区间问题
# 每个植物的可行的天数会在一个范围里面 -- low and high
# 求所有范围的交集，即答案

# ps: 不能只求max，因为递推不单单要满足i和i+1的关系，还需要保证不破坏前面的关系
# 举例： 前面一对是h1>h2, speed1<speed2 我们要对天数做限制，不能超过 x 天
# 后一对是h1<h2, speed1>speed2 我们需要 y天才行，但是y比x大 —— 这个冲突不是max()可以解决的

# 如何确定可行天数的范围
# 从高到低看相邻两项，根据 speed 和 height 的关系来确定天数的可行范围
# 只需要看相邻两项递推过去即可，不需要双重for循环进行全检查

from math import *
def solve():
    n = int(input())
    plants = list(map(int, input().split()))
    speeds = list(map(int, input().split()))
    taller = list(map(int, input().split()))  # ti 表示比 i 更高的植物的数量, 0 是最高的植物
    nodes = [(taller[i], plants[i], speeds[i]) for i in range(n)]
    nodes.sort()
    low = 0              # 最小天数
    high = float('inf')  # 最大天数
    for i in range(n-1):  # 从最高的开始 -- 没有植物比i高 -- 相当于已经排序了
        h1, h2 = nodes[i][1], nodes[i+1][1]
        speed1, speed2 = nodes[i][2], nodes[i+1][2]
        
        if h1 > h2 and speed1 >= speed2:
            pass
        elif h1 > h2 and speed1 < speed2:
            high = min(high, floor((h1-h2-1)/(speed2-speed1)))
        elif h1 <= h2 and speed1 > speed2:
            low = max(low, ceil((h2-h1+1)/(speed1-speed2)))
        elif h1 <= h2 and speed1 <= speed2:
            return -1
    return low if low <= high else -1

T = int(input())
for r in range(T):
    print(solve())

'''
1
3
4 8 5
3 1 3
2 1 0
'''
