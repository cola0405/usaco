# analyse

# 题意：
# 给定一个列表，每次可以把相邻两个元素减1，问经过多少次操作后，列表内各元素相等

# 通过手推，会发现我们会关注相邻的三个元素
# 选择某两个元素来减，使得中间元素和第三个元素相等
# 然后再调整中间元素和第三个元素，使这三个元素相等

# ps：大体思路是这样，但是会存在不可调整的情况，这时就返回-1

t = int(input())
for _ in range(t):
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(1, n-1):
        if h[i] > h[i+1]:
            gap = h[i] - h[i+1]
            h[i] -= gap
            h[i-1] -= gap
            ans += 2*gap
        if h[i] > h[i-1]:
            gap = h[i] - h[i-1]
            h[i] -= gap
            h[i+1] -= gap
            ans += 2*gap

    for i in range(1, n-1)[::-1]:   # 还需要反着来一遍，参考测试用例：10 8 6
        if h[i] > h[i+1]:
            gap = h[i] - h[i+1]
            h[i] -= gap
            h[i-1] -= gap
            ans += 2*gap
        if h[i] > h[i-1]:
            gap = h[i] - h[i-1]
            h[i] -= gap
            h[i+1] -= gap
            ans += 2*gap

    for i in range(n-1):
        if h[i] != h[i+1] or h[i] < 0:
            print(-1)
            break
    else:
        print(ans)