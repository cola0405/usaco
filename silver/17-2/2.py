# 最优情况肯定是x ... x
# 但是要注意的是，左右的x也可能需要修
# 解决办法是额外加两边边界



import sys
sys.stdin = open("maxcross.in", "r")
sys.stdout = open("maxcross.out", "w")

n,k,b = map(int, input().split())

# 加两边边界
broken = [0, n+1]
for i in range(b):
    broken.append(int(input()))

broken.sort()
b += 2
p = [0]*(n+3)
i = 1
j = 0
while i<=n:
    if j<b and i == broken[j]:
        p[i] = p[i-1]+1
        j += 1
    else:
        p[i] = p[i-1]
    i += 1

min_op = float("inf")
for i in range(b):
    if n-broken[i]+1 < k:
        break
    for j in range(i+1, b):
        # 只修中间的若干个
        if broken[j]-broken[i] - 1 >= k:
            min_op = min(j-i - 1, min_op)

print(min_op)
