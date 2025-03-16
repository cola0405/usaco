# python 没办法全过

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * len(arr))
        self.build(arr, 0, 0, self.n-1)     # node = 0 表示开始构建根节点

    # 父节点是两个子节点的最大值
    # 递归构建线段树，那么列表左半部分的最大值则为根节点的左孩子，右半部分的最大值为右孩子，以此类推
    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            left = 2*node + 1
            right = 2*node + 2
            self.build(arr, left, start, mid)
            self.build(arr, right, mid+1, end)
            self.tree[node] = max(self.tree[left], self.tree[right])

    # 查询 (l,r)区间的最大值
    def query(self, node, start, end, l, r):
        if r < start or l > end:
            return float('-inf')
        # 如果当前区间在 (l,r)内，则返回当前区间的最大值，让上层递归再汇总其他区域的最大值
        if l <= start and end <= r:
            return self.tree[node]

        # 部分包含
        mid = (start + end) // 2

        # 当前 node节点的两个孩子
        left = 2*node + 1
        right = 2*node + 2
        return max(self.query(left, start, mid, l, r), self.query(right, mid+1, end, l, r))

    def max(self, l, r):
        return self.query(0, 0, self.n-1, l, r)


import sys
sys.stdin = open('teamwork.in', 'r')
sys.stdout = open('teamwork.out', 'w')

n,k = map(int,input().split())
s = [int(input()) for _ in range(n)]
if n == 1:
    print(s[0])
    exit()

dp = [0]*(n+1)
dp[1] = s[0]
dp[2] = max(s[0], s[1]) * 2
seg = SegmentTree(s)
for i in range(2,n):
    for j in range(k):
        if i-j < 0: continue
        dp[i+1] = max(dp[i+1], dp[i-j] + seg.max(i-j, i) * (j+1))
print(dp[-1])
