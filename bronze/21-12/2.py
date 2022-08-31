# 问题转化
# 差分数组

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
