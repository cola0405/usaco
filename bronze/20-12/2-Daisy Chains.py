# Daisy Chains
# 模拟
# 前缀和


ans = int(input())
lst = list(map(int, input().split(" ")))
pre_sum = [0]
s = 0
for i in lst:
    s += i
    pre_sum.append(s)

for i in range(1, len(pre_sum)):
    for j in range(i+1, len(pre_sum)):
        ij_sum = pre_sum[j] - pre_sum[i-1]
        average = ij_sum // (j - i + 1)
        if ij_sum % (j-i+1) == 0 and average in lst[i-1:j]:
            ans += 1

print(ans)


