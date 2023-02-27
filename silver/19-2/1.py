import sys

sys.stdin = open("herding.in", "r")
sys.stdout = open("herding.out", "w")

n = int(input())

def get_min_moves():
    max_already = 0

    # 右边满
    # 1 5 6 7
    if loc[1]-loc[0] > 2 and loc[-1]-loc[1] == n-2:
        return 2
    # 左边满
    # 1 2 3 7
    if loc[n-1]-loc[n-2] > 2 and loc[n-2]-loc[0] == n-2:
        return 2

    j = 0
    for i in range(n):
        # 滑动窗口(大小不固定)
        # index的差作cow的个数
        # 不重置j，因为窗口满足之后，就左端右移，然后看右端是否满足
        # 为什么用j+1，因为不想让j越界，debug走一遍就懂了
        while j+1<n and loc[j+1]-loc[i] < n:
            j += 1
        # 没办法恰好取到n的
        # 而是位置够，然后看该范围内已有多少cow，那么min_moves则是(n-amount)
        max_already = max(j-i+1, max_already)
    return n - max_already

loc = []
for i in range(n):
    c = int(input())
    loc.append(c)

loc.sort()

min_moves = get_min_moves()
max_moves = max(loc[n-2]-loc[0], loc[-1]-loc[1]) - (n-2)

print(min_moves)
print(max_moves)