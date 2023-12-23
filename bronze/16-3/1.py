# 滑动窗口
# 其实直接暴力枚举也行，1000 不会超时
# 唯一要注意的就是要与最小的比，而不是与第一个放入的相比 -- 还是要排序
# 还是用滑动窗口吧

import sys
sys.stdin = open("diamond.in", "r")
sys.stdout = open("diamond.out", "w")

n,k = map(int, input().split())
diamonds = [int(input()) for _ in range(n)]
diamonds.sort()

ans = 0
for i in range(n):
    for j in range(i, n):
        if diamonds[j] - diamonds[i] > k:
            break
        ans = max(ans, j-i+1)

print(ans)
