# 排列组合问题

n = int(input())
cow = list(map(int, input().split()))
stall = list(map(int, input().split()))

cow.sort(reverse=True)
stall.sort(reverse=True)

ans = 1
j = 0               # j对应牛棚, i对应牛
for i in range(n):  
    while j<n and stall[j] >= cow[i]:   # 找到可入牛棚数 j
        j += 1      
    ans *= j-i      # j-i = 可入牛棚数 - 已被占的牛棚数 = 当前牛可入的牛棚数

print(ans)
