# 模拟
# 前缀和
# 也可以模拟，那就是组合问题

ans = int(input())
flowers = list(map(int, input().split(" ")))
s = 0

for i in range(len(flowers)):
    for j in range(i+1, len(flowers)):
        ij_sum = sum(flowers[i:j+1])
        average = ij_sum // (j-i+1)
        # 保证是整除
        if ij_sum%(j-i+1) == 0 \
                and average in flowers[i:j+1]:
            ans += 1

print(ans)


