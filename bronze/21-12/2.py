# 不往差分数组去想吧，找不到对应关系
# 但是差分的思想是可以有的
# 因为差值就是我们研究的东西

# [i]和[i-1]主要分为两种情况：同侧和异侧
# 同侧：
# 如果[i]比[i-1]小，则不用统计，因为[i-1]可以捎一下
# 如果[i]比[i-1]大，则他们的差值就是额外需要新加到sum里的，而剩余的路程[i-1]已经捎了
# 然后，同侧其实还得细分为x轴上方和下方，他们的sum计算不太一样，具体看代码

# 异侧：
# 肯定没办法捎了，直接加上距离

n = int(input())

target = list(map(int, input().split(" ")))
origin = list(map(int, input().split(" ")))
diff = []

for i in range(len(target)):
    diff.append(target[i] - origin[i])

# 它们之间的差值就是我们要额外调的次数
sum = abs(diff[0])
for i in range(1, len(diff)):
    # 同一侧
    if diff[i]*diff[i-1] > 0:
        if diff[i] > 0:
            sum += max(diff[i] - diff[i-1], 0)
        else:
            sum += max(diff[i-1] - diff[i], 0)
    else:
        sum += abs(diff[i])

print(sum)
