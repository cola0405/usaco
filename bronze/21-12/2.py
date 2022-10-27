# 问题转化
# 差分数组


# o:1 2 1 2 1
# t:1 5 2 8 4

# o:1 2 2 2 2
# t:3 0 3 3 3

# 1 5 3 3 4
# 1 2 2 2 1

# 引导作差




n = int(input())

target = list(map(int, input().split(" ")))
origin = list(map(int, input().split(" ")))
diff = [0]

for i in range(len(target)):
    diff.append(target[i] - origin[i])
diff.append(0)

# 它们之间的差值就是我们要额外调的次数
sum = 0
for i in range(1, len(diff)):
    sum += max(diff[i] - diff[i-1], 0)

print(sum)
